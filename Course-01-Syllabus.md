# Course 01 — Under the Hood: How Computers & AI Really Work

*A hands-on course for adult beginners. Understand how computers, operating systems, and containers actually work — and how modern AI works underneath — by running and building things yourself.*

**Who it's for:** adults (late-20s+) with little or no computer background. Curiosity required; experience not.
**Prerequisites:** none — just a laptop and a willingness to break things.
**Format:** lab-first. One "win" every session. Notes are one page; the rest is doing. (See the lesson engine: Hook → Frame → Lab → Build → Show → Take-home.)

**By the end you can:** explain how a computer and its OS work, move confidently around the command line, understand processes/files/networking, run and build a container, and explain in plain English how AI and LLMs actually work — with a small project to prove it.

> **Pacing:** 8 core modules below. Treat each as ~1 session; **Containers (M6)** and **AI Fundamentals** often want 2 sessions each, so this is comfortably an 8–11 week course depending on your slot length. Re-pace freely.

---

## Module map

### M1 — What is a computer, really?
- **Win:** Demystify the box — you can name what each part does and how a computer turns input into output.
- **Concepts:** hardware vs software, CPU/RAM/storage, bits & bytes, "input → process → output."
- **Lab:** Explore *your own* machine's specs; match each part to its job; a quick "build-a-PC" picking exercise. First glimpse of the magic: it's just electricity and logic.

### M2 — The Operating System & the filesystem
- **Win:** You understand what the OS is *for* and can find anything on your computer on purpose.
- **Concepts:** what an OS does (manages hardware, programs, files, users), files/folders, paths.
- **Lab:** Navigate the filesystem in the GUI, then peek underneath; create a tidy folder structure; learn what a "path" really is.

### M3 — Talking to the computer directly: the command line
- **Win:** The "scary black screen" becomes your friend — you can move around and make things happen by typing.
- **Concepts:** terminal/shell, commands, arguments.
- **Lab:** Guided CLI tour — move between folders, create/rename/move files, run a program. Same actions as M2, now by command.

### M4 — Inside the OS: what's really happening
- **Win:** You can see and control what your computer is doing right now.
- **Concepts:** processes, memory, multiple users, permissions (and why they protect you).
- **Lab:** Open the task/process viewer; spot what's running and what's eating memory; safely start/stop a process; read a file's permissions.

### M5 — How computers talk: networking & the web
- **Win:** You understand what *actually* happens when you open a website.
- **Concepts:** internet vs web, IP & DNS, client/server, requests & responses.
- **Lab:** Trace a website end-to-end — look up a domain, ping it, fetch a page from the command line, watch the request happen in the browser tools.

### M6 — Packaging software: enter containers  *(plan for ~2 sessions)*
- **Win:** You can run a real app in a container — and you understand the "but it works on *my* machine" problem it solves.
- **Concepts:** isolation & portability, images vs containers, why containers matter (callback: it's an OS trick from M4).
- **Lab (6a):** Install Docker (or use a browser playground); run "hello world"; run a real app (e.g., a small web app) in one command.
- **Lab (6b):** Write a tiny `Dockerfile`, build your own image, run it. You shipped a box that runs anywhere.

### M7 — AI Fundamentals I: what AI actually is
- **Win:** You can clearly explain AI vs machine learning vs deep learning vs LLMs — and you've *watched* a model learn.
- **Concepts:** learning from data, training vs inference, neural nets at an intuitive level.
- **Lab:** Train a tiny model in the browser (e.g., an image or sound classifier) — give it examples, watch it get smarter, test it live. Learning becomes something they *saw happen*.

### M8 — AI Fundamentals II: how LLMs work  +  Capstone
- **Win:** You understand why LLMs are brilliant *and* why they make things up — and you tie the whole course together.
- **Concepts:** tokens & next-word prediction, why prompts matter, hallucination & limits, data → model → output.
- **Lab + Capstone:** Probe an LLM (see tokens, push its limits), then a "show what you learned" project — e.g., **run a small AI model/app inside a container on your own machine**, or a short demo explaining a working computer-to-AI stack you built. Present it; everyone claps.

---

## Capstone options (pick one)
- **"AI in a box"** — a small AI app or trained model running locally, ideally containerized (M6 + M7/M8).
- **"Explain the stack"** — a 5-minute live demo walking from hardware → OS → command line → container → a running AI thing.
- **"My machine, mastered"** — a personal setup project: organized system, a useful container running, documented in their own words.

---

## Repo layout (this course's own repo)
```
course-01-computers-and-ai/
├── README.md                  # this syllabus + link to the Pages site
├── START-HERE/
├── m1-what-is-a-computer/
├── m2-os-and-files/
├── m3-command-line/
├── m4-inside-the-os/
├── m5-networking-and-web/
├── m6-containers/
├── m7-ai-fundamentals-1/
├── m8-ai-fundamentals-2/
├── _templates/lesson/
└── resources/ (glossary, cheat-cards, install-guides)
```

*Each module folder = one-page `README.md` + `lab/` + `solution/` + `assets/`.*
