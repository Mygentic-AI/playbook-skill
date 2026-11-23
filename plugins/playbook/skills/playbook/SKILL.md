---
name: playbook
description: Build and run playbooks, one folder per job the user repeats (steps, scripts, reference files, good examples, checks, a corrections log, and memory of what earlier runs handled), kept on their computer or in a Claude Project, reviewed after every run and improved every time they correct the output. Use whenever the user says "set up my playbooks", "make a playbook for X", "do my weekly X", "run my X playbook", "what playbooks do I have", or describes work they do every week and want to hand off, such as client updates, invoice chasing, content repurposing, reports or hiring screens. Also use right after a playbook run when the user corrects the result ("that's wrong again", "same mistake as last time", "no, it should be...") so the fix goes into the playbook, not the chat, and when they approve a result ("perfect, keep this") so the good version is saved as a template, example or script. Use it even when the user doesn't say "playbook" if a PLAYBOOKS.md file is in the connected folder or the Project's files.
---

# Playbook

A playbook is one folder per job the user repeats. It holds their judgment written down
(the steps and the rules for each decision), the tools that worked (scripts, templates,
reference data, approved examples), checks that can fail, a log of every correction, and
the job's memory: what earlier runs handled and what's still open.

A skill tells Claude how to do a job, and every change to it needs the user's approval.
A playbook also remembers what it handled, what the user corrected, and what its own
reviewer flagged, in a folder Claude can write to as it works. So it gets better even on
the runs nobody watches. The chat closes; the folder remains.

The method comes from "The AI Delegation Loop" by The Actionable AI
(theactionableai.com/guides/ai-delegation-loop). The wording here is our own.

## Before anything else, in every chat: find the playbook home

Playbooks are the user's data and must survive the chat. They can live in exactly two
kinds of place, and the user chooses which at setup:

| Home | Where the files are | Works from |
|---|---|---|
| **On their computer** | a dedicated folder, normally `~/Playbooks`, connected to this chat | desktop; the phone too, but only while the desktop app is installed, open, active and the computer is online (saving changes from the phone is not yet confirmed: if a write fails there, say so) |
| **In a Claude Project** | the Project's files | any chat inside that Project, desktop or phone. Chats outside it, or in other Projects, cannot see it |

Work out which one you have from what you can actually do, not from tool names:

1. **A folder is connected and contains `PLAYBOOKS.md`** → local home. Use it.
2. **This chat is inside a Project and the Project's files include a `PLAYBOOKS.md`**
   (search for it; it may sit under a prefix such as `claude/`) → Project home. Use it.
3. **Neither, but the user is asking to set up** → read `references/setup.md`.
4. **Neither, and the user wants to run or fix a playbook** → stop and say what is
   missing in one or two plain sentences, for example: "I can't see your playbooks in
   this chat. Connect your Playbooks folder, or open the Project they live in and ask
   again." Do not carry on: anything you write would vanish when the chat ends. If they
   need a new chat for it, give them a one-block message to paste there that repeats
   their request (e.g. "Do my weekly client update for ACME Group").

Whenever you send the user to a new chat, for any reason, give them the message to paste
as its first message, in one copy-paste block. The new chat remembers nothing of this one.

Never ask for a broad folder such as Documents, Desktop or the home folder. Connecting
a folder exposes everything in it to the chat. Ask for the Playbooks folder by name.

Folder access lasts one chat. In a new chat, ask for the Playbooks folder again before
doing playbook work.

## What the user wants → what to read

| The user says | Read |
|---|---|
| "set up my playbooks", first time, no home yet | `references/setup.md` |
| "make a playbook for X", "I do X every week" | `references/interview.md` |
| "do my X", "run the X playbook" | `references/running.md` |
| corrects an output from a playbook | `references/corrections.md` |
| "perfect, keep this", or a run went well | `references/toolbox.md` |
| "add checks", or a playbook has none that can fail | `references/checks.md` |
| reviewing a run's output before handing it over | `references/review.md` |
| "what playbooks do I have?" | read `PLAYBOOKS.md` and list name + when to use |
| "use this playbook in my other Project too" | `references/sharing.md` |
| "run this every morning", "automate it", or a playbook's first corrected run is done | `references/scheduling.md` |
| wants an email-triage playbook and has none yet | `references/interview.md`, starting from `references/examples/email-triage/` |

