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

## Starting from an example template

If the job matches an example in `references/examples/` (for now: email triage), say so:
"There's an example email-triage playbook I'll start from. I'll ask about your own
VIPs, categories and limits." Use its structure to shape your questions, but the user's
answers replace every [bracketed] part, and anything they don't confirm comes out.
Ask the extra questions listed in the example's README as well as the general ones below.
Remove the EXAMPLE TEMPLATE banner from the files you write for them. Where the example's
files differ from the generic template (e.g. `people.md` instead of `data.md`), use the
example's and drop the generic file, so there's one file per purpose.

For anything that touches an account (an inbox, a drive, a CRM, a calendar), agree what
Claude may do there and write each permission into `rules.md` with the date it was
agreed. Typical steps, from least to most reach:

1. read
2. tag or label
3. move, file or archive
4. draft
5. send, post, share or delete

Start with what the job needs. Anything more is done only once the user agrees, never
assumed from the job description. Recommend the steps that would clearly help, plainly
and with the reason ("I'd like to tag each one by client so you can see them at a
glance. Shall I?"), then act on the yes. Add a check that nothing beyond the agreed
permissions was done.

Know what each limit is for. Keeping send, post and share off protects other people from
something the user didn't mean to put out; never set those up to happen automatically.
Delivering the result to the user themselves (a note to their own inbox, a message in
their own channel) carries no such risk: recommend it.

## Look at the data before you ask about it

When the job works on data a connector can show you (an inbox, a folder, a sheet, a
calendar), first ask: "Is there anything in there I shouldn't open, like bank, health
or legal material?" Write the answer into `rules.md` as "Never read". Then pull a real sample, skipping
anything on that list, before the questions about categories and rules: two weeks
is usually enough to see the weekly repeats. Group it, propose the categories, and let
the user correct them. People define their own mail or files badly from memory and very
well when shown them. Say what you sampled and how much, and keep it read-only.

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
9. **What not to touch.** "Is there anything I shouldn't read, open or change at all?"
   (banks, health, a folder of contracts). Write the answer into `rules.md` as a hard rule.
10. **What it must remember.** "What does next week's run need to know about this one?"
    (what's already been sent or chased, open items, the last date it ran). This goes in
    `state.md`. If the answer is "nothing", say so: a plain skill may be enough for this job.
11. **When it should run.** If the job is recurring: how often, what time, which timezone.
    You'll need this for `references/scheduling.md`.

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
`references/INDEX.md`. Fill `state.md` with what the job must remember (question 10), or
note that it has nothing to remember yet.

## Review with the user

Show `PLAYBOOK.md` and ask two questions:

1. "What did I get wrong?"
2. "What did you forget to tell me?"

Expect the first version to be about 80% right. Fix it in the file, not in the chat.
Then add checks (`references/checks.md`) and run it (`references/running.md`).
