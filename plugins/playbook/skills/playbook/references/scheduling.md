# Closing the loop: schedule, place, owner

A playbook that runs only when the user asks is a well-written procedure, not a delegation.
The Delegation Loop needs four things: a **job** (one thing, stated in one sentence), a
**schedule** (it runs without anyone pressing a button), a **place** (the output lands
where the user already looks) and an **owner** (one person checks it for the first two
weeks). The interview gives you the job. This file covers the other three.

Offer this once a playbook has had its first corrected run, not before: scheduling a
playbook nobody has corrected yet repeats its mistakes three times a day.

## 1. The job, in one sentence

Put it at the top of `PLAYBOOK.md`, under the title, before "Purpose":

> Job: Every morning, list the leads who replied and did not get an answer.

If you can't write it in one sentence, the playbook is doing two jobs. Split it, and let
the two share data (see "Shared files" in `SKILL.md`).

## 2. Schedule

Use the app's scheduled-task tool if this session has one (it may need to be searched
for before it can be used). Call it a "scheduled task" when talking to the user. If there
is no such tool here, say so plainly and give the user the one line to type each time
instead ("do my <job name>"); don't pretend the job is automated.

Tell the user the conditions for unattended runs as the app states them (for example
whether the computer must be awake and the desktop app open). If you can't tell, say that
too: a schedule that silently doesn't fire is worse than none.

- **Ask the time and frequency in the interview** if the job is recurring, and use the
  user's timezone.
- **One task can run several playbooks** in order (for example triage, then digest). The
  user gets one notification per run instead of several.
- **Write the prompt to stand alone.** Each run starts a fresh session that remembers
  nothing. The prompt must name the home (the Project or folder), the playbooks to run,
  the order, the permissions, where to write the output, and what to say at the end.
- **Say what to do when something is missing.** "If you cannot reach the playbook home or
  the connector, stop and tell the user which one failed. Do not improvise from memory."
- **In a Project home, scripts don't run in place.** The prompt must say to recreate the
  playbook's folder layout in the workspace, including any shared files a script reads.
- **Fire one test run straight away**, if the tools allow it, and read what came back
  before calling the loop done. If you can't fire it, say so, and tell the user how to
  run it themselves or when the first scheduled run is.
- **Record it** in `PLAYBOOKS.md` under "Schedule": task name and id, times, timezone, and
  "verified" or "not yet verified" until a run has completed unattended.

### Recurring runs must be idempotent

A scheduled job will see the same items twice: overlapping windows, retries, a late run.
Keep the ids of what each run handled in the playbook's `state.md` (the last few days is
enough), and skip ids already there. Don't rely on "since the last run time" alone: some
connectors search by date only, and their day boundaries may not be in the user's
timezone. Search from a day earlier and let the id list remove repeats.

## 3. Place

Ask: "Where do you already look every day?" Then put the output there, or put a pointer
there.

- **Prefer the place over a new doc.** A report in a Project doc is a new place the user
  has to remember. An email to themselves, a message in the channel they read, or the item
  left in their inbox with a label lands where they already are.
- **Things that need action belong where action happens.** For email, that can mean
  leaving them in the inbox with a label and filing the rest, but only if the user has
  agreed to the label and move rungs in `rules.md`. If they haven't, offer labelling
  once (it puts the sorting where they already look) and turn it on only if they agree. With the default read-and-draft
  access, send the summary to the place instead and touch nothing in the inbox.
- **Keep a full record too,** in the home (for example `reports/YYYY-MM-DD.md`), newest
  run at the top. Remove old records after a period the user picks.
- **Notification text leads with what needs the user,** then the counts, then the path.

## 4. Owner

One person checks every output for the first two weeks. In practice that is usually the
user. Write it down:

```
- Owner: Sam, checking every report until 2026-12-07
```

in the playbook's entry in `PLAYBOOKS.md`. Until that date, end each run's notification
with the two after-run questions. After it, ask the owner whether to keep checking, check
weekly, or only on failures, and record the answer.

## Done means

- [ ] The job fits in one sentence at the top of `PLAYBOOK.md`
- [ ] A scheduled task exists, and `PLAYBOOKS.md` records it
- [ ] One unattended run has completed and its output was read (or the gap is stated)
- [ ] The output reaches a place the user already looks
- [ ] An owner and a checking-until date are recorded
