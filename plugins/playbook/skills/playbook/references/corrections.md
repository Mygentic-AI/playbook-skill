# Corrections: fix the playbook, not the chat

When the user says an output is wrong, the answer in chat is the least important part.
The playbook let the mistake through, and it will do so again next week unless the folder
changes.

## 0. Check the mistake is really in the output

Look at the output the user is correcting. If the mistake isn't there (for example they
say the name was misspelled, but the output never names the client), say so in one line
and ask what they saw, rather than "fixing" something that didn't happen. The
underlying rule may still be worth adding; ask.

## 1. Find which part failed

| Part | It failed if… | Fix |
|---|---|---|
| **Steps** | a step was missing, out of order, or a rule lived only in the user's head | add or reorder the step; write the rule into "Decisions" |
| **Toolbox** | you rebuilt something that already existed, or used a saved file that's out of date | point the step at the file; update or replace the stale file |
| **Script** | a script has a bug, or reads the wrong thing | fix the code; rerun it on the case that failed |
| **Checks** | the output was wrong and no check caught it | add a check that would have failed on this output |
| **Intent** | the correction doesn't fit the "Intent" section: the job is for something the playbook didn't know | say what you've learned in one line, update "Intent" once the user confirms, then check the other rules still fit it |

Often two parts failed: the step that produced the error and the check that missed it.
Fix both. When adding a check, follow `references/checks.md`.

## 2. Make the smallest fix that lasts

**Test the fix against the intent.** A fix should make the playbook serve its intent
better, not just silence this one complaint. If the fix you're about to make would work
against the intent (for example, a rule that hides more mail when the intent is not to
miss anything that matters), say so and ask which one should win.

**Prefer data to rules.** Many corrections are facts about one item, not new behaviour:
"don't mention this sender", "this sender has a second address", "this client's name is
ACME Group". Store those as a marker or a line in the reference data the playbook already
reads (`references/data.md`, or a shared list), and add a check that the marker is
honoured. Write a new rule in `rules.md` only when the behaviour itself changes. Rules
written for single cases pile up, and sooner or later two of them disagree.

Change the playbook's files, not just this output. Prefer one precise line over a
paragraph. If the same mistake has happened before (check `notes.md`), don't add a gentle
reminder; add an explicit rule or a check.

## 3. Log it

Add one line to the top of `notes.md`:

```
2026-11-23 | figures rounded to thousands | steps + checks: step 2 says exact figures; added figure-match check
2026-11-30 | figures rounded again (2nd) | checks: check now runs as scripts/check_figures.py
```

Date, what went wrong (mark repeats), which part or parts, what changed.

## 4. Rerun and show the difference

Run the job again from the playbook, not from memory of the conversation, and show the
user before and after. Then say in one line what you changed in the playbook, and ask only: "Anything else
wrong?" (the save question can wait for a normal run).

If the fix couldn't be saved (no home in this chat, write failed), say so plainly and give
the user the change so it isn't lost.

## Monthly

Read `notes.md`. Several entries in the same part means that part needs more than
patching: steps that keep going wrong may need splitting, and a recurring mechanical
error is a script waiting to be written.
