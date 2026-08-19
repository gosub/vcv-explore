#!/usr/bin/env python3
"""edit_session.py - open one patch for description editing.

The descriptions in the quarter readmes are the author's, not a reading of the
cables, so each one gets written with the patch actually playing. This puts the
two halves of that in place: Rack running the patch, audible, and an emacs
sitting on the exact line of the readme where that patch's description starts.

    python3 tools/edit_session.py 2026-Q3               # list the entries
    python3 tools/edit_session.py 2026-Q3 tilt_shift    # open that one
    python3 tools/edit_session.py 2026-Q3 --stop        # close Rack again

Each call stops the Rack the previous call started, so patches never end up
playing over each other. The emacs runs its own server (--server-name=vcvedit
by default), which keeps it clear of whatever emacs is already open.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACK_DIR = os.path.expanduser("~/dl/audio/rack")
RACK_HOME = os.path.expanduser("~/dl/audio/rackhome")
PIDFILE = os.path.join(tempfile.gettempdir(),
                       "vcv_explore_edit_session.%d.pid" % os.getuid())


def die(msg):
    sys.exit("edit_session: %s" % msg)


def entries(readme):
    """One dict per '## title - date (VCV Rack x)' entry in the readme.

    Reports the line the heading is on, the line the description starts on,
    and the line its second paragraph starts on. The second paragraph is the
    one my drafts put the invented material in, so that is where the cursor
    goes: the first paragraph is usually just the signal path.
    """
    lines = open(readme).read().split("\n")
    out = []
    for i, line in enumerate(lines):
        m = re.match(r"^## (.+?) - (\d{4}-\d{2}-\d{2})\b", line)
        if not m:
            continue
        # Walk past the screenshot and the module table to the first prose line.
        j, seen_table = i + 1, False
        while j < len(lines):
            s = lines[j].strip()
            if s.startswith("|"):
                seen_table = True
            elif seen_table and s:
                break
            j += 1
        k = j
        while k < len(lines) and lines[k].strip():
            k += 1
        while k < len(lines) and not lines[k].strip():
            k += 1
        second = k + 1 if k < len(lines) and not lines[k].startswith("## ") else j + 1
        out.append({"title": m.group(1), "date": m.group(2),
                    "heading": i + 1, "desc": j + 1, "second": second})
    return out


def find_patch(quarter_dir, entry):
    """The .vcv the entry describes, matched on its date prefix."""
    cands = sorted(f for f in os.listdir(quarter_dir)
                   if f.startswith(entry["date"]) and f.endswith(".vcv"))
    if not cands:
        die("no .vcv dated %s in %s" % (entry["date"], quarter_dir))
    if len(cands) > 1:
        slug = entry["title"].replace(" ", "_").lower()
        exact = [f for f in cands if slug in f.lower()]
        if len(exact) != 1:
            die("several patches dated %s: %s" % (entry["date"], ", ".join(cands)))
        cands = exact
    return os.path.join(quarter_dir, cands[0])


def stop_rack():
    """Stop the Rack this script started last, if it is still up."""
    if not os.path.exists(PIDFILE):
        return False
    try:
        pid = int(open(PIDFILE).read().strip())
        os.kill(pid, 15)
        for _ in range(40):
            time.sleep(0.25)
            try:
                os.kill(pid, 0)
            except OSError:
                break
    except (OSError, ValueError):
        pass
    os.remove(PIDFILE)
    return True


def start_rack(patch):
    env = dict(os.environ, HOME=RACK_HOME)
    p = subprocess.Popen([os.path.join(RACK_DIR, "Rack"), patch],
                         cwd=RACK_DIR, env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    open(PIDFILE, "w").write(str(p.pid))
    return p.pid


def emacs_up(server):
    return subprocess.run(["emacsclient", "-s", server, "-e", "t"],
                          capture_output=True).returncode == 0


def emacs_at(server, readme, line):
    """Put the dedicated emacs on readme:line, starting it if it is not up."""
    if not emacs_up(server):
        subprocess.Popen(
            ["emacs", "--eval",
             '(progn (setq server-name "%s") (server-start))' % server,
             "+%d" % line, readme],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(60):
            time.sleep(0.5)
            if emacs_up(server):
                return "started"
        return "started (server not answering yet)"
    subprocess.run(["emacsclient", "-s", server, "-n", "+%d" % line, readme],
                   capture_output=True)
    subprocess.run(["emacsclient", "-s", server, "-n", "-e",
                    "(progn (raise-frame)"
                    " (select-frame-set-input-focus (selected-frame)))"],
                   capture_output=True)
    return "jumped"


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("quarter", help="quarter folder, e.g. 2026-Q3")
    ap.add_argument("entry", nargs="?",
                    help="entry title or a unique prefix of it; "
                         "underscores stand in for spaces")
    ap.add_argument("--stop", action="store_true",
                    help="just stop the running Rack and exit")
    ap.add_argument("--server", default="vcvedit", help="emacs server name")
    ap.add_argument("--line", choices=["desc", "second", "heading"],
                    default="second", help="where to land the cursor")
    args = ap.parse_args()

    if args.stop:
        print("rack stopped" if stop_rack() else "no rack of mine was running")
        return

    quarter_dir = os.path.join(REPO, args.quarter)
    readme = os.path.join(quarter_dir, "readme.md")
    if not os.path.exists(readme):
        die("no readme at %s" % readme)
    found = entries(readme)
    if not found:
        die("no entries in %s" % readme)

    if not args.entry:
        for e in found:
            print("%-34s heading %4d  desc %4d  2nd para %4d"
                  % (e["title"], e["heading"], e["desc"], e["second"]))
        return

    want = args.entry.replace("_", " ").lower()
    hits = [e for e in found if e["title"].lower().startswith(want)]
    if len(hits) != 1:
        die("no unique entry for %r (matched %d of %d)"
            % (args.entry, len(hits), len(found)))
    entry = hits[0]
    patch = find_patch(quarter_dir, entry)

    stop_rack()
    pid = start_rack(patch)
    line = entry[args.line]
    state = emacs_at(args.server, readme, line)
    print("patch:  %s" % os.path.basename(patch))
    print("rack:   pid %d" % pid)
    print("emacs:  %s, at %s/readme.md:%d (%s)"
          % (state, args.quarter, line, args.line))


if __name__ == "__main__":
    main()
