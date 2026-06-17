# Dev container — the hosted Linux lab for M3–M6

This `.devcontainer/` gives every student **one identical Linux environment in the browser**
(via GitHub Codespaces), so the command-line-and-up modules don't depend on each learner's OS.

## What it provides
- **Ubuntu** base (`mcr.microsoft.com/devcontainers/base:ubuntu`) with a terminal.
- **Docker inside the Codespace** (docker-in-docker feature) → M6's `docker run` / `docker build` work.
- **The lab commands**, installed on create: `ping`, `dig`, `nslookup` (M5) and `cal` (M3 bonus).
  `ps`, `top`, `kill`, `id`, `curl`, and the M3 file commands are already in the base image.
- **Port 8080 forwarded** → M6's `docker run -p 8080:80 nginx` is reachable via the Codespace URL.

## Scope (intentional)
Used for **M3 (command line), M4 (inside the OS), M5 (networking), M6 (containers)**.
**Not** used for M1/M2 (those are about the student's *own* physical computer) or M7/M8
(browser AI tools). See `resources/install-guides/codespaces.md` for the learner-facing guide.

## How it was verified
- Pulled the base image and confirmed which commands are present vs missing.
- Confirmed `apt-get install -y iputils-ping bind9-dnsutils ncal` installs `ping`, `dig`,
  `nslookup`, `cal` (the `postCreateCommand`).

## ⚠️ Still to verify in a live Codespace (can't be tested locally)
- **`ping` may be restricted** inside the container (ICMP/capabilities). `dig`/`nslookup`/`curl`
  all work and carry M5's win even if `ping` is blocked — test it once in a real Codespace.
- The **docker-in-docker** flow and port 8080 forwarding (M6) — open a Codespace and run the M6 lab end-to-end.
- Free-tier compute limits for your cohort (and whether **GitHub Education** expands them).

## Requires
The repo must be on **GitHub** with Codespaces enabled. Lives at the repo root alongside
`mkdocs.yml` and `.github/` (current monorepo layout).
