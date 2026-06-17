# Capstone — tie the whole course together

> This is the finale. You'll take the ideas from all twelve modules and turn them into **one small
> thing you can run and explain**. It doesn't need to be big — it needs to *work*, and you need to be
> able to walk someone through how, in your own words.

You planned your track in the **[M12 lab, Part D](../lab/lab/)**. This page is the scaffold to actually
build it — including a tiny, ready-to-run **starter project** so you never face a blank page.

---

## Pick your track
| Track | What you deliver | Modules it pulls from |
|---|---|---|
| **A · AI in a box, in the cloud** | A small AI app in a **container**, tracked in **Git**, runnable in the **cloud**, with one **security** habit applied | M6, M7, M8, M10, M11, M12 |
| **B · Explain the modern stack** | A 5-minute live demo walking hardware → OS → CLI → network → Git/cloud → container → a running AI thing | M1–M12 |
| **C · My modern setup** | A tidy, documented setup that's **secured**, **version-controlled**, and cloud-connected | M2, M3, M6, M7, M8 |

**Every track must meet the same three requirements:**

- [ ] **It runs.** Someone else can start it and see it work.
- [ ] **It handles one failure gracefully** — a bad input or missing thing doesn't crash it; it says something helpful.
- [ ] **You can explain it** — how it works *and* how you'd secure it — in plain language.

---

## Track A — build it with the starter
A complete, dependency-free starter lives in **`capstone/starter/`**: a *tiny language model in a box.*
It mirrors exactly what M11–M12 taught — **learn from data, then predict the next word** — with no API
key and no heavy libraries, so it runs the same on your laptop, in a Codespace, or in a container.

**1. Open it in a Codespace** (M8/M10 — nothing to install): [▶ Open in Codespaces](https://codespaces.new/ThinkTechConsultingLLC/under-the-hood-course), then in the terminal:
```bash
cd docs/m12-ai-fundamentals-2/capstone/starter
python app.py            # generate text from the built-in data
python app.py computers  # start from a word you choose
```

**2. See the M11 lesson live — *data is everything*.** Edit `sample.txt`, add a few of your own
sentences, and run it again. The output changes because the **model learned from different data**.

**3. Run it as a container** (M10 — *runs the same everywhere*):
```bash
docker build -t my-capstone .
docker run --rm my-capstone
```

**4. Meet the "handle one failure" requirement.** Try a word the model never saw:
```bash
python app.py zzzzz
```
It won't crash — it tells you the word is unknown and recovers. Read `generate()` in `app.py` to see
how. (Want to go further? Make it handle an *empty* `sample.txt` with your own friendly message.)

**5. Track it in Git and push to GitHub** (M7): copy the `starter/` folder into your own new repo, then
```bash
git init && git add . && git commit -m "My capstone: a tiny language model in a box"
```
and push it to a repo on your GitHub account.

**6. Apply one security habit** (M6): add a short `README.md` that notes **what you would *not* commit**
(secrets, API keys, passwords) and why — and confirm none are in your repo.

??? note "Peek at the starter code (`app.py`) — only ~50 lines"
    ```python
    def train(text):
        """'Training': learn which words tend to follow which (a tiny next-word model)."""
        words = text.split()
        model = {}
        for current, nxt in zip(words, words[1:]):
            model.setdefault(current.lower(), []).append(nxt)
        return model

    def generate(model, seed, length=25):
        """'Inference': start from a seed word and predict the next word, again and again."""
        word = seed.lower()
        if word not in model:                      # graceful failure: unknown seed
            word = random.choice(list(model.keys()))
        output = [word]
        for _ in range(length - 1):
            choices = model.get(word)
            if not choices:                        # dead end — stop cleanly
                break
            word = random.choice(choices).lower()
            output.append(word)
        return " ".join(output)
    ```
    The full file (with comments) and a `Dockerfile`, `sample.txt`, and `requirements.txt` are in `capstone/starter/`.

---

## Track B — present the stack
Don't want to code? **Explain it instead** — that's a real skill. Use this 5-minute script, one line per
module, in your own words. Show something real on screen where you can (your specs, a terminal, a repo).

1. **The machine (M1)** — here are my computer's parts; this is why AI needs GPUs.
2. **OS, files & inside the OS (M2/M4)** — boot to desktop; processes the OS juggles right now.
3. **Command line (M3)** — one thing I can do faster by typing.
4. **Network & security (M5/M6)** — how a page reaches me, and one habit that keeps me safe.
5. **Git & cloud (M7/M8)** — my work, tracked and living on someone else's computer.
6. **VMs & containers (M9/M10)** — one computer pretending to be many; an app that runs anywhere.
7. **AI (M11/M12)** — a thing that learned from data and predicts what comes next — *and* one time I caught it being confidently wrong.

End with: *"That's the whole stack, from the box to the AI."*

---

## How you'll present (all tracks)
A short, friendly share in the final session:

- **~3 minutes:** show it running (or do your demo), then explain **one thing that surprised you**.
- **Answer two questions:** *"What happens if it fails?"* and *"How would you keep it secure?"*
- Post your win to the chat board: *"I shipped a capstone that ties the whole course together! 🎉"*

There's no grade. The bar is simple: **it runs, it fails gracefully, and you can explain it.** If you can
do that, you understand how computers and AI really work — which was the whole point. 👏
