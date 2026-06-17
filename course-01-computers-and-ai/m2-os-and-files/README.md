# M2 — The OS, booting, & the filesystem

> Ever wonder what actually happens in those few seconds between pressing the power button and
> seeing your desktop? Or saved a file and had no idea where it went? Today both mysteries end:
> you'll trace your computer from cold metal to login, and learn to put your hand on *any* file
> on purpose.
> <!-- HUMAN: review/replace this hook. The instructor's voice and relatability are the whole point. -->

**Today's win:** you can explain what the operating system does, trace how your computer **boots** (power → firmware → bootloader → OS), and find any file on your machine *on purpose* by reading its path.

### Today you will
- Name what the **OS** manages, and watch the **boot sequence** happen on your own machine
- See your computer's **firmware** and **filesystem type** (APFS / NTFS / ext4)
- Build a tidy folder structure and read a file's **path** to jump straight to it

### Run of show (~50 min)
| Time | What we do |
|------|------------|
| 0:00 | Hook + the win we're chasing |
| 0:05 | The big ideas: the OS as manager; the boot chain; files live in a tree (full recap in [`notes.md`](notes.md)) |
| 0:10 | **Lab** — trace your boot + explore your filesystem (breakout pairs) |
| 0:40 | **Show** — post your boot phases + a path you found, e.g. `Documents/.../myfile` 🎉 |
| 0:45 | Wrap + take-home |

### If you get stuck
- Nothing here changes important files — we're organizing and *looking*, and you can undo anything.
- Re-read the **✅ You should now see** line. Screens differ by computer — compare with your breakout partner.
- Lost in the file manager? Click **Home** in the sidebar to get back to familiar ground.

### Optional challenge
Find your computer's exact **firmware version** (Mac: System Report → Hardware; Windows: System Information → BIOS) and whether it uses **UEFI**. Bring it to the chat — whose machine is newest?
