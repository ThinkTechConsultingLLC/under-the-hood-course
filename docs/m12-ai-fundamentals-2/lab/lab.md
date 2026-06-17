# Lab — M12: probe an LLM, then plan your capstone

**You'll need:** a web browser, a chatbot (e.g. **claude.ai** — any works), and a **token-visualizer**
tool (your instructor will share the link). **Nothing to install.**
**Time:** ~30 min for Parts A–C, then Part D plans the capstone • **Work in your breakout pair.**

> Heads up: you can't hurt anything by chatting. Today's goal includes deliberately *catching the AI
> being wrong* — that's a win, not a problem.

---

# Part A — See the tokens

## Step 1 — Break a sentence into tokens
Open the token-visualizer and paste a sentence, e.g. *"Computers are surprisingly dumb."*

✅ **You should now see:** your sentence split into coloured **tokens** with a count. Notice tokens aren't always whole words — spaces and word-pieces count too.

## Step 2 — Try to confuse it
Paste a long or made-up word, like `antidisestablishmentarianism`.

✅ **You should now see:** that one "word" break into **several tokens**. Proof: an LLM reads **chunks**, not words, and predicts them one at a time.

---

# Part B — Prompts steer everything

## Step 3 — Give a lazy prompt
Open your chatbot and type something vague: `write about dogs`.

✅ **You should now see:** a generic, forgettable answer — a vague request continued vaguely.

## Step 4 — Give a rich prompt
In a new chat, give a role, audience, length, and goal, e.g.:
`You are a vet. In 4 friendly bullet points, tell a first-time owner how to settle a new puppy on night one.`

✅ **You should now see:** a sharply better, tailored answer — *same model, just a better setup*. That difference is prompt engineering (Course 02 goes deep).

---

# Part C — Catch a hallucination

## Step 5 — Ask for something it can't really know
Ask for specific, checkable detail on something obscure or invented, e.g.:
`Give me three published studies (with authors and years) about [a very niche or made-up topic].`

✅ **You should now see:** a confident, tidy answer — often with **citations that look real**.

## Step 6 — Verify one claim
Pick one "fact" or source it gave and try to confirm it (search for the paper/quote).

✅ **You should now see:** at least one claim that is **wrong or doesn't exist**. That's a **hallucination**:
the model produced *plausible* text, not *true* text. Say the takeaway with your partner: **brilliant and
confident ≠ correct — always verify** (and never paste secrets into it).

---

# Part D — Plan your capstone (the finale)

## Step 7 — Pick a track and sketch it
Choose one and write a short plan (3–4 sentences): what it does, and which modules it pulls from.
- **AI in a box, in the cloud** — a trained model or small AI app, in a **container** (M10), runnable in the **cloud** (M8), tracked in **Git** (M7), with one **security** habit applied (M6).
- **Explain the modern stack** — a 5-minute live demo from hardware (M1) → OS (M2/M4) → command line (M3) → network & security (M5/M6) → Git & cloud (M7/M8) → VM & container (M9/M10) → a running AI thing (M11/M12).
- **My modern setup** — a tidy, documented setup that's **secured** (M6), **version-controlled** (M7), and cloud-connected.

✅ **You should now see:** a one-paragraph plan naming your track and the modules it builds on.
**Requirements for the finished capstone:** it *runs*, it *handles one failure gracefully*, and *you can
explain how it works — and how you'd secure it — in your own words.*

---

## 🎉 Your win
You've seen the one trick behind every chatbot, made prompting visibly change the output, caught the AI
making something up, and planned a project that ties the whole course together.

**Post it to the chat wins board:** *"I caught an AI hallucinating — and I know why it happens! 🎉"*

## Take-home → your capstone
Build it for the final session. Keep it small enough to actually *run*. Then present it — walk your stack
from the box to the AI, in your own words. **Everyone claps.** 👏
