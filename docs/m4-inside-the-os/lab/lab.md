**# Lab — M4: look inside a running machine (in your Codespace)**

**You'll need:** your **Codespace** terminal (Linux in your browser). **Nothing to install.**
New to it? See **[How to open your Codespace](../../resources/install-guides/codespaces.md)**.
**Time:** ~30 minutes • **Work in your breakout pair** — your numbers will differ, that's the point.

> Heads up: *looking* at processes is completely safe. The only thing we'll **stop** is a harmless
> practice program we start ourselves. If unsure whether something's safe to stop — leave it.

---

## Step 1 — Meet the resource manager
```text
$ nproc
$ free -h
```

✅ **You should now see:** `nproc` prints how many **CPU cores** you have; `free -h` shows memory **total / used / free**. This is the OS's job in two numbers: share these cores and this memory among everything.

## Step 2 — See everything running (live)
```text
$ top
```
Watch it update, then press **`q`** to quit.

✅ **You should now see:** a live, self-updating list of processes with a summary of tasks and memory at the top. That's *everything* the machine is doing right now.

## Step 3 — Find the memory hog (snapshot + pipe)
```text
$ ps aux --sort=-%mem | head -6
```

✅ **You should now see:** the top few processes by memory, biggest first. (You just combined `ps` with the `head` pipe from M3.) The one on top is your hungriest process.

## Step 4 — Start a harmless practice process
`sleep` does nothing but wait — perfect to practice on. Run it in the background with `&`:
```text
$ sleep 300 &
```

✅ **You should now see:** a line like `[1] 4567` — that number is its **PID** (process ID). The process is now running in the background.

## Step 5 — Find it, then stop it by PID
```text
$ ps               # find your sleep and its PID
$ kill 4567        # use YOUR number from above
$ ps               # it's gone
```

✅ **You should now see:** `kill` ends the process; the second `ps` no longer lists `sleep`. You stopped a program by **naming its PID** — exactly how you'd rescue a frozen app without rebooting. *(Tip: `Ctrl-C` stops a program running in the foreground.)*

## Step 6 — Read a file's permissions
```text
$ touch demo.txt
$ ls -l demo.txt
```

✅ **You should now see:** a line starting like **`-rw-r--r--`**. Read it: `-` = a file; `rw-` = **you (owner)** can read+write; the two `r--` groups = **your group** and **everyone else** can only read.

## Step 7 — Change permissions, and see who you are
```text
$ chmod 600 demo.txt
$ ls -l demo.txt
$ id
```

✅ **You should now see:** after `chmod 600`, the permissions become **`-rw-------`** — now *only you* can read/write it. `id` shows your username and groups — *that's* the "owner" the permissions refer to. (Tidy up: `rm demo.txt`.)

## Step 8 — The container trick (look, don't worry if it errors)
A container is just the OS fencing a process off with **namespaces** (what it can *see*) and **cgroups** (what it can *use*). Peek at the namespaces on your machine:
```text
$ ls -l /proc/self/ns
```

✅ **You should now see:** a list of namespace entries (like `mnt`, `pid`, `net`, …). Each is a "fence" the OS can put around a process. **This exact mechanism is what M10's containers are built on** — you're looking at the engine now.

---

## 🎉 Your win
You watched everything a machine is running, found the memory hog, safely stopped a process by its
PID, read and changed permissions, and saw the namespaces that make containers possible.

**Post it to the chat wins board:** *"My biggest memory hog is ___, and I killed a process I started 🎉"*

## Take-home (optional)
Next time an app freezes on your own computer, don't reboot — open your process viewer (Task Manager
/ Activity Monitor), find it, and End task. You'll fix it in seconds without losing anything else.