## Layout of a home

```
<home>/
├── PLAYBOOKS.md                 index: storage choice, schedule, one entry per playbook
├── shared/                      data two or more playbooks read (e.g. a sender list)
└── playbooks/
    └── <job-name>/
        ├── PLAYBOOK.md          purpose, when to use, inputs, steps, decisions, checks
        ├── scripts/             code for mechanical steps and for checks
        ├── references/          INDEX.md, rules, reference data, examples/
        ├── assets/              templates copied into the output
        ├── state.md             memory between runs: last run, what's handled, what's open
        └── notes.md             corrections log, newest first
```

Starting files are in `assets/playbook-template/` and `assets/PLAYBOOKS.md`. In a local
home you can copy the playbook folder with `scripts/new_playbook.py <home> <job-name>`
(write `PLAYBOOKS.md` yourself during setup; the script doesn't touch it). In a Project
home there is no copy command: write each file into the Project one by one, using the
template text.

`references/examples/` holds **example templates**, starting with email triage. They are
models to start an interview from, never a user's playbook: don't run them, don't list
them as the user's playbooks, and don't copy them into a home unchanged. Tell the user
when you're starting from one.

**Shared files.** When two playbooks need the same data (a sender list, a client list),
keep one copy in `<home>/shared/` and point both playbooks' `INDEX.md` at it. Don't park it
inside one playbook's folder: the other playbook then depends on a folder it doesn't own.
Scripts name every file they read at the top, so a Project run can recreate exactly those.

`PLAYBOOK.md` is deliberately not called `SKILL.md`. Playbooks are data this skill reads,
not separate skills, and the name keeps them from being mistaken for one.

## After every playbook run, ask two short questions

1. "Anything wrong? I'll fix the playbook itself, not just this answer."
2. "Worth keeping any of this as a template, example or script?"

Users should not have to learn modes. These two questions are how corrections and saved
tools reach the folder. Keep them to one line each. After a rerun that follows a
correction, ask only "Anything else wrong?", but go back to asking both on the next
normal run: the save question is easy to drop, and dropping it leaves the examples folder
empty. The first time the owner accepts a run with no corrections, ask in one line:
"Save this run as the example of a good one?" Save it to `references/examples/` only on
a yes; it may hold other people's messages.

## Principles, and why

- **Fix the playbook, not the chat.** A correction typed into chat is gone next week.
  Write it into the folder, then rerun.
- **Someone who didn't do the work reviews it.** After the checks, a fresh reviewer (a
  sub-agent when the session has one) looks for what scripts can't measure. What it can't
  fix now is logged, and a pattern becomes a proposed rule, never a silent one.
- **A check that cannot fail is not a check.** "Looks professional" proves nothing. "Every
  figure appears in the source file" can be checked and can fail. Without real checks the
  user is still the quality control, which is the job they were handing over.
- **Say what was not saved.** If a write fails, or there is no home, tell the user plainly.
  Never let them believe a correction was stored when it wasn't.
- **One file per purpose.** Two near-identical files is how the wrong one gets used.
- **A playbook nobody runs is a document.** Once the first run is corrected, offer to
  schedule it, send the output where the user already looks, and name an owner
  (`references/scheduling.md`).
- **Ask, but make bold, helpful suggestions.** A skill that only offers the safest option
  is useless. When something would clearly help (a schedule, a summary sent to the user,
  tagging or filing), recommend it plainly with the reason ("I'd like to ... so you ...
  Shall I?"), not as a hedged option buried in warnings. Then act on the yes. Keep
  warnings for real risks, and know what each safeguard is for: keeping sending off
  protects other people from what the user didn't mean to put out, not the user from a
  summary of their own work.
- **The user's words beat your draft.** You write the files, but every rule comes from
  the user. When unsure, ask rather than invent a rule.
