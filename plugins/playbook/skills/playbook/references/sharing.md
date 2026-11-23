# Using a playbook in more than one place

A chat can only see its own Project, and a computer home is only visible where its folder
is connected. So a playbook needed in two Projects (for example the same client update for
two clients) lives as one full copy in each.

## Copying a playbook to another Project

You can't reach the other Project from here. Instead:

1. Gather every file of the playbook.
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
