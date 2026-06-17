# M3 — The command line

> You've seen it in movies — someone hunched over a black screen, typing fast, looking like a
> wizard. Today you become that person (minus the dramatic music). The "scary black screen"
> becomes the fastest, most precise way you own to tell a computer what to do — and you'll even
> learn to snap commands together to do things a mouse can't.

**Today's win:** in a real Linux terminal, you move around, create/copy/rename/delete files, run programs, and **chain commands together** — all by typing.

### Today you will
- Use `pwd`, `ls`, `cd` to move around, and `mkdir`, `cp`, `mv`, `rm` to manage files
- **Combine commands** with pipes (`|`) and redirection (`>`) — the command line's superpower
- Start your own **commands cheat-card** habit (look things up, don't memorize)

### Environment
We work in a **Codespace** — a ready-made Linux terminal in your browser, the same for everyone.
First time? See **[How to open your Codespace](../resources/install-guides/codespaces.md)**. (No install.)

### Run of show (~50 min)
| Time | What we do |
|------|------------|
| 0:00 | Hook + the win we're chasing |
| 0:05 | The big ideas: terminal vs shell, a command's parts, and combining commands (recap in [`notes.md`](notes.md)) |
| 0:10 | **Lab** — open your Codespace and go (breakout pairs) |
| 0:40 | **Show** — post "I chained commands: `ls \| wc -l` told me I have ___ files! 🎉" |
| 0:45 | Wrap + take-home |

### If you get stuck
- **Errors are safe** — a wrong command just says *command not found* and waits. You can't break anything by typing.
- Re-read the **✅ You should now see** line; compare with your breakout partner.
- Press **↑** to recall your last command, **Tab** to auto-complete, and keep the [cheat-card](../resources/cheat-cards/linux-commands.md) open.

### Optional challenge
Use a pipe to answer: **how many programs are installed in your Codespace?** (Hint: list `/usr/bin` and count the lines.) Bring the number to the chat.
