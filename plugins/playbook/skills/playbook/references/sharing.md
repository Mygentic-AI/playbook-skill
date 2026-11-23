# Using a playbook in more than one place

## Same job, many clients

Many users do the same job for many clients or entities: an HR consultancy's first
outreach to each new client, a bookkeeper's month-end close, an agency's weekly report.
The method is the same; the details differ. Set it up like this:

1. **One master playbook** holds the method: steps, decisions, checks, scripts and
   templates that apply to every client, with no client names or data in it. Keep it in a
   home of its own (a "Templates" Project, or the local Playbooks folder).
2. **A copy in each client's Project.** Each client gets its own Project, so its files,
   chats and data stay separate. Copy the master in (below) and customise the copy: the
   client's contacts, rules, tone, examples and anything else that's theirs.
3. **When you correct a client's copy, ask one question:** "Is this fix for this client
   only, or for every client?"
   - **This client only** (their name, their deadline, their preferences): fix the copy.
   - **Every client** (a better step, a missing check, a clearer template): fix the copy,
     then give the user the change to apply to the master, and list the other client
     Projects that should get it too. You can't reach other Projects yourself.
4. **New client:** copy the current master, not another client's copy, so nothing from one
   client leaks into another.


A chat can only see its own Project, and a computer home is only visible where its folder
is connected. So a playbook needed in two Projects (for example the same client update for
two clients) lives as one full copy in each.

## Copying a playbook to another Project

You can't reach the other Project from here. Instead:

1. Gather every file of the playbook, plus any file it reads from `<home>/shared/`
   (check its `INDEX.md` and the top of each script).
2. Add an "Origin" line at the top of `PLAYBOOK.md` in the copy:
   `Origin: copied from <Project or folder name>, <date>.`
3. Give the user the files to add to the other Project, either as a single download or as
   one file at a time with its path, whichever their app supports.
4. Tell them: in a chat inside the other Project, say "set up my playbooks" if it has no
   `PLAYBOOKS.md` yet, then "add this playbook", and attach or paste the files.

Remove anything specific to the first Project (client names, targets, examples) or flag
it for the user to replace.

## Keeping copies in step

A fix made in one copy doesn't reach the others. When you correct a playbook that has an
Origin line, or that the user says exists elsewhere, end with one line: "This playbook
also lives in <place>. Want the same fix there?" and give them the change to apply.
