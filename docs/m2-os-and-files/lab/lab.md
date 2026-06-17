# Lab — M2: from power-on to any file, on purpose

**You'll need:** your own laptop. **Nothing to install. Nothing to break** — we're looking and organizing.
**Time:** ~30 minutes • **Work in your breakout pair** — your screens will differ, that's fine.

> Heads up: creating/moving folders is safe and undo-able, and we won't touch system files.
> If something looks different from the example, note it and keep going. (Recap in the [notes](../notes.md).)

### The chain you'll trace
Steps 1–3 follow your computer from the power button to the desktop:
```mermaid
flowchart LR
  P["Power on"] --> F["Firmware (BIOS / UEFI)"] --> B["Bootloader"] --> O["Operating system"] --> D["Desktop"]
```

---

## Step 1 — Name your operating system
- **Mac:** Apple menu  → **About This Mac** (says *macOS* + a version).
- **Windows:** **Start → Settings → System → About**. **Chromebook:** **ChromeOS**. **Linux:** names your distribution.

✅ **You should now see:** your OS name. Say it: *"The manager running my hardware is ___."*

## Step 2 — Watch your computer boot
Think through (or, if it's quick, actually do) a restart and watch the two phases:
- the **logo** right after pressing power = the **firmware** waking the hardware and finding the disk,
- the **spinner / progress** after it = the **operating system** loading.

✅ **You should now see / recall:** the boot in two phases — **firmware first, then the OS.** Say the chain to your partner: *power → firmware → bootloader → OS → desktop.*

## Step 3 — Find your firmware
- **Mac:** About This Mac → **System Report** → **Hardware** → look for **"System Firmware Version"**.
- **Windows:** Start → type **System Information** → look for **"BIOS Mode"** (it'll likely say **UEFI**).

✅ **You should now see:** a firmware version (Mac) or **BIOS Mode: UEFI** (Windows). That tiny program is what ran *first*, before your OS existed in memory.

## Step 4 — Open your file manager and go Home
- **Mac:** **Finder**. **Windows:** **File Explorer** (⊞ Win + E). **Linux/Chromebook:** **Files**.
Click **Home** in the sidebar.

✅ **You should now see:** your personal folders — **Documents, Downloads, Pictures, Desktop**. This is your *home folder*.

## Step 5 — Find your filesystem type
- **Mac:** open **Disk Utility** → click your disk → it shows **APFS**.
- **Windows:** right-click the **C:** drive → **Properties** → "File system" shows **NTFS**.

✅ **You should now see:** your filesystem format (**APFS**, **NTFS**, or **ext4**). You didn't choose it — the OS uses it to track where every file's bits live on the SSD.

## Step 6 — Build a tidy folder structure
1. Open **Documents**.
2. Make a folder **`Course-01`** (right-click → New Folder).
3. Inside it, make **`labs`** and **`notes`**.

✅ **You should now see:** `Documents` → `Course-01` → containing `labs` and `notes`. You just designed a small tree.

## Step 7 — Reveal and read the path
Turn on the path/address bar (**Mac:** View → Show Path Bar; **Windows/Linux:** the address bar at top). Look at the trail for your `labs` folder.

✅ **You should now see:** a trail like **Home › Documents › Course-01 › labs** — that's the **path**. Read it aloud and write it down: `Documents/Course-01/labs`.

## Step 8 — Use a path to find something on purpose
From **Home**, click step-by-step: **Documents → Course-01 → notes**, watching the path bar grow.

✅ **You should now see:** you arrive at `notes` by *following its path* — no hunting. A path is directions to a file. (And it's the exact same address you'll *type* in M3.)

---

## 🎉 Your win
You can trace your computer from power-on to desktop (firmware → bootloader → OS), and find any
file on purpose by reading its path. The box is a lot less mysterious now.

**Post it to the chat wins board:** *"My boot: firmware → OS; and I built `Documents/Course-01/labs` 🎉"*

## Take-home (optional)
Next time you turn your computer on, *watch the boot* and name each phase as it happens. Then tidy
your real **Downloads** folder into a couple of sensible folders — notice how structure makes things findable.
