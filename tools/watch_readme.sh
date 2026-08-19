#!/bin/bash
# watch_readme.sh - report every save to a quarter's readme, one line each.
#
# The other half of the description review loop (see edit_session.py): while
# the author writes an entry, this says when they have saved, so the text can
# be picked up and translated or corrected without polling the file by hand.
#
#     tools/watch_readme.sh 2026-Q3      # watch, one line per save
#     tools/watch_readme.sh --pause      # stop reporting saves
#     tools/watch_readme.sh --resume     # report them again
#
# Writing back into the same file is part of the loop, and so is the buffer
# revert that follows it, so both come back as saves that are not the author's.
# Wrap those writes in --pause and --resume: changes made while paused are
# absorbed silently instead of being reported.
#
# Polls md5, because inotify-tools is not installed on this machine.

set -u

REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
FLAG="${TMPDIR:-/tmp}/vcv_explore_watch.$(id -u).paused"

case "${1:-}" in
  --pause)  touch "$FLAG"; echo "paused: saves will not be reported"; exit 0 ;;
  --resume) rm -f "$FLAG"; echo "watching again"; exit 0 ;;
  --flag)   echo "$FLAG"; exit 0 ;;
  "" | -h | --help)
    sed -n '2,18p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 0 ;;
esac

F="$REPO/$1/readme.md"
[ -f "$F" ] || { echo "watch_readme: no readme at $F" >&2; exit 1; }

prev=$(md5sum "$F" | cut -d' ' -f1)
while true; do
  sleep 1
  cur=$(md5sum "$F" 2>/dev/null | cut -d' ' -f1) || continue
  [ -n "$cur" ] || continue
  if [ "$cur" != "$prev" ]; then
    prev=$cur
    [ -e "$FLAG" ] && continue
    echo "$1/readme.md saved at $(date +%H:%M:%S)"
  fi
done
