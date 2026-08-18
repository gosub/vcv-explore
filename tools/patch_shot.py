#!/usr/bin/env python3
"""patch_shot.py — screenshot a VCV Rack patch, and dump what is in it.

A .vcv patch cannot be photographed from the outside: Rack has to load it and
show it. So a throwaway copy of the patch gets one extra module, forsitan
modulare's limen, whose TCP server is the handle everything else pulls on.
Rack opens the copy, limen parks itself flush against the right edge of the
patch, the view goes fullscreen and zooms to fit, and only then does limen
step off screen — the framing already includes the space it was standing in,
so it leaves without disturbing the shot.

    python3 tools/patch_shot.py 2026-Q3/2026-07-06_for_eliane.vcv

writes 2026-Q3/media/2026-07-06_for_eliane.webp (1000x625, matching the
screenshots already in the repo) and, with --dump, a sidecar .json holding
the module list and cable list read back out of the running Rack — the raw
material for the readme entry.

Needs: Rack, the forsitan plugin installed (limen protocol >= 2), grim,
ImageMagick, tar and zstd.
"""

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

RACK_BIN = os.path.expanduser("~/dl/audio/rack/Rack")
RACK_USER = os.path.expanduser("~/dl/audio/rackhome/.local/share/Rack2")
PLUGIN_DIR = "plugins-lin-x64"
# Somewhere no patch reaches, for limen to wait in and retire to.
EXILE = (4000, 900)


def die(msg):
    sys.exit("patch_shot: " + msg)


class Limen:
    """One JSON object per line, one reply per line."""

    def __init__(self, host, port, timeout=20.0):
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self.buf = b""

    def close(self):
        self.sock.close()

    def call(self, cmd, **fields):
        req = {"cmd": cmd}
        req.update(fields)
        self.sock.sendall((json.dumps(req) + "\n").encode())
        while b"\n" not in self.buf:
            chunk = self.sock.recv(1 << 20)
            if not chunk:
                die("limen closed the connection")
            self.buf += chunk
        line, self.buf = self.buf.split(b"\n", 1)
        resp = json.loads(line.decode())
        if not resp.get("ok"):
            die("limen: %s (%s)" % (resp.get("error", "unknown error"), cmd))
        return resp.get("result")


# ── patch file ───────────────────────────────────────────────────────────────

def read_patch(path):
    """patch.json out of the zstd-compressed tar that a .vcv is."""
    raw = subprocess.run(["zstd", "-dc", path], check=True,
                         stdout=subprocess.PIPE).stdout
    return json.loads(subprocess.run(["tar", "-xO", "./patch.json"], input=raw,
                                     check=True, stdout=subprocess.PIPE).stdout)


def write_patch(patch, path):
    with tempfile.TemporaryDirectory() as d:
        os.mkdir(os.path.join(d, "modules"))
        with open(os.path.join(d, "patch.json"), "w") as f:
            json.dump(patch, f, indent=2)
        tar = os.path.join(d, "out.tar")
        subprocess.run(["tar", "-cf", tar, "./modules", "./patch.json"],
                       cwd=d, check=True)
        subprocess.run(["zstd", "-q", "-f", tar, "-o", path], check=True)


def with_limen(patch, port):
    """A copy of the patch with one limen bolted on, server already listening.

    It is parked far away: the real position is chosen later, once Rack can be
    asked how wide every module actually is.
    """
    patch = json.loads(json.dumps(patch))
    ids = [m.get("id", 0) for m in patch.get("modules", [])]
    patch.setdefault("modules", []).append({
        "id": max(ids, default=0) + 1,
        "plugin": "forsitan",
        "model": "limen",
        "pos": list(EXILE),
        "params": [],
        "data": {"port": port, "serverEnabled": True},
    })
    return patch


def user_dir():
    """A throwaway Rack user dir borrowing the real one's plugins.

    The patches need every plugin the real Rack home has, but not its
    settings: the tips dialog, the CPU meter and parameter tooltips would all
    end up in the picture.
    """
    plugins = os.path.join(RACK_USER, PLUGIN_DIR)
    if not os.path.isdir(plugins):
        die("no plugins at %s" % plugins)
    d = tempfile.mkdtemp(prefix="patch-shot-")
    os.symlink(plugins, os.path.join(d, PLUGIN_DIR))
    with open(os.path.join(d, "settings.json"), "w") as f:
        json.dump({"showTipsOnLaunch": False, "cpuMeter": False,
                   "tooltips": False, "autoCheckUpdates": False,
                   "skipLoadOnLaunch": False}, f)
    return d


