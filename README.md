# Under the Hood — How Computers & AI Really Work

**A hands-on, beginner-friendly course by Tin Tech Consulting.** Start from "what *is* a computer?"
and finish able to explain — and operate — the whole modern stack: the machine, the operating system,
the command line, networking, security, Git, the cloud, virtualization, containers, and AI.

> 📖 **Read the course (free, open, no sign-in):**
> **https://thinktechconsultingllc.github.io/under-the-hood-course/**

- **Who it's for:** complete beginners. No computer-science background, no coding, no prerequisites — just a laptop and curiosity.
- **How it's taught:** *lab-first.* Every session ends with a real **win**. Notes are readable; the rest is doing.
- **What you'll be able to do:** read your own machine's specs, work the command line, understand processes/files/networking/security, use Git and the cloud, run and build a container, and explain in plain English how AI and LLMs actually work — with a project to prove it.

---

## 🆕 New to GitHub? Read this first (60 seconds)
You do **not** need to understand GitHub to take this course.
1. **To read the lessons:** just open the course link above. That's it — no account, nothing to install.
2. **To do the hands-on labs:** you'll need a **free GitHub account** (sign up at [github.com/signup](https://github.com/signup)) so you can open a **Codespace** — a ready-made computer that runs *in your browser*. One click, nothing to install. (More below.)
3. That's the whole of GitHub you need. Everything else, the course teaches you.

---

## 📚 The course — full breakdown (12 modules)

### Part A — The machine
| # | Module | What you'll be able to do |
|---|--------|---------------------------|
| **M1** | What a computer really is | Read your own specs (cores, RAM, SSD, GPU) and explain *why AI needs GPUs* |
| **M2** | The OS, booting & the filesystem | Trace power-on → desktop, and find any file on purpose |
| **M3** | The command line | Move around and get things done by typing — and chain commands together |
| **M4** | Inside the OS | See and control running programs; meet the trick behind containers |

### Part B — Connected, and how people really work
| # | Module | What you'll be able to do |
|---|--------|---------------------------|
| **M5** | Networking & the web | Trace a website end-to-end: DNS → request → the padlock (HTTPS) |
| **M6** | Security & privacy | Build a simple threat model and the habits that stop most attacks |
| **M7** | Version control: Git & GitHub | Track every change, branch safely, and push your work to GitHub |
| **M8** | The Cloud | Understand what "the cloud" really is, and why everything runs there |

### Part C — Packaging & running software anywhere
| # | Module | What you'll be able to do |
|---|--------|---------------------------|
| **M9** | Virtualization & VMs | Understand how one computer pretends to be many |
| **M10** | Containers | Run a real app in a container — and build and ship your own |

### Part D — AI
| # | Module | What you'll be able to do |
|---|--------|---------------------------|
| **M11** | AI Fundamentals I | Explain AI vs ML vs deep learning vs LLMs — and watch a model learn |
| **M12** | AI Fundamentals II + Capstone | Understand why LLMs are brilliant *and* why they make things up — then tie it all together |

Each module has an **Overview** (the plan), **Notes** (the in-depth read), and a **Lab** (the hands-on).

---

## 🧪 The labs — how to open them (the important part)
Labs are where the learning happens. Where each one runs:

- **M1–M2** → on **your own computer** (you explore *your* machine — nothing to set up).
- **M3–M10** → in a **Codespace**: a free Linux computer **in your browser**, with everything pre-installed.
- **M11–M12** → free **browser AI tools** (no setup).

### ▶️ Opening a Codespace (M3–M10) — for total beginners
1. Make a free GitHub account (if you haven't): [github.com/signup](https://github.com/signup).
2. Click this button → **[Open in Codespaces](https://codespaces.new/ThinkTechConsultingLLC/under-the-hood-course)** *(or: on this repo, the green **`< > Code`** button → **Codespaces** → **Create codespace**).*
3. Wait about a minute. You'll get a code editor with a **Terminal** at the bottom — that terminal is your Linux computer. Follow the lab there.

Nothing to install, works on any laptop (even a Chromebook). Codespaces include a generous free monthly allowance.

---

## 💡 Who it's for / use cases
- **Career-changers & "non-technical" professionals** who want to genuinely understand the tools they use — and talk to engineers with confidence.
- **Aspiring developers / IT / data / AI** building the foundation *before* a bootcamp or a coding course (it's the perfect on-ramp to our **Course 02 — AI Engineering**).
- **Founders, PMs, analysts, and the curious** who keep hearing "the cloud," "containers," "LLMs" and want the real picture, not buzzwords.
- **Students & self-learners** who learn best by *doing* — every module ends with something that works.

By the end you can build a small **capstone** — e.g. an AI model running in a container, in the cloud, tracked in Git — and explain every layer in your own words.

---

## 🛠 Setup / installation summary
You need almost nothing. Per stage:

| Stage | What you need | Install? |
|---|---|---|
| Reading the course | a web browser | none |
| M1–M2 labs | your own laptop | none |
| M3–M10 labs | a free GitHub account → **Codespaces** (browser) | none |
| M11–M12 labs | a web browser | none |

Detailed setup help (terminal, Docker, Codespaces) lives in the course's **Resources → Install guides** — and you only ever need it when a module says so.

---

## 🗺 Repository layout
```
docs/                    ← the whole course (this is the site content)
  ├─ index.md            ← website home
  ├─ START-HERE/         ← orientation: what you need and how sessions work
  ├─ how-to-use-this-site.md
  ├─ SYLLABUS.md         ← the detailed syllabus
  ├─ m1-…  …  m12-…      ← the 12 modules (each: README = overview, notes.md, lab/)
  └─ resources/          ← glossary, cheat-cards, install guides
README.md                ← this page (the repo's front door)
mkdocs.yml               ← builds the website
.devcontainer/           ← defines the Codespaces lab environment
.github/workflows/       ← auto-publishes the site on every change
```

---

## 🏢 About
Built and maintained by **Tin Tech Consulting**. Interested in guided cohorts, or our follow-on
**Course 02 — AI Engineering**? Get in touch.

© Tin Tech Consulting. Course content is original. *(Third-party source materials are not redistributed.)*
