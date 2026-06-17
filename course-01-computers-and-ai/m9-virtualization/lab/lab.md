# Lab — M9: measure a VM vs a container (in your Codespace)

**You'll need:** your **Codespace** (Docker is available). **Nothing to install.**
New to it? See **[How to open your Codespace](../../resources/install-guides/codespaces.md)**.
**Time:** ~25 minutes • **Work in your breakout pair.**

> Heads up: these commands only **measure and report** — nothing is changed. Real VMs are gigabytes
> and can't run inside a Codespace, so we observe a container directly and *compare* it to a VM.

The big idea: a **VM** is a whole fake computer with its **own operating system**; a **container**
**shares** the host's operating system. Let's prove how light that makes a container.

---

## Step 1 — How big is a container?
```text
$ docker pull alpine
$ docker images alpine
```

✅ **You should now see:** a `SIZE` of only a few **MB** (around 8–13 MB). A virtual machine doing the same job would be **gigabytes** — it has to carry an entire operating system inside it.

## Step 2 — How fast does it start?
```text
$ time docker run --rm alpine echo "hello from a container"
```

✅ **You should now see:** the message, and a `real` time **under a second**. A VM has to *boot* a full OS first, so it takes closer to a **minute**.

## Step 3 — Does a container have its own OS? (No.)
```text
$ uname -r                              # the host's kernel
$ docker run --rm alpine uname -r       # the container's kernel
```

✅ **You should now see:** the **same Linux kernel version** both times. The container didn't bring its own OS — it **borrowed the host's**. *That's* the whole reason it's tiny and instant. A VM, by contrast, would show its *own* separate kernel.

## Step 4 — Fill in the contrast
With your partner, complete the table from what you just observed (and the notes):

| | Virtual machine | Container |
|---|---|---|
| Own OS? | ? | ? |
| Size | ? | ? (you measured it) |
| Start time | ? | ? (you measured it) |
| Isolation | stronger | lighter |

✅ **You should now see:** VM = **own full OS, gigabytes, ~a minute, strong isolation**; container = **shares host OS, megabytes, ~a second, lighter isolation**.

## Step 5 — Connect it to the cloud
Recall M8: the cloud rents out slices of big servers. Now you know *how* — a **hypervisor** chops one
physical server into many isolated **VMs** to rent.

✅ **You should now see / say** to your partner: *"Virtualization lets one server become many rentable
computers — that's what made the cloud possible. Containers then made each app lighter to ship."*

---

## 🎉 Your win
You measured exactly how a container differs from a VM (megabytes vs gigabytes, a second vs a minute,
shared OS vs its own), and you can explain how virtualization powers both the cloud and containers.

**Post it to the chat wins board:** *"A container is ___ MB and starts in ___s — a VM would be gigabytes! 🎉"*

## Take-home (optional)
Look up the download size of a real OS install image (e.g. "Ubuntu Desktop ISO size" — several GB).
*That's* roughly what a VM carries that a container skips by sharing the host. Bring the number to the chat.
