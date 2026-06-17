# M4 — Inside the OS: what's really happening

> Right now, behind your wallpaper, your computer is juggling *hundreds* of running programs across
> a handful of cores, shuffling memory, and quietly enforcing who can touch what. Today we open
> that hidden control room, take the controls — and discover the exact OS trick that powers
> containers (you'll use it for real in M10).

**Today's win:** you can see everything running on a machine, find the memory hog, stop a misbehaving process *without* rebooting, and read a file's permissions — and you can explain how the OS shares a few cores among hundreds of programs.

### Today you will
- Watch live processes and **spot the memory hog** (`top`, `ps`)
- Safely **start and stop** a process by its **PID** (`kill`)
- Read and change **permissions** (`ls -l`, `chmod`) — and meet **namespaces + cgroups**, the container trick

### Environment
We work in a **Codespace** — a Linux terminal in your browser. New to it? See **[How to open your Codespace](../resources/install-guides/codespaces.md)**.

### Run of show (~50 min)
| Time | What we do |
|------|------------|
| 0:00 | Hook + the win we're chasing |
| 0:05 | The big ideas: processes, the scheduler, memory, permissions (recap in [`notes.md`](notes.md)) |
| 0:10 | **Lab** — look inside a running machine (breakout pairs) |
| 0:40 | **Show** — post "My biggest memory hog is ___, and I killed a process I started 🎉" |
| 0:45 | Wrap + take-home |

### If you get stuck
- Nothing here harms anything — viewing is safe, and we only stop a harmless practice process we start ourselves.
- Re-read the **✅ You should now see** line. Numbers differ on every machine — compare with your breakout partner.
- Keep the [cheat-card](../resources/cheat-cards/linux-commands.md) open; press **`q`** to leave `top`.

### Optional challenge
Use a pipe (from M3) to show only the **top 5** memory users: `ps aux --sort=-%mem | head -6`. What's #1, and why do you think it's so hungry?
