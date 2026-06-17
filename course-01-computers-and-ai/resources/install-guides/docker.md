# Installing Docker

**Needed at Module 6 — not before.** Docker is the tool we use to run apps in containers.
You have two paths: install it (Option A), or skip installing and use a free browser version
(Option B). Either works for the lab.

---

## Option A — Install Docker on your computer
1. Go to the official install page: **https://docs.docker.com/get-started/get-docker/**
2. Download and install for your system:
   - **Mac / Windows:** **Docker Desktop** (follow the installer; you may need to restart).
   - **Linux:** **Docker Engine** (follow the Linux instructions on that page).
3. **Start Docker** — on Mac/Windows, open the **Docker Desktop** app and wait for it to say it's running (a whale icon in your menu bar / system tray).

### Check it works
In your terminal:

```text
docker --version
```
✅ **You should now see:** a version line, e.g. `Docker version 28.x, build …`.

```text
docker run hello-world
```
✅ **You should now see:** a message that starts **`Hello from Docker!`**. That means Docker is
installed and working — you're ready for M6.

### If it doesn't work
- **`command not found`** → Docker isn't installed, or your terminal was open before installing — close and reopen it.
- **`Cannot connect to the Docker daemon`** → Docker isn't *running*. Open Docker Desktop and wait for it to start.
- **Windows:** Docker Desktop may ask you to enable virtualization (WSL 2). Follow its prompt.
- Still stuck? Use Option B for class and sort the install out afterward.

---

## Option B — No install: use the browser playground
If you can't install Docker (locked-down or school laptop, or it's fighting you):

1. Go to **labs.play-with-docker.com**.
2. Sign in with a **free Docker Hub account**.
3. Click **Start**, then **+ ADD NEW INSTANCE** — you get a real Docker terminal in your browser.

Every command in the M6 lab works there. (Note: web sessions are temporary and time out — fine for the lab.)

---

> 💲 **For the instructor (paid-course note):** **Docker Desktop** is free for personal use,
> education, and small businesses, but **large organizations need a paid subscription**
> (see the licence terms on Docker's site). Learners installing it on their **own personal
> laptops** for this course are covered by personal use. Fully free alternatives if needed:
> **Docker Engine** on Linux, or the **Play with Docker** browser playground (Option B).
> *(Not legal advice — confirm Docker's current terms for your situation.)*
