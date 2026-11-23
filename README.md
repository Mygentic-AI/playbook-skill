# Playbook

A skill for the Claude app that turns the work you repeat into **playbooks**: one folder per
job, holding the steps, the tools that worked, checks that can fail, a log of every
correction, and the job's memory of what earlier runs handled. After every run a fresh
reviewer looks over the output, and when Claude gets something wrong it fixes the playbook,
not just the answer, so the next run starts better.

## Why not just a skill?

A skill can hold steps, scripts, references and templates too, and you can write your own or
copy one and change it. So what does a playbook add?

- **Memory between runs.** A skill starts every run from the same files. A playbook keeps a
  `state.md`: what was already handled (emails triaged, invoices chased and when), what's
  still open, when it last ran. That changes on every run and nobody needs to review it. In
  a skill, each of those changes would need your approval in the app.
- **Its own reviewer.** After the checks, someone who didn't do the work reviews the output: a
  sub-agent when the chat has one. Anything that clearly breaks a rule you already wrote is
  fixed, and the playbook tightened so it can't happen again. Anything that could go either
  way comes back to you with a suggested rule. Every run ends with both lists: "Fixed, and the
  playbook updated" and "Needs your call". On scheduled runs nobody watches, that's the only
  feedback the job gets, and it's kept.
- **Corrections that land as you work.** When you correct a run, Claude writes the fix into the
  right file straight away. Rules still change only with your agreement.
- **One skill, many jobs.** This skill is the method; each job you add is just another folder.

In short: skills tell Claude how to do a job. A playbook also remembers what it handled, what
you corrected, and what its own reviewer flagged. So it gets better even on the runs you
don't watch.

**The trade-off:** a skill works in every chat; a playbook works only where its folder is
connected or inside its Project. **A good test:** does this job need to remember anything from
last time? If not, a skill is enough. Once a playbook's rules stop changing, its steps can
become a skill, and the folder keeps only its memory.

## Install

### Claude app (desktop, web): upload the ZIP

1. Download `playbook.zip` from the [latest release](https://github.com/Mygentic-AI/playbook-skill/releases/latest).
   Use the release file, not GitHub's "Source code" ZIP, which has the wrong layout.
2. In the Claude app: **Customize → Skills → + → Create skill → Upload a skill**, and pick the ZIP.
3. Make sure **Code execution and file creation** is switched on.

Skills belong to your account. We've used it on desktop; the phone app is listed under "Not tested yet" below.

### From GitHub as a plugin

- **Claude Code:** `/plugin marketplace add Mygentic-AI/playbook-skill`, then `/plugin install playbook@playbook-skill`.
- **Claude app:** some guides describe **Customize → Plugins → Add marketplace** with this
  repo's URL. We haven't tried this route in the app yet.

## Get started

Say:

> **Set up my playbooks**

Claude explains what a playbook is, asks where you want yours kept, helps you pick a first
job, interviews you about it, writes the playbook, and runs it once on a real example so
you can make your first correction. Have a real piece of that work at hand; the first
session takes about half an hour.

## Where your playbooks live: your choice

| | **On your computer** | **In a Claude Project** |
|---|---|---|
| Files are | in a `Playbooks` folder on your computer | in your Claude account, in one Project |
| Desktop | any chat with the folder connected | chats inside that Project |
| Phone | only while the desktop app is open and active and the computer is online (not fully tested) | chats inside that Project, any time |
| Privacy | data stays on your computer | data is stored by Claude |

**On your computer:** create an empty `Playbooks` folder yourself and connect only that
folder. Don't connect Documents or your home folder: the chat can see everything in a
connected folder. Access lasts one chat, so connect it at the start of each new chat.

**In a Project:** create the Project yourself (Claude can't), and do your playbook work in
chats inside it. Chats outside it, or in other Projects, can't see its playbooks. A
playbook you need in several Projects is copied into each; the skill helps with that.

## Everyday phrases

| Say | What happens |
|---|---|
| "set up my playbooks" | first-time setup |
| "make a playbook for my invoice chasing" | interview, then a new playbook |
| "do my weekly client update" | runs that playbook, checks it, reports pass/fail |
| "what playbooks do I have?" | lists them |
| "make me an email triage playbook" | starts from the bundled example template |
| "make it run every morning" | schedules a playbook that has had its first corrected run |

After every run, Claude asks whether anything was wrong and whether to keep anything as a
template, example or script. Answer in plain words; it updates the playbook.

## Example template: email triage

The skill ships with one worked **example template**: email triage (sort new email,
draft replies to what needs one today). It's a model Claude starts the interview from, not
a playbook that runs as-is: your VIPs, categories and limits replace every placeholder.
See [`references/examples/email-triage/`](plugins/playbook/skills/playbook/references/examples/email-triage/).

- Needs an email connector (Gmail or Outlook) switched on in the Claude app.
- **Default: read and draft only.** Claude never sends, labels, archives or deletes.
- You can turn sending on during setup. Even then, Claude only sends drafts you approve
  by number in the chat. There is no automatic sending.

## What's been tested

Working in a Claude Project (tested by hand, November 2026):
- Claude creates files in the Project, in subfolders, and a new chat finds them.
- A script saved in the Project runs unchanged in a later chat.
- Corrections saved in one chat are there in the next, and an older open chat sees them.

Working from the phone with files on the computer:
- A phone chat reaches the computer through the desktop app while it's open, and can list
  the files in a connected folder.

Sub-agents for the review step:
- Available in the Claude app, including chats opened from the phone; they run in the cloud.
  Which tools a chat gets can vary by session, so the skill falls back to a self-review pass.

Not tested yet:
- Opening or writing files in a computer folder from the phone.
- Phone and desktop opening the same Project's playbooks.
- The skill triggering inside a Project on the phone.
- Images, logos and other non-text files in a Project (Project files come through as text).
- Installing from GitHub inside the Claude app.
- The email-triage example with a real Gmail or Outlook connector (tested only on a sample inbox).
- Scheduled runs: whether a scheduled task finds a Project or folder home, and under what
  conditions it fires (computer awake, app open).

## For contributors

- The skill: `plugins/playbook/skills/playbook/`
- App test prompts: [`TESTING.md`](TESTING.md)
- Skill-creator evals: `evals/` (from Claude Code these cover the computer-folder home only)
- Build the release ZIP: `./build.sh` → `dist/playbook.zip`

MIT licensed.
