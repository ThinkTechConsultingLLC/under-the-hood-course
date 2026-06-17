# Lab — M3: the command line (in your Codespace)

**You'll need:** your **Codespace** terminal — a Linux computer in your browser. **Nothing to install.**
First time opening it? See **[How to open your Codespace](../../resources/install-guides/codespaces.md)**.
**Time:** ~30 minutes • **Work in your breakout pair** — compare each other's screens.

> Heads up: you **cannot** break anything by typing a command name — a wrong one just says
> "command not found." The *one* command to slow down for is `rm` (delete), which is permanent.
> Keep the [cheat-card](../../resources/cheat-cards/linux-commands.md) open in another tab.

The same things you did by clicking in M2, you'll now do by typing — and then some.

---

## Step 1 — Find the terminal
In your Codespace, the **Terminal** panel is at the bottom (if hidden: menu → Terminal → New Terminal).

✅ **You should now see:** a prompt ending in `$` with a blinking cursor.

## Step 2 — Where am I, and what's here?
```text
$ pwd
$ ls
```

✅ **You should now see:** `pwd` prints your current folder's path (something like `/workspaces/...`); `ls` lists what's in it.

## Step 3 — Prove errors are safe
Type gibberish, e.g. `helllo`, and press Enter.

✅ **You should now see:** `bash: helllo: command not found`, then the prompt again. Nothing broke. **This is your playground** — say it with your partner.

## Step 4 — Make a folder and go in
```text
$ mkdir practice
$ cd practice
$ pwd
```

✅ **You should now see:** `mkdir` says nothing (silence = success), and `pwd` now ends in `/practice`.

## Step 5 — Create a file and read it
```text
$ echo "hello from the command line" > note.txt
$ ls
$ cat note.txt
```

✅ **You should now see:** `ls` lists `note.txt`, and `cat` prints `hello from the command line`. (You just used `>` to send text into a file — more on that in Step 9.)

## Step 6 — Copy, then rename
```text
$ cp note.txt backup.txt
$ mv note.txt journal.txt
$ ls
```

✅ **You should now see:** `backup.txt` and `journal.txt`. (`cp` copied; `mv` renamed `note.txt`.)

## Step 7 — Look closer, then delete
```text
$ ls -l
$ rm backup.txt
$ ls
```

✅ **You should now see:** `ls -l` shows a detailed row per file (starting with a `-rw-r--r--` permissions code — that's M4); after `rm`, only `journal.txt` remains. ⚠️ `rm` is permanent — read the name first.

## Step 8 — Run a program
```text
$ whoami
$ date
$ cal
```

✅ **You should now see:** your username, the date/time, and this month's calendar. These are little programs you just *ran*.

## Step 9 — Redirection: send output to a file
```text
$ echo "line one" > log.txt
$ echo "line two" >> log.txt
$ cat log.txt
```

✅ **You should now see:** `cat` prints **both** lines. `>` writes (replacing); `>>` adds to the end. You're capturing output instead of just watching it scroll by.

## Step 10 — Pipes: snap commands together
A **pipe** (`|`) feeds one command's output into the next:
```text
$ ls | wc -l
$ ls /usr/bin | wc -l
$ ls -l | grep txt
```

✅ **You should now see:** the first counts files in this folder; the second counts the **programs installed** (a big number!); the third lists only lines containing `txt`. **That's the superpower:** small commands combined into something new.

---

## 🎉 Your win
In a real Linux terminal you moved around, created/copied/renamed/deleted files, ran programs,
and **chained commands** with pipes and redirection — all by typing.

**Post it to the chat wins board:** *"I chained commands: `ls | wc -l` says I have ___ files! 🎉"*

## Take-home (optional)
Open the [cheat-card](../../resources/cheat-cards/linux-commands.md) and try three commands you
haven't used yet (e.g. `head`, `tail`, `grep`). Looking things up *is* the skill.
