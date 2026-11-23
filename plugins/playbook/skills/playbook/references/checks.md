# Definition of done: checks that can fail

A playbook without checks leaves the user doing the quality control, which is the job they
were trying to hand over. An AI saying "this looks good" about its own output is worth
nothing.

## Writing checks

Write 5 to 10 checks in the playbook's "Definition of done". Each one must:

- be specific to this job,
- be verifiable with evidence from outside the output: a number traced to a source file,
  a link that loads, a count, an exact quote match, a comparison with a reference file,
  a script that runs,
- be able to fail. If you can't imagine it failing, rewrite it.

Banned: "clear", "professional", "high quality", "engaging", "accurate" on their own.
Turn each into something countable or traceable.

Where a check is mechanical, write it as a script in `scripts/` (e.g.
`check_word_count.py`) and name the script in the check, so the result comes from code,
not from your judgment.

## Examples

**Email triage** (full example template in `references/examples/email-triage/`)
- Every fetched email is in exactly one category (`scripts/check_triage.py`).
- Every email from a VIP in `references/people.md` is in "reply today".
- Nothing was sent unless sending is on and the user approved that draft in the chat.
- Nothing was archived, labelled or deleted.
- Every draft quotes or names the question it answers.

**Weekly client update**
- Every figure appears in the pulled data file.
- No adjective without a number next to it.
- Under 200 words (`scripts/check_word_count.py`).
- The client's name matches `references/data.md` exactly.
- The action promised last week is addressed.

**Content repurposing**
- Hook under 12 words.
- No word from the banned list in `references/rules.md`.
- Every quote matches the transcript word for word.
- The first line isn't the payoff.

**Chasing invoices**
- Amount and due date match the invoice record.
- Tone matches the stage in `references/escalation.md` for how late it is.
- The payment link opens.

**Hiring screen**
- Every score cites a line from the candidate's answer.
- The summary contradicts nothing in the scorecard.

## On every run

Run every check, fix failures, run again, then report pass or fail per check with its
evidence, and list anything you couldn't verify. More than two failures on the first pass
means the playbook has a gap. Name it (`references/corrections.md`) instead of patching.
