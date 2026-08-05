**# Lab (M6): protect yourself (and see how protection works)**

**You'll need:** your **own device** (for your accounts) and your **Codespace** (for the hashing demo). **Nothing to install.**
**Time:** ~30–40 minutes • **Work in your breakout pair** but keep your *own* passwords private.

> Heads up: no judgment in this lab, almost everyone has reused a password or skipped 2FA.
> The goal is to improve **one** habit today. Nothing here exposes your real passwords.

--------------------------------------------------------------------------------------------------------

**## Part A: See how passwords are really stored (Codespace)**

**## Step 1:** Turn a "password" into a hash
In your Codespace terminal:
```text
$ echo -n "correct-horse" | sha256sum
```

✅ **You should now see:** a long string of letters/numbers ending in `-`, e.g.
`9dca666e…d163`. That **hash** is what a good website stores — *never your actual password*.

## Step 2: Prove it's one-way and consistent
```text
$ echo -n "correct-horse" | sha256sum      # same input...
$ echo -n "correct-horsf" | sha256sum      # ...one letter changed
```

✅ **You should now see:** the first line is **identical** to Step 1 (same input → same hash), but the second is **completely different** one changed letter scrambles the whole thing (the **avalanche effect**). And there's no way to run it backwards to get the password. *That's* why hashing protects you.

------------------------------------------------------------------------------------------------------

**## Part B:** Audit your own security (your own device)

**## Step 3:** Check 2FA on your most important account
Open your **email** account's security settings. Is **two-factor authentication (2FA)** on?

✅ **You should now see:** whether 2FA is on or off. If off, this is the single highest-value fix, email is the "master key" (password resets go there). Turn it on (or plan to today).

**## Step 4:** Spot password reuse
Think honestly: do you use the **same password** on more than one important site?

✅ **You should now see / admit:** at least one place you reuse a password. The fix is a **password manager** one strong, unique password per site, remembered for you. (Note one to set up.)

---

**## Part C:** Spot the phish (worksheet)

**## Step 5:** Find the red flags
Here's a (fake) email. Find as many red flags as you can:

> **From:** Apple Support `<no-reply@apple-id-verify.support-secure.com>`
> **Subject:** ⚠️ URGENT: Your account will be DISABLED in 24 hours
> Dear Customer, We detected unusual activity. Verify your identity immediately or lose access.
> 👉 **[Verify my account now](http://apple-id-verify.support-secure.com/login)**
> Failure to act will result in permanent suspension.

✅ **You should now see (at least 3):** the **sender domain** isn't apple.com; **urgency/threats**; a **generic greeting** ("Dear Customer"); a **link** to a fake domain (not apple.com) over **http** (no padlock). The rule: **never log in from a link in a message** go to the real site yourself.

---

**## Part D:** Least privilege (Codespace, callback to M4)

**## Step 6:** You're not the boss (and that's good)
```text
$ whoami
$ touch /etc/test-file 2>&1 || echo "→ blocked, as expected"
```

✅ **You should now see:** `whoami` is your normal user (e.g. `vscode`, *not* `root`), and writing to a system folder is **blocked** ("Permission denied"). That's **least privilege**: if something malicious ran as you, it couldn't wreck the whole system. (Admin power needs `sudo` on purpose.)

---

## 🎉 Your win
You can explain how hashing, encryption, and 2FA actually protect you, you spotted a phishing
attempt's red flags, and you saw least privilege in action — and you improved one real habit today.

**Post it to the chat wins board:** *"I turned on 2FA / caught a phish red flag 🔒🎉"*

## Take-home (optional)
Set up a **password manager** (many are free) and move your three most important accounts into it
with new, unique passwords — starting with email. It's the highest-leverage hour in this whole course.
