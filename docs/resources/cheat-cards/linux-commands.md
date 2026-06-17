# Cheat-card — Linux commands

Keep this open while you work. **You don't memorize commands — you look them up.** These work in
your Codespace (Linux/bash). Try one and read what happens; you can't break anything by *listing*.

## The daily 8 (90% of what you'll use)
| Command | Does | Example |
|---|---|---|
| `pwd` | print working directory ("where am I?") | `pwd` |
| `ls` | list what's here | `ls`,  `ls -l`,  `ls -a` |
| `cd` | change directory ("go there") | `cd practice`,  `cd ..`,  `cd ~` |
| `mkdir` | make a folder | `mkdir practice` |
| `cp` | copy | `cp a.txt b.txt` |
| `mv` | move **or rename** | `mv a.txt b.txt` |
| `rm` | remove (⚠️ permanent) | `rm a.txt`,  `rm -r folder` |
| `cat` | show a file's contents | `cat note.txt` |

## Getting around
- `pwd` — where am I
- `ls` — list • `ls -l` long/detailed • `ls -a` show hidden (dot) files • `ls -la` both
- `cd folder` — go in • `cd ..` — up one • `cd ~` or `cd` — home • `cd -` — back to previous

## Files & folders
- `mkdir name` — make a folder • `mkdir -p a/b/c` — make nested folders
- `touch file` — create an empty file (or update its timestamp)
- `cp src dst` — copy • `cp -r src dst` — copy a folder
- `mv src dst` — move or rename
- `rm file` — delete (⚠️ no Recycle Bin) • `rm -r folder` — delete a folder + contents

## Looking inside & searching
- `cat file` — print the whole file
- `less file` — scroll a long file (press `q` to quit)
- `head file` / `tail file` — first / last lines • `tail -f file` — follow live
- `grep word file` — find lines containing `word` • `grep -r word .` — search a whole folder
- `wc -l file` — count lines • `wc -w` — words

## Combining commands (the superpower)
- `command > file` — send output **into** a file (replaces it)
- `command >> file` — **append** output to a file
- `a | b` — **pipe**: send `a`'s output into `b`
- Examples: `ls | wc -l` (count files) • `ls /usr/bin | wc -l` (count programs) • `ls -l | grep txt` (only .txt)

## Getting help
- `command --help` — quick usage for almost any command
- `man command` — the full manual (if installed; press `q` to quit)
- **↑ / ↓** — recall previous commands • **Tab** — auto-complete a name • **Ctrl-C** — stop a running command

## Knowing your machine (more in M4)
- `whoami` — your username • `date` — date/time • `cal` — calendar
- `df -h` — disk space • `ps` / `top` — running programs (M4)

---
**Further reference:** a large public Linux-commands list lives at
<https://github.com/beskridge/Linux101-Resources/blob/main/all-commands.md> (~200 commands, grouped).
This card re-expresses the essentials in our own words; check that source's licence before redistributing *it*.
