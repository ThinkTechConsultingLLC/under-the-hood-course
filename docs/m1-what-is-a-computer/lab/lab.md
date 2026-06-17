# Lab — M1: read your own computer's specs

**You'll need:** your own laptop and a web browser. **Nothing to install. Nothing to break** — we're only *looking*.
**Time:** ~30 minutes • **Work in your breakout pair** — compare what each of you finds.

> Heads up: every step here is *looking*, not changing. There's no way to break your computer.
> If a screen looks different from the example, that's fine — note it and keep going.

First, two words for the whole day:
- **Hardware** — the physical parts (the chips, screen, keyboard).
- **Software** — the instructions running on them (apps, the system, this page).

A computer is hardware running software — and today we meet the hardware. (One-page recap in the [notes](../notes.md).)

---

## Step 1 — Open your "About" / specs screen
- **Mac:** Apple menu  → **About This Mac**.
- **Windows:** **Start → Settings → System → About** (keep it open; we'll also use **Task Manager → Performance**, press Ctrl+Shift+Esc).
- **Chromebook:** Settings ⚙️ → **About ChromeOS**. **Linux:** Settings → **About**.

✅ **You should now see:** a panel listing your computer's details — a chip/processor name, a memory amount, and more. These are your **specs**.

## Step 2 — Find your CPU: name, speed, and cores
Find the **Processor / Chip / CPU**. Note three things if you can:
- its **name** (e.g. *Apple M2*, *Intel Core i7*, *AMD Ryzen 5*),
- its **clock speed** in **GHz** (e.g. 2.4 GHz),
- its **cores** (Windows: Task Manager → Performance → CPU shows "Cores" and "Logical processors"; Mac: the chip name's core count, or it's an Apple chip with listed cores).

✅ **You should now see:** a processor name, and ideally a GHz number and a core count (e.g. "8 cores"). **Write them down.** That's your worker — the more cores and GHz, the more it can do at once.

## Step 3 — Find your memory (RAM)
Look for **Memory** or **RAM** — a number in **GB** (e.g. 8 GB, 16 GB).

✅ **You should now see:** a memory size in GB. **Write it down.** That's your *right-now* working space — it forgets everything when the power's off.

## Step 4 — Find your storage, and whether it's an SSD
Find **Storage** (Mac: the **Storage** tab; Windows: Settings → System → Storage, or Task Manager → Performance → Disk, which often shows the type). Note the **size** (GB/TB) **and the type** — **SSD** (fast, modern) or **HDD** (older, spinning).

✅ **You should now see:** a storage size *and* its type. **Write both down.** Storage keeps your files forever — and an SSD is why modern machines feel instant.

## Step 5 — Find your graphics (GPU)
Find **Graphics / GPU** (Mac: About This Mac lists it; Windows: Task Manager → Performance → GPU, or Settings → Display → Advanced display).

✅ **You should now see:** a graphics chip name (e.g. *Intel UHD Graphics*, *AMD Radeon*, *NVIDIA GeForce*, or *Apple M-series GPU*). Some computers list **two** (a built-in one and a separate powerful one). **Write it down** — this is the part that draws your screen *and* is the same kind of chip that trains AI.

## Step 6 — Match each part to its job
Fill this in for *your* machine and read your row to your partner:

| Part | Your value | Its job |
|------|-----------|---------|
| **CPU** | name, ___ GHz, ___ cores | Does the work — every task runs through it |
| **RAM** | ___ GB | Holds what you're doing *right now* (forgets when off) |
| **Storage** | ___ GB/TB, SSD/HDD | Keeps files forever (remembers when off) |
| **GPU** | name | Draws the screen — and does the parallel math AI needs |

✅ **You should now see:** all four rows filled in. You can now read a spec sheet.

## Step 7 — The GPU insight: why AI loves it
A CPU has a *few powerful* cores; a GPU has *thousands of tiny* ones. AI training is "do the same simple math across millions of numbers" — exactly what thousands of tiny cores do best, all at once (**parallelism**).

✅ **You should now see / say** to your partner: *"A GPU does lots of the same small math at once — that's why AI runs on GPUs, not just CPUs."*

## Step 8 — Build a computer for a purpose (on paper)
With your partner, pick parts for **one** of these people. There's no single right answer — but defend your build:
- **A student** (writing, web, lots of photos) — what matters most?
- **A gamer / video editor** — what changes?
- **Someone training AI models** — what's now essential?

Choose: more **cores** or higher **GHz**? How much **RAM**? **SSD** size? A basic or a **powerful GPU**?

✅ **You should now see:** three or four parts chosen for your person, with a one-sentence "why" (e.g. *"The AI build needs a powerful GPU and lots of RAM"*). A sample is in `../solution/`.

---

## 🎉 Your win
You can read your own computer's specs — cores, GHz, RAM, SSD, GPU — say what each does, and explain why AI runs on GPUs. You can read *any* device now.

**Post it to the chat wins board:** *"My machine: ___-core CPU, ___ GB RAM, ___ GB SSD, ___ GPU 🎉"*

## Take-home (optional)
Find the specs of your **phone** (search "[your phone] specs"). It has a CPU, RAM, storage, and a GPU too — the same parts as your laptop, just smaller. Notice it even has cores and a GPU.
