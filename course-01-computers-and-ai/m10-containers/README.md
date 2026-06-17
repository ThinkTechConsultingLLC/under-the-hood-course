# M10 — Containers

> "It works on my machine" is the oldest groan in software. Today you end it: you'll run a real app in
> a sealed box that runs the same anywhere, then build and ship your *own* box. You've seen the engine
> (M4's namespaces/cgroups) and the heavier VM (M9) — now you drive the thing that runs modern IT.
> <!-- HUMAN: review/replace this hook. The instructor's voice and relatability are the whole point. -->

**Today's win:** you run a real app in a container in one command, build your own image from a Dockerfile, and can explain why containers (light, portable) beat shipping a whole machine.

### Today you will
- Run "hello world" then a real **web app** in a container, each in one line *(Part 10a)*
- Write a tiny **Dockerfile**, build your **own image**, and run it *(Part 10b)*
- Explain **images vs containers**, and **containers vs VMs** (callback to M9), plus what **Kubernetes** is for

### Environment
We work in a **Codespace** — **Docker is built in**, nothing to install. New to it? See **[How to open your Codespace](../resources/install-guides/codespaces.md)**.

> 🗓️ **This module spans two sessions.** Open `lab/lab.md` — it's split into Part 10a (run apps) and Part 10b (build your own).

### Run of show
| Session | Time | What we do |
|---|------|------------|
| **1** | 0:00 | Hook + the "works on my machine" problem (recap in [`notes.md`](notes.md)) |
| **1** | 0:10 | **Lab 10a** — hello-world, then a real web app |
| **1** | 0:40 | **Show** — "I ran a web server in a box! 🎉" |
| **2** | 0:00 | Recap: images vs containers, vs VMs (M9) |
| **2** | 0:10 | **Lab 10b** — write a Dockerfile, build & run your own image |
| **2** | 0:40 | **Show** — "I shipped a box that runs anywhere! 📦" |

### If you get stuck
- Containers are throwaway — anything can be `docker rm`'d and remade. You can't make a lasting mess.
- Re-read the **✅ You should now see** line. A container that "exited" isn't broken — that's often normal.
- `docker ps` shows what's running; compare with your breakout partner.

### Optional challenge
Change your `index.html`, rebuild, and reload — watch your image update. Then look up "Kubernetes" in one
sentence: *why* would anyone need a tool to run hundreds of containers across many servers? Bring your answer to the chat.
