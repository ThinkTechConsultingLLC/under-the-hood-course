# Course 01 — How Computers & AI Really Work (Modern Foundations)

> **This is the canonical syllabus.** It supersedes the original beginner-lite brief
> (`Course-01-Syllabus.md`). Same friendly on-ramp — **raised depth and a modern lens.**

*A hands-on, live-online course that takes a complete beginner all the way to genuinely
understanding how computers, the internet, security, the cloud, containers, and AI work —
the way IT actually works today.*

**Who it's for:** adults with little or no background who want **real depth**, not a tour.
**Prerequisites:** none. We start from "what is a computer" and go deep, one solid step at a time.
**Format:** lab-first. A **win every session**. Errors are normalized; nobody's behind.

## What changed (and what didn't)
- **Unchanged:** beginner-accessible, no prerequisites, lab-first, a win per session, warm + safe.
- **Deeper:** we no longer stop at the surface — each topic goes to real, usable understanding.
- **Modern:** the framing reflects today's IT — cloud, containers, HTTPS, Git, GPUs, LLMs.
- **Notes are now fuller**, multi-section in-depth reads (still plain-language) — not one-pagers.
  Long references (commands, etc.) live in **`resources/cheat-cards/`**.

---

## Module map (12 modules)

### Part A — The machine
**M1 · What a computer really is**
- **Win:** name what each part does *and* explain how modern hardware shapes what's possible — including why AI needs GPUs.
- **Concepts:** hardware vs software; CPU (cores, clock speed); RAM; storage (HDD vs **SSD**); bits & bytes; input → process → output; **GPUs & parallelism**; the spectrum from phone to data center.
- **Lab:** explore your own machine's specs; map parts to jobs; see cores/threads; understand what a GPU is and why AI/graphics need one. *(Own machine.)*

**M2 · The OS & the filesystem**
- **Win:** understand what the OS does, how it *boots*, and find anything on purpose.
- **Concepts:** what an OS manages; files/folders/paths; **firmware (BIOS/UEFI)**; the **boot sequence** (power → firmware → bootloader → OS); filesystems at intuition; users.
- **Lab:** navigate the filesystem (GUI + path bar); build a tidy structure; trace what happens between power-on and desktop. *(Own machine.)*

**M3 · The command line**
- **Win:** make things happen by typing; real comfort in the terminal.
- **Concepts:** terminal/shell, commands/arguments/options, navigation, file ops; **pipes & redirection** (combining commands); a proper **commands cheat-card**.
- **Lab:** guided CLI tour — move, create, rename, delete, run programs, chain commands. *(Codespaces.)*

**M4 · Inside the OS**
- **Win:** see and control what your computer is doing right now.
- **Concepts:** processes & PIDs; multitasking/scheduling; memory; users; **permissions (rwx)**; the OS as resource manager; a **namespaces/cgroups teaser** (the trick behind containers).
- **Lab:** process viewer + `ps`/`top`/`kill`; read permissions; safely start/stop a process. *(Codespaces.)*

### Part B — Connected, and how people actually work
**M5 · Networking & the web**
- **Win:** understand exactly what happens when you open a website — including the modern parts.
- **Concepts:** internet vs web; IP; **DNS**; client/server; request/response; **HTTPS/TLS** (and why the padlock matters); **CDNs & the cloud**; ports.
- **Lab:** trace a site end-to-end — `dig`/`nslookup`, `ping`, `curl`, browser dev tools; inspect a certificate. *(Codespaces.)*

**M6 · Security & privacy** 🆕
- **Win:** understand how systems are protected, and protect yourself — with a basic threat model.
- **Concepts:** authentication (**passwords, 2FA, password managers**); **encryption** at rest & in transit (HTTPS revisited); **phishing & social engineering**; least-privilege (callback to M4 permissions); updates/patching; privacy basics; an OWASP-lite "how things get hacked."
- **Lab:** audit your own posture; inspect a real TLS certificate; dissect a phishing email; reason about least-privilege. *(Own machine + Codespaces.)*

**M7 · Version control: Git & GitHub** 🆕
- **Win:** track every change to your work and collaborate — and understand why *all* modern software runs on Git.
- **Concepts:** what version control is and why; commits & history; branches (intuition); local vs remote; **GitHub** as the cloud home; the clone → commit → push → pull loop.
- **Lab:** create a repo, make commits, view history, push to GitHub, make a branch and a change. *(Codespaces — Git pre-installed.)*

