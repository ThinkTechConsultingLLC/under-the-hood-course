# Using a Codespace (a Linux computer in your browser)

**For Modules 3–6, your class may use a *Codespace* instead of your own laptop's terminal.**
A Codespace is a real Linux computer that runs **in your browser** — everything is already set
up, nothing to install, and it's the *same* for everyone, so the steps just work.

> Why: M3–M6 use a terminal, and Mac/Windows/Linux each behave a little differently. A Codespace
> gives the whole class one identical Linux machine, so we can focus on learning, not on setup.
> *(Modules 1–2 use your **own** computer on purpose, and Modules 7–8 use websites — no Codespace needed there.)*

## Open your Codespace
1. Go to the course's **GitHub repository** (your instructor will share the link).
2. Click the green **`< > Code`** button → the **Codespaces** tab → **Create codespace on main**.
3. Wait a minute while it sets up.

✅ **You should now see:** a code-editor page in your browser with a **Terminal** panel at the
bottom showing a prompt (a `$`). That terminal *is* your Linux computer — start the lab there.

## What's already installed for you
- The terminal and all the M3/M4 commands (`pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, `ps`, `top`, …).
- The M5 networking tools (`curl`, `dig`, `nslookup`, `ping`).
- **Docker** for M6 — `docker run` and `docker build` work right inside the Codespace.

## For Module 6 (web apps)
When you run `docker run -p 8080:80 nginx`, the Codespace will pop up a notification to **open
port 8080** in your browser — click it to see the running web page (instead of `localhost:8080`).

## Good to know
- You need a **free GitHub account** and to be signed in. Codespaces has a **free monthly
  allowance** for individuals (your instructor will confirm what your class uses).
- A Codespace is a **fresh Linux box**, not your own computer — that's the point for these modules.
- If `ping` doesn't respond in the Codespace, don't worry: `dig`/`nslookup` and `curl` still show
  the full website trace in M5. Tell your instructor and keep going.
