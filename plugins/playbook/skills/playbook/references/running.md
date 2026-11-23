# Running a playbook

## 1. Find it

Read `PLAYBOOKS.md` and pick the entry whose "when to use this" matches the request. If
two could match, ask which one, then suggest sharpening their "when to use" lines so it
doesn't happen again. If none matches, say so and offer to make one
(`references/interview.md`).

## 2. Load it

Read the playbook's `PLAYBOOK.md`, its `references/INDEX.md`, `references/rules.md` (rules
apply to every output, whether or not a step mentions them), and the latest entries in
`notes.md` (recent corrections are the rules most likely to be broken again). Read the
other files when a step calls for them, not all up front.

Paths in `PLAYBOOK.md` are relative to the playbook's own folder. A file kept elsewhere is
written as its full path from the home (e.g. `<home>/inputs/last-week.csv`). If a path is
ambiguous, fix it in `PLAYBOOK.md` after the run.

## 3. Do the steps

Follow the steps in order and apply the decisions as written. Use saved templates,
examples and scripts rather than rebuilding them; that's what they're for. If a step
can't be done:

- **A file is missing or unreadable:** stop at that step and tell the user what you need.
- **Only the user can supply it** (a decision, a first name, a sign-off): finish the rest,
  leave a clearly marked `[NEEDED: ...]` placeholder, and list what's needed at the top of
  your reply. If it's needed every run, suggest adding it to the playbook.

## Scripts

**Local home:** run the script where it is.

**Project home:** Project files can be read as text but not run in place. Recreate the
playbook's folder layout in your workspace (the script plus every file it reads, at the
same relative paths, including anything it reads from `<home>/shared/`), run it there,
and use the saved version unchanged. If the Project
version changes later, copy it again before the next run.

Either way:

- Scripts find their files relative to their own location (e.g. `../references/data.md`),
  so they work in both homes. Keep it that way when writing new ones.
- **Anything a script produces that should last must be written back** to the home.
  Outputs left in the workspace disappear with the chat.
- Don't assume internet access. If a script needs it and fails, say so, and suggest a
  connector or a manual input instead.
- Never store passwords, API keys or tokens in a playbook.

## 4. Run the checks

Run every check in the "Definition of done". Fix what fails and run them again. Then
report each check as pass or fail with its evidence. List anything you couldn't verify.
If more than two checks fail on the first pass, don't just patch the output: tell the
user which part of the playbook let it happen (see `references/corrections.md`).

## 5. Independent review

Have someone who didn't do the work review it, following `references/review.md`: a
sub-agent if this session can start one, otherwise a separate review pass. Fix what it
finds that can be fixed now; log the rest under "Suspected" in `notes.md`.

## 6. Hand over and ask the two questions

Give the output, the check report and the review in a few lines, then:

1. "Anything wrong? I'll fix the playbook itself, not just this answer."
2. "Worth keeping any of this as a template, example or script?"
