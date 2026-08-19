# Lab M8: prove you're already in the cloud

**You'll need:** your **Codespace** terminal and a browser. **Nothing to install.**
New to it? See **[How to open your Codespace](../../resources/install-guides/codespaces.md)**.
**Time:** ~25 minutes • **Work in your breakout pair.**

> Heads up: these commands just *report facts* about the machine you're on nothing changes.
> The whole point today is realizing where you actually are.

--------------------------------------------------------------------------------

## Step 1: This terminal is not your laptop
```text
$ hostname
$ uname -srm
$ nproc
```

✅ **You should now see:** a **random hostname** (like `613cb477f82a`, not "MyLaptop"), a **Linux** system, and a core count. This is a *rented Linux machine*, handed to you on demand — your actual laptop might be a Mac or Windows with a different name.

**## Step 2: It's somewhere else (a data center)**
```text
$ curl -s https://api.ipify.org ; echo
```

✅ **You should now see:** a public **IP address** that is **not your home internet's** — it belongs to a Microsoft Azure data center (where Codespaces run). Your "terminal" is physically in a warehouse of servers, possibly on another continent.

## Step 3 — You reached it from anywhere
Think about how you got here: you opened this Codespace **in a browser**. You could close it, open the *same* Codespace on a different computer or your phone, and pick up exactly where you left off.

✅ **You should now see / realize:** the machine isn't tied to one device — that's **anywhere-access**, a core reason the cloud won.

## Step 4 — Map real services to the three flavors
With your partner, label each service **SaaS**, **PaaS**, or **IaaS** (hint: *who manages the machine?*):

| Service | You manage… | Flavor? |
|---|---|---|
| Gmail | nothing — just use it | ? |
| Your Codespace | your code; they run the machine | ? |
| Netflix | nothing — just watch | ? |
| Renting an empty server to set up yourself | everything | ? |
| GitHub Pages (this course's site) | your files; they host them | ? |

✅ **You should now see:** Gmail = **SaaS**, Netflix = **SaaS**, Codespace = **PaaS**, empty server = **IaaS**, GitHub Pages = **PaaS/hosting**. The pattern: the *less* you manage, the more it's SaaS.

## Step 5 — See a real cloud deploy
This course's notes are published to **GitHub Pages** — open the site (your instructor will share the link).

✅ **You should now see:** the exact `notes.md`/glossary files from the repo, served as a website **from the cloud**, reachable by anyone in the world. That's hosting-as-a-service in action — no server of your own required.

---

## 🎉 Your win
You proved your Codespace is a rented computer in a data center, you can tell IaaS/PaaS/SaaS apart
with real examples, and you can explain why the cloud took over — *and its trade-offs*.

**Post it to the chat wins board:** *"My 'cloud computer' is a ___-core Linux box in a data center, not my laptop! ☁️🎉"*

## Take-home (optional)
Next time you use an app, ask: *whose computer is this actually running on, and which flavor is it?*
You'll start seeing the cloud everywhere — because it's nearly everywhere.
