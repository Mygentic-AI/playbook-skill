# First-time setup

Goal of the first session: a working home, one real playbook, and one real run of it with
the user's first correction written back. Stopping once the playbook is written leaves a
document nobody uses; the first correction is what teaches the user how the loop works.
Expect about half an hour, and ask the user to have a real piece of this work at hand.

## 0. Coming back after creating the container

If this chat is already inside a Project, or an empty Playbooks folder is connected, the
user has probably just done step 3. Confirm what you can see ("I can see this Project's
files" / "I can see your Playbooks folder"), check it matches the storage choice, and go
straight to step 4. Don't repeat the explanation or the questions.

## 1. Explain in three lines

Something like:

> A playbook is one folder per job you repeat. I learn the job once by interviewing you,
> then every time you correct me, I fix the playbook rather than just the answer, so it
> gets better each week.

## 2. Let the user choose where playbooks live

This is their trade-off, not yours. Ask in their terms:

1. "Do your playbooks and the data they use need to stay on your computer?"
2. "Do you want to use them from your phone as well as your desktop?"

Then explain the consequence of their answers:

- **On your computer** (privacy first): "Everything stays in a folder on your computer.
  You can still use it from your phone, but only while your computer is on, online and
  the Claude desktop app is open. On the phone you'll connect the folder at the start of
  each chat." (Saving changes from the phone is not yet confirmed. If a write fails on
  the phone, tell the user rather than carrying on.)
- **In a Project** (portability first): "Your playbooks are stored in your Claude account,
  inside one Project, and work from any chat in that Project on desktop or phone. Chats
  outside that Project can't see them, so keep the work they're for in the same Project."

If they want both privacy and phone use, the computer option with its conditions is the
only one that gives both. Say so.

## 3. The user creates the container; you can't

You cannot create a Claude Project, and you cannot create a folder outside a folder that
is already connected. Give the exact step and wait:

- **Computer:** "In Finder (or File Explorer), create an empty folder called Playbooks in
  your home folder, then connect just that folder to this chat. Please don't connect
  Documents or your whole home folder: I'd be able to see everything in it."
- **Project:** "Create a Project in the Claude app for this work (or open the one it
  belongs to), start a new chat inside it, and say 'set up my playbooks' again."

## 4. Prove you can write there before going on

Write `PLAYBOOKS.md` from `assets/PLAYBOOKS.md`, filling in the storage choice and today's
date. Then read it back.

- In a Project, files you write may land under a prefix such as `claude/`. Note the real
  path you got back and record it in `PLAYBOOKS.md` under "Home path", so later chats
  look in the right place.
- If the write or the read-back fails, stop and tell the user exactly what failed. Do not
  continue setup with nowhere to save.

## 5. Project homes: one line for the Project instructions

Offer this line for the user to paste into the Project's custom instructions, so the skill
is used reliably in every chat there:

> This Project keeps playbooks in its files (see PLAYBOOKS.md). For any job listed there,
> and for any correction to a playbook's output, use the playbook skill.

## 6. Pick the first job

Suggest the job the user does most often, not the most complicated one. A good first job:

- happens at least weekly,
- they would recognise a bad version instantly,
- they could explain to a new hire in under 20 minutes.

If they go blank, offer examples, starting with the one most people want:

- **Email triage**: sort new email and draft replies to what needs one today. There's a
  worked example template for this (`references/examples/email-triage/`); it needs an
  email connector switched on.
- A weekly client or team update, chasing late invoices, turning a video or call into
  social posts, a recurring report, screening applicants.

## 7. Interview, write, run

1. Follow `references/interview.md` to write the playbook.
2. Run it straight away on the real example the user has at hand (`references/running.md`).
3. Ask the two after-run questions. Apply the first correction with
   `references/corrections.md`, so they see the playbook change.

## 8. Close with the words to use next time

> Next time, just say "do my <job name>". If I get something wrong, tell me and I'll fix
> the playbook. To see everything you've set up, ask "what playbooks do I have?"

For a computer home, add: "In a new chat, connect your Playbooks folder first."
