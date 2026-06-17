# Course 02 — AI Engineering: Build & Ship Real AI Apps

*A hands-on course that takes you from writing your first line of Python to building and shipping real AI-powered applications — chatbots, knowledge assistants (RAG), and agents.*

**Who it's for:** learners comfortable using a computer (Course 01 graduates or equivalent) who want to build AI apps. **No prior programming required — the course starts with Python from scratch.**
**Prerequisites:** Course 01 *or* basic computer fluency (command line, files, ran a program before). No coding experience needed.
**Format:** lab-first. Every session ends with something that runs. Notes are one page; the rest is building. (Same engine: Hook → Frame → Lab → Build → Show → Take-home.)

**By the end you can:** write Python, call an LLM from code, engineer prompts, build a retrieval system over your own data (RAG), build a tool-using agent, evaluate and add guardrails to an AI app, and deploy a working application.

> This course is the *applied* companion to the **AI Engineering Resource Map** — each AI module points to its deeper resources (HF Agents course, DeepLearning.AI short courses, the security labs and datasets) for students who want to go further.
>
> **Pacing:** the course now opens with a **Python foundation (M1–M3)** before the AI build modules. With Python first plus the 2-session RAG and Agents modules, this is roughly an **~11–15 week course** depending on slot length and how new your students are to programming. If your students are complete programming beginners, expand the Python block (split M1–M3 across more sessions, add an extra practice week). Re-pace freely.

---

## Part A — Python foundation
*Build the tool before you build with it. This isn't a full computer-science course — it's exactly the Python an AI engineer needs, taught lab-first.*

### M1 — Your first Python program
- **Win:** you write and run your own Python program.
- **Concepts:** what programming is, running Python, variables, types (text / numbers / true-false), input & output, comments.
- **Lab:** set up Python (or a browser notebook), then write a program that asks a question and responds — make it from their life (a tip calculator, a personalized greeting). They wrote real code on day one.

### M2 — Logic & data: decisions and collections
- **Win:** a small program that makes decisions and processes a list of things.
- **Concepts:** if / else, loops, lists, and **dictionaries** — the exact shape of JSON and API data, so this is direct prep for the AI half.
- **Lab:** build something that loops over data and decides (a simple grader, a budget categorizer); meet the dictionary — the structure every API speaks.

### M3 — Functions, files, libraries & errors
- **Win:** organized, reusable code that reads/writes data, uses outside libraries, and survives mistakes.
- **Concepts:** functions, imports, `pip` & libraries, virtual environments, reading/writing files, **JSON**, `try/except`. *(Light touch: you'll **use** objects/classes from libraries well before writing your own.)*
- **Lab:** refactor M2 into clean functions; install and use a library; read a file → transform it → save it as JSON; add error handling. **This is exactly the toolkit the LLM API needs in Part B.**

---

## Part B — Building with AI

### M4 — Ship your first AI app
- **Win:** a working AI chatbot running in front of you — and you understand the code, not just a starter.
- **Concepts:** what an LLM is from a *builder's* view, API keys, request → response.
- **Lab:** call an LLM from Python, build a tiny chatbot, give it a personality. *"I built an AI app — and I can read every line."*

### M5 — Prompt engineering
- **Win:** you can reliably get an LLM to do what you want.
- **Concepts:** system vs user prompts, few-shot, chain-of-thought, structured output, when prompting alone is enough.
- **Lab:** build a prompt-powered tool from their life/work (email rewriter, classifier, study-question generator); A/B different prompts and see the difference.

### M6 — Driving the model from code (the API, properly)
- **Win:** you use the LLM API fluently from real programs.
- **Concepts:** the messages API, parameters (temperature, max tokens), streaming, structured/JSON outputs, handling responses — building straight on M3's JSON and functions.
- **Lab:** write an app that calls the model and parses a **structured JSON** response into something useful (e.g., extract fields from messy text).

### M7 — RAG I: give the AI your own knowledge
- **Win:** an assistant that answers questions about *your* documents.
- **Concepts:** why models don't know your data, embeddings, vector search, chunking.
- **Lab:** build a Q&A app over a document they choose (their notes, a manual, a policy); ask it real questions.

### M8 — RAG II: make it good
- **Win:** you can tell whether your RAG app is actually *correct* — and improve it.
- **Concepts:** retrieval quality, chunk/size tradeoffs, reranking, evaluation (does the answer match the source?).
- **Lab:** measure and improve M7 — fix a bad retrieval, add reranking, run a simple eval set.

### M9 — Agents: tools, function calling & frameworks  *(plan for ~2 sessions)*
- **Win:** an AI that can *take actions*, not just talk.
- **Concepts:** ReAct loop, giving the LLM tools, function calling, multi-step tasks; a framework (LangGraph or CrewAI) and MCP.
- **Lab (9a):** build a tool-using agent (e.g., calculator + web search + a custom tool).
- **Lab (9b):** rebuild it in a framework as a small multi-step agent; add memory.

### M10 — Evaluation, guardrails & security
- **Win:** you can test your AI app and stop it from being tricked or misused.
- **Concepts:** evaluating LLM apps, prompt injection & excessive agency (OWASP LLM Top 10), guardrails.
- **Lab:** red-team your own app (try to break it), then add a guardrail layer and re-test. *(Deeper: the security labs & red-team tools in the Resource Map.)*

### M11 — Deployment & productionizing  +  Capstone
- **Win:** your app runs for real — not just on your laptop.
- **Concepts:** wrapping an app in an API (FastAPI), containers, cost/latency, basic monitoring.
- **Lab + Capstone:** wrap and deploy an app, then **design, build, and demo a complete AI application of your choice** (RAG or agent), running and shareable. Present it; everyone claps.

---

## Capstone (pick a track)
- **Knowledge assistant (RAG)** — a Q&A app over a real document set, evaluated and deployed.
- **Action agent** — a tool-using agent that completes a multi-step task, with guardrails.
- **Your idea** — anything LLM-powered that solves a real problem from their life or work.

Requirements: it runs, it handles a basic failure gracefully, and they can explain *how it works* and *how they'd secure it* — in their own Python.

---

## Repo layout (this course's own, separate repo)
```
course-02-ai-engineering/
├── README.md                       # this syllabus + link to the Pages site
├── START-HERE/                     # setup, accounts/keys, how to get help
├── m1-python-first-program/
├── m2-python-logic-and-data/
├── m3-python-functions-files-libraries/
├── m4-first-ai-app/
├── m5-prompting/
├── m6-api-in-code/
├── m7-rag-1/
├── m8-rag-2/
├── m9-agents/
├── m10-eval-guardrails-security/
├── m11-deployment-capstone/
├── starters/                       # ready-to-run starter projects per module
├── _templates/lesson/
└── resources/ (cheat-cards, links into the AI Engineering Resource Map)
```

*Each module folder = one-page `README.md` + `lab/` + `solution/` + `starters/` + `assets/`.*
