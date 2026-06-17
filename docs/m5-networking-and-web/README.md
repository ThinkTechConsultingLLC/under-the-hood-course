# M5 — Networking & the web

> You type a name, hit Enter, and a page from a computer on the other side of the planet appears
> in under a second. It feels like magic. Today we pull back the curtain and follow that journey
> step by step — the address lookup, the request, the padlock — and you'll do every step yourself.
> <!-- HUMAN: review/replace this hook. The instructor's voice and relatability are the whole point. -->

**Today's win:** you can trace exactly what happens when you open a website — name → IP (**DNS**), the **request → 200 response**, and what the **padlock (HTTPS)** actually means — and you can decode a real site's security certificate.

### Today you will
- Turn a website's **name** into its **address** with `dig` (that's DNS)
- **Fetch a page from the command line** and read the `200` response — over **HTTPS**
- **Decode the padlock**: inspect a site's TLS **certificate**, and see it's served by a **CDN**

### Environment
We work in a **Codespace** — a Linux terminal in your browser — plus a normal browser tab. New to it? See **[How to open your Codespace](../resources/install-guides/codespaces.md)**.

### Run of show (~50 min)
| Time | What we do |
|------|------------|
| 0:00 | Hook + the win we're chasing |
| 0:05 | The big ideas: internet vs web, DNS, request→response, HTTPS, CDNs (recap in [`notes.md`](notes.md)) |
| 0:10 | **Lab** — trace a website end-to-end (breakout pairs) |
| 0:40 | **Show** — post your site's IP + "it answered 200 OK over HTTPS! 🔒🎉" |
| 0:45 | Wrap + take-home |

### If you get stuck
- Every command just *asks the network a question* — nothing changes your computer.
- Re-read the **✅ You should now see** line. Your IP may differ from your partner's (big sites have many) — that's normal.
- If a command seems to hang, press **Ctrl-C** and try again.

### Optional challenge
Run the trace on a site you use daily. Open its **Network tab** (browser dev tools) and reload — how many separate requests does *one* page make? Some sites make hundreds (that's the CDN at work). Bring the number.
