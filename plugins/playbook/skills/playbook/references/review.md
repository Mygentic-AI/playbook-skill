# Independent review

Checks catch what a script can measure. A reviewer catches what needs judgment: does the
draft answer the question that was asked, does it match the approved examples, does it say
anything the source doesn't support. Claude marking its own work in the same breath is
anchored on its own reasoning, so the review is done by someone who didn't do the work.

Run it after the checks pass, before handing over. Skip it only for jobs whose output is
fully covered by mechanical checks (a sorted list, a filled-in form), and say so.

## Who reviews

- **A sub-agent, if this session can start one.** Give it a fresh, tightly scoped brief
  (below). Keep it small: it needs the output and the few files that define "good", not
  the whole conversation.
- **Otherwise, a separate review pass.** Set the draft aside, re-read only the files in the
  brief, and review as if someone else wrote it. This is weaker, because it is the same
  session marking its own work.

Say which one you used in the check report ("Reviewed by: a separate reviewer" or
"Reviewed by: a self-review pass, no sub-agent here").

## The brief

Give the reviewer only:

- the output of this run;
- the source inputs it was made from;
- the playbook's "Intent", "Definition of done" and `references/rules.md`;
- the approved examples in `references/examples/`, if any;
- the "Suspected" section of `notes.md`, so it knows what it flagged before.

Not the drafting conversation. Paste the text of these into the brief rather than giving
paths: sub-agents run in the cloud, so one asked to open files in a folder on the user's
computer fails whenever that computer is asleep or offline.

Ask it for at most five findings, each with:

1. what is wrong, in one line;
2. the evidence: a quote from the output and, where relevant, from the source or a rule;
3. which kind it is (below).

Tell it to report nothing rather than pad the list. A finding without evidence is dropped.

## Two kinds of finding

**1. Certain: it breaks something already written down.** The output contradicts a rule in
`rules.md`, a step or decision in `PLAYBOOK.md`, a check, or the source itself, and the
quote proves it. Example: a sender listed as a VIP in `people.md` was filed as FYI.

- Fix the output.
- Then update the playbook so it can't slip through again: add or tighten a check, clarify
  the step that allowed it, or add the case to an example. Log it in `notes.md` as a
  correction.
- **Only enforce what the user already said.** If the fix needs a decision they have never
  made (a new rule, a new category, a change of tone), it is not certain: treat it as kind 2.

Use the "Intent" section as the lens for anything the rules don't cover: does the output do
what the job is for, and could anything it skipped cause the harm the user is afraid of? A
finding that rests on the intent alone, not a written rule, is kind 2.

The intent can be wrong too: Claude wrote it from a conversation and may have missed a
nuance. If the reviewer sees an improvement that is sound on its own merits but conflicts
with the written intent, it doesn't discard it and doesn't make it automatically. It goes
under "Needs your call" with the conflicting line of the intent and a suggested rewording,
so the user can decide whether the improvement or the intent should change. A kind 1 fix
that would conflict with the intent becomes kind 2 for the same reason.

**2. Unsure: it might be wrong, or it could go either way.** Example: "I put this in FYI, but
it could be reply-today." Or a draft that may be too blunt for this client.

- Don't change the playbook.
- Explain the doubt in one or two lines and **propose a rule that would settle it**
  ("Emails that ask a direct question go to reply-today, even from newsletters' senders?").
- Log it under "Suspected" in `notes.md` until the user answers. When they do, write the
  rule into `rules.md` (or record that it's not a problem) and remove the line.

## Report both, after the output

End every run with the two lists, in plain words, before the after-run questions:

> **Fixed, and the playbook updated:**
> 1. Northwind's email was filed as FYI; they're a VIP. Moved to reply-today.
>    Playbook: the VIP check now also matches their second address.
>    Before: `@northwind.com` · Now: `@northwind.com, @northwind-group.com` (people.md,
>    check_triage.py). Say "undo 1" to reverse it.
>
> **Needs your call:**
> - The Delta Print email asks a question but reads like a newsletter. I put it in FYI.
>   Suggested rule: "Any email that asks me a direct question goes to reply-today." Add it?

Every automatic fix is flagged, however small: number it, say what changed in the output
and in the playbook, show before and after for the playbook change, name the file, and
offer "undo <number>". Log each one in `notes.md` marked `auto-fix`, so it can be found and
reversed later. If a list is empty, say "Nothing fixed" or "Nothing needs your call".
Never let a playbook change go unreported.

## Unattended runs

When a scheduled run has nobody watching, the reviewer is the only feedback it gets. Kind 1
fixes and playbook updates go ahead as above; kind 2 questions wait. Put both lists in the
run's report and its notification, so the owner sees them next time they look.
