# M6 — Security & privacy

> The internet can feel scary — breaches, hackers, scams in the news. Today we replace that vague
> dread with a clear picture: who's actually after your stuff, how they really get in (hint: it's
> usually not code), and the handful of habits that stop the vast majority of attacks. You'll even
> watch a password turn into an unbreakable hash.

**Today's win:** you can describe a basic threat model, explain how passwords/encryption/2FA actually protect you, spot a phishing attempt, and name the few habits that stop most attacks.

### Today you will
- Watch a password become a one-way **hash** — and see the **avalanche effect**
- Audit your own security: **2FA**, password reuse, updates
- **Dissect a phishing email** for its red flags, and reason about **least privilege**

### Environment
Some steps are on your **own machine** (your accounts/settings); the hashing demo runs in your **Codespace**. New to it? See **[How to open your Codespace](../resources/install-guides/codespaces.md)**.

### Run of show (~50 min) — *plan ~2 sessions if you go deep*
| Time | What we do |
|------|------------|
| 0:00 | Hook + the win: most attacks are preventable |
| 0:05 | The big ideas: threat model, auth/hashing, encryption, phishing, least privilege (recap in [`notes.md`](notes.md)) |
| 0:10 | **Lab** — audit yourself + the hashing demo + spot the phish (breakout pairs) |
| 0:40 | **Show** — post "I turned on 2FA / I caught a phish red flag 🔒🎉" |
| 0:45 | Wrap + take-home |

### If you get stuck
- No judgment here — *everyone* has reused a password. The point is to improve one habit today.
- Re-read the **✅ You should now see** line; compare findings with your breakout partner.
- The hashing demo can't hurt anything — you're just scrambling text.

### Optional challenge
Check whether your email has appeared in a known breach (search "Have I Been Pwned"). If it has,
that's your cue to change that password and turn on 2FA. Bring back *how many* breaches it found (no details!).
