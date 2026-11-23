# Writing a playbook: the interview

The user knows the job; you know how to write it down. Don't draft the steps yourself and
ask for approval: people approve a plausible draft and the unwritten rules stay in their
head. Interview first, write second.

## Interview rules

- **One question at a time.** Wait for the answer before the next.
- **At least eight questions** before writing anything. Follow up when an answer is vague
  ("depends" always hides a rule: ask what it depends on).
- **Ask for real material** wherever it exists: a past output they liked, the template
  they use, the file the numbers come from.

## What to cover

1. **Trigger and frequency.** What starts this job? How often?
2. **Inputs.** What does it need, and where does each thing live (file, app, inbox,
   dashboard, their head)?
3. **Steps, in the real order.** Walk through the last time they did it.
4. **Decisions.** Every point where they choose. What's the rule? ("If the client is
   behind plan, lead with the fix, not the number.")
5. **Done.** How do they know it's finished and good?
6. **Edge cases.** What went wrong in the past? What's unusual but recurring?
7. **Standard and tone.** Who reads it? What does "good" sound like? Words to avoid?
8. **What a bad version looks like.** This is often where the real rules come out.

## Write the playbook

Create `playbooks/<job-name>/` from `assets/playbook-template/` (kebab-case name, e.g.
`weekly-client-update`). Fill `PLAYBOOK.md`:

- **Purpose:** one line.
- **When to use this:** one or two lines a different chat could match against. Make it
  specific enough that two playbooks are never confused.
- **Inputs:** what and where.
- **Steps:** numbered, plain language, real order.
- **Decisions:** "if X, then Y" lines.
- **Definition of done:** leave for `references/checks.md`, but note any checks the user
  already mentioned.
- **Edge cases.**

Add an entry to `PLAYBOOKS.md`: name, folder, "when to use this" line, date created.

Save any material the user gave you: approved past outputs into `references/examples/`,
templates into `assets/`, names and targets into `references/data.md`. List each in
`references/INDEX.md`.

## Review with the user

Show `PLAYBOOK.md` and ask two questions:

1. "What did I get wrong?"
2. "What did you forget to tell me?"

Expect the first version to be about 80% right. Fix it in the file, not in the chat.
Then add checks (`references/checks.md`) and run it (`references/running.md`).