def connect(host, port, timeout):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            return Limen(host, port)
        except OSError:
            time.sleep(0.5)
    die("limen never answered on %s:%d" % (host, port))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("patch", help="the .vcv file to shoot")
    ap.add_argument("-o", "--out", help="output image (default: <dir>/media/<name>.webp)")
    ap.add_argument("--dump", action="store_true",
                    help="also write <out>.json with the module and cable lists")
    ap.add_argument("--max-size", type=int, default=1000,
                    help="cap the longest side at this many px (default: %(default)s)")
    ap.add_argument("--quality", type=int, default=82, help="webp quality (default: %(default)s)")
    ap.add_argument("--settle", type=float, default=2.0,
                    help="seconds to wait after fullscreen and after the zoom")
    ap.add_argument("--load", type=float, default=3.0,
                    help="extra seconds for the patch to draw itself before framing")
    ap.add_argument("--mute", action="store_true",
                    help="mute the default sink while the patch is open")
    ap.add_argument("--port", type=int, default=7000)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--output", help="grim output name, for a multi-monitor setup")
    ap.add_argument("--keep-open", action="store_true", help="leave Rack running")
    args = ap.parse_args()

    for tool in ("zstd", "tar", "grim"):
        if not shutil.which(tool):
            die("%s not found on PATH" % tool)
    magick = shutil.which("magick") or shutil.which("convert")
    if not magick:
        die("ImageMagick not found on PATH")
    if not os.access(RACK_BIN, os.X_OK):
        die("no Rack binary at %s" % RACK_BIN)

    src = os.path.abspath(args.patch)
    name = os.path.splitext(os.path.basename(src))[0]
    out = args.out or os.path.join(os.path.dirname(src), "media", name + ".webp")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    patch = read_patch(src)
    tmpdir = tempfile.mkdtemp(prefix="patch-shot-patch-")
    shot_patch = os.path.join(tmpdir, name + ".vcv")
    write_patch(with_limen(patch, args.port), shot_patch)

    udir = user_dir()
    muted = False
    if args.mute and shutil.which("wpctl"):
        subprocess.run(["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "1"])
        muted = True

    proc = subprocess.Popen([RACK_BIN, "-u", udir, shot_patch],
                            cwd=os.path.dirname(RACK_BIN),
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    limen = None
    try:
        limen = connect(args.host, args.port, timeout=90)
        if limen.call("hello")["protocol"] < 2:
            die("limen protocol 2 is needed for move_module")

        mods = limen.call("list_modules")
        me = [m for m in mods if m["plugin"] == "forsitan" and m["model"] == "limen"]
        others = [m for m in mods if m not in me]
        if not others:
            die("the patch has no modules besides limen")
        if len(me) != 1:
            die("expected exactly one limen, found %d" % len(me))
        me = me[0]

        # Flush against the right edge of the patch, on its topmost row: the
        # smallest bite limen can take out of the framing.
        right = max(m["pos"]["x"] + m["hp"] for m in others)
        top = min(m["pos"]["y"] for m in others)
        for mode in ("strict", "nearest"):
            try:
                limen.call("move_module", id=me["id"], x=right, y=top, mode=mode)
                break
            except SystemExit:
                continue

        # Let the patch finish drawing: modules with displays come up blank and
        # fill in over the first seconds, and a blank display is a poor portrait.
        time.sleep(args.load)
        # Fullscreen frees the whole screen, but the compositor takes its time;
        # zooming before the viewport has grown fits to the old size.
        limen.call("set_fullscreen", on=True)
        time.sleep(args.settle)
        limen.call("zoom_to_modules")
        time.sleep(args.settle)
        # The framing is fixed now, so limen can leave without moving it.
        limen.call("move_module", id=me["id"], x=EXILE[0], y=EXILE[1], mode="force")
        time.sleep(0.7)

        png = os.path.join(tmpdir, "shot.png")
        capture = ["grim"] + (["-o", args.output] if args.output else []) + [png]
        subprocess.run(capture, check=True)
        # Shrink-only fit inside a max_size box: the grab is at screen
        # resolution, whatever that happens to be, and only its longest side
        # is pinned.
        subprocess.run([magick, png, "-filter", "Lanczos",
                        "-resize", "%dx%d>" % (args.max_size, args.max_size),
                        "-strip", "-quality", str(args.quality), out], check=True)
        print("wrote %s" % out)

        if args.dump:
            plugins = {p["slug"]: p["name"] for p in limen.call("list_plugins")}
            by_id = {m["id"]: m for m in others}
            ports = {m["id"]: limen.call("list_ports", id=m["id"]) for m in others}

            def side(mid, kind, idx):
                """"Module OUT" for one end of a cable, named where Rack names it."""
                mod = by_id.get(mid)
                if not mod:
                    return "?"
                entries = ports.get(mid, {}).get(kind, [])
                label = next((e["name"] for e in entries if e["id"] == idx), "") or "#%d" % idx
                return "%s %s" % (mod["name"], label)

            info = {
                "patch": os.path.basename(src),
                "rack_version": patch.get("version"),
                "modules": sorted(
                    ({"plugin": m["plugin"], "plugin_name": plugins.get(m["plugin"], m["plugin"]),
                      "model": m["model"], "name": m["name"], "hp": m["hp"],
                      "id": m["id"], "x": m["pos"]["x"], "y": m["pos"]["y"]}
                     for m in others),
                    key=lambda m: (m["y"], m["x"])),
                "signal_flow": [
                    "%s -> %s" % (side(c["outputModule"], "outputs", c["outputPort"]),
                                  side(c["inputModule"], "inputs", c["inputPort"]))
                    for c in limen.call("list_cables")],
            }
            with open(out + ".json", "w") as f:
                json.dump(info, f, indent=2)
            print("wrote %s.json" % out)
    finally:
        if limen and not args.keep_open:
            try:
                limen.call("quit")
            except SystemExit:
                pass
            limen.close()
        if not args.keep_open:
            try:
                proc.wait(timeout=20)
            except subprocess.TimeoutExpired:
                proc.kill()
            shutil.rmtree(udir, ignore_errors=True)
            shutil.rmtree(tmpdir, ignore_errors=True)
        if muted:
            subprocess.run(["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "0"])


if __name__ == "__main__":
    main()
