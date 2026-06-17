# M9 — Virtualization & VMs

> How does one server in a data center turn into 50 rentable cloud computers? And what's *really*
> underneath the containers you'll build next module? Same answer: **virtualization** — making one
> computer act like many. Today you'll see the layer that quietly powers both the cloud and containers.

**Today's win:** you can explain what a virtual machine is, what a hypervisor does, how virtualization made the cloud possible, and — concretely — how a container differs from a VM.

### Today you will
- Explain **virtualization**, **VMs**, and the **hypervisor** that runs them
- See *why* virtualization made the **cloud** (M8) possible
- Measure the **VM-vs-container** contrast with a real container's tiny footprint

### Environment
Your **Codespace** (with Docker). New to it? See **[How to open your Codespace](../resources/install-guides/codespaces.md)**.
> Note: we **observe** containers directly; real VMs are gigabytes and can't spin up inside a Codespace, so we reason about the VM side by comparison.

### Run of show (~50 min)
| Time | What we do |
|------|------------|
| 0:00 | Hook + the win we're chasing |
| 0:05 | The big ideas: virtualization, VMs + hypervisor, VMs vs containers (recap in [`notes.md`](notes.md)) |
| 0:10 | **Lab** — measure a container's footprint + compare to a VM (breakout pairs) |
| 0:40 | **Show** — post "A container is ___ MB and starts in ___s — a VM would be gigabytes! 🎉" |
| 0:45 | Wrap + take-home |

### If you get stuck
- The commands only *measure and report* — nothing is installed or changed.
- Re-read the **✅ You should now see** line; sizes/times differ slightly per machine — compare with your partner.
- Fuzzy on VM vs container? Re-read the notes' comparison table — it's the heart of this module.

### Optional challenge
A container shares the host's OS; a VM carries its own. So: could you run a *Windows* container on a
*Linux* host? Why or why not? (Hint: what does a container borrow from the host?) Discuss in the chat.