**M8 · The Cloud** 🆕
- **Win:** understand what "the cloud" actually is and why nearly everything runs there now.
- **Concepts:** the cloud = **renting computers on demand**; IaaS/PaaS/SaaS at intuition; why cloud (scale, cost, anywhere-access); data centers; **the cloud you're already using** (Codespaces, GitHub, web apps); regions & latency.
- **Lab:** make it concrete — your Codespace *is* a cloud computer; observe a cloud resource; map everyday services to what they really are. *(Codespaces / browser.)*

### Part C — Packaging & running software anywhere
**M9 · Virtualization & VMs** 🆕
- **Win:** understand how one computer pretends to be many — the layer beneath the cloud and containers.
- **Concepts:** virtualization; **hypervisors**; guest vs host OS; VMs vs physical machines; how virtualization made the cloud possible; **VMs vs containers** (teaser → M10).
- **Lab:** observe a VM and its resource cost; compare against a container. *(Codespaces / browser; real VMs are heavy — observation-first.)*

**M10 · Containers**
- **Win:** run a real app in a container, build your own image, and understand why containers run modern IT.
- **Concepts:** isolation & portability; images vs containers; **Dockerfiles**; registries; VMs vs containers (callback M9); an **orchestration/Kubernetes** intuition; the modern unit of deployment.
- **Lab:** hello-world → run nginx → build & run your own image. *(Codespaces — Docker-in-Docker.)*

### Part D — AI
**M11 · AI Fundamentals I**
- **Win:** explain AI vs ML vs deep learning vs LLMs — and watch a model learn — with real understanding.
- **Concepts:** learning from data; training vs inference; neural networks; **what made the current AI wave** (data + compute + scale, transformers at intuition); GPUs (callback M1); bias & data quality.
- **Lab:** train a model in the browser (give examples, watch it learn, test live), then probe its limits. *(Browser. Depth pending provided resources.)*

**M12 · AI Fundamentals II + Capstone**
- **Win:** understand LLMs deeply — *and* why they make things up — then tie the whole modern stack together.
- **Concepts:** tokens & next-token prediction; prompts; **hallucination & limits**; context windows; training cutoff; responsible use & ethics; the **data → model → output** pipeline mapped across the whole course.
- **Lab + Capstone:** probe an LLM, then **build and present a project that spans the modern stack.** *(Browser + earlier tools.)*

---

## Capstone (pick a track)
- **AI in a box, in the cloud** — a trained model or small AI app, in a **container**, runnable in the **cloud**, tracked in a **Git** repo.
- **Explain the modern stack** — a live demo from hardware → OS → command line → network → security → Git → cloud → container → a running AI thing.
- **My modern setup** — a documented personal setup that's organized, **secured**, **version-controlled**, and cloud-connected.

*Requirements: it runs, it handles a failure gracefully, and you can explain how it works — and how you'd secure it — in your own words.*

---

## Pedagogy & conventions
- **Fuller in-depth notes:** each module's `notes.md` is a richer, multi-section read in plain language — depth in the main flow, with a **"Go deeper"** box for the truly optional.
- **Cheat-cards:** `resources/cheat-cards/` holds reference material (commands, Git, etc.) so notes stay readable.
- **Lab environment (the modern, no-setup default):**
  - **M1, M2** → the student's **own machine** (the lesson *is* their real computer).
  - **M3–M10** → **GitHub Codespaces** — one identical Linux environment in the browser (terminal + Docker), so labs don't depend on each learner's OS.
  - **M11, M12** → **browser** AI tools.
- **Site:** published with **MkDocs Material** on **GitHub Pages**.
- **Boundary with Course 02:** Course 01 = *modern foundations* (how IT works today). **Building** AI apps — agents, RAG, deployment — stays in Course 02. Flag anything that straddles.

**Pacing:** 12 modules; several (M6 Security, M10 Containers, M11/M12 AI) often want two sessions, so this runs comfortably as a **~14–18 week** course. Re-pace freely.

---

## Build status & rework plan
Built against the *old* beginner-lite brief (now to be reworked to this level):

| New | Old | Status |
|---|---|---|
| M1–M4 | M1–M4 | exist — **deepen + modernize** |
| M5 Networking | M5 | exists — deepen (+DNS/HTTPS/CDN) |
| **M6 Security** | — | **new** |
| **M7 Git & GitHub** | — | **new** |
| **M8 The Cloud** | — | **new** |
| **M9 Virtualization** | — | **new** |
| M10 Containers | old M6 | exists — deepen, renumber |
| M11 AI I | old M7 | exists — deepen, renumber |
| M12 AI II + Capstone | old M8 | exists — deepen, renumber |

Rework runs **one module per run**, against this syllabus. Folder renames/renumbering + site-nav
updates happen as part of the rework. AI deepening (M11/M12) waits on the resources being provided.
