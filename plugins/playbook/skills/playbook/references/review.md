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
- the playbook's "Definition of done" and `references/rules.md`;
- the approved examples in `references/examples/`, if any;
- the "Suspected" section of `notes.md`, so it knows what it flagged before.

Not the drafting conversation. Paste the text of these into the brief rather than giving
paths: sub-agents run in the cloud, so one asked to open files in a folder on the user's
computer fails whenever that computer is asleep or offline.

Ask it for at most five findings, each with:

1. what is wrong, in one line;
2. the evidence: a quote from the output and, where relevant, from the source or a rule;
3. whether it can be fixed in this output, or points at the playbook itself;
4. how sure it is (sure / likely / unsure).

Tell it to report nothing rather than pad the list. A finding without evidence is dropped.

## What to do with the findings

- **Fixable in this output, and sure or likely:** fix it before handing over, and mention
  the fix in one line.
- **Unsure, or about the playbook itself:** don't change anything. Add one line to the
  "Suspected" section of `notes.md`:
  `YYYY-MM-DD | reviewer | what it flagged | evidence`.
- **The same thing flagged three times** (check "Suspected"): propose a rule or a check to
  the user in plain words, with the dated lines as evidence. Change `rules.md` or add a
  check only if they agree. The reviewer improves outputs on its own; it never rewrites
  the playbook on its own.
- **The user later says a flagged item was fine:** remove it from "Suspected" and, if it
  keeps coming up, add a line to the reviewer brief section of `PLAYBOOK.md` saying it is
  not a problem. A reviewer that cries wolf gets ignored.

## Unattended runs

When a scheduled run has nobody watching, the reviewer is the only feedback it gets. Put
its findings, fixed and unfixed, in the run's report and its notification, so the owner
sees them next time they look.
