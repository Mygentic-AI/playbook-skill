# Testing in the Claude app

Paste these into the app after uploading `dist/playbook.zip`. Start a **new chat** where it
says so: what matters is that results survive the chat.

## A. First run, Project home

In a new Project called "Playbook Trial", new chat:

```
Set up my playbooks. I want to use them on my phone too.
```

✅ Explains playbooks in a few lines; says files will be stored in this Project; writes
`PLAYBOOKS.md` and reads it back; gives a Project instructions block to paste; asks for a
first job; interviews ONE question at a time, at least eight, before writing.

## B. First run, outside any Project, no folder

New chat outside any Project, no folder connected:

```
Set up my playbooks.
```

✅ Asks the storage question, then gives numbered steps to create the Project or folder
yourself, ends with a kickoff message in one copy-paste block for the new chat, and does
not write a playbook anywhere.

Paste that kickoff message into a new chat in the Project (or with the folder connected).

✅ It does not repeat the explanation or the storage question; it checks it can save and
starts the interview.

```
Do my weekly client update.
```

✅ Says it can't see your playbooks in this chat and what to do. Does not do the job from
scratch.

## C. First run, computer home

Create an empty `~/Playbooks` folder. New chat, connect only that folder:

```
Set up my playbooks. Everything must stay on my computer.
```

✅ Writes `PLAYBOOKS.md` into `~/Playbooks`; never asks for Documents or your home folder.

## D. Run a playbook (after A or C)

New chat in the same home:

```
Do my <job name>.
```

✅ Finds it in `PLAYBOOKS.md`; follows the steps; reports every check as pass/fail with
evidence; ends with the two questions (anything wrong? keep anything?).

## E. Correction sticks

In the same chat, correct something specific:

```
That's wrong: <the mistake>. Fix it for good.
```

✅ Names which part failed (steps, toolbox, script, checks); changes the playbook's files;
adds one line to the top of `notes.md`; reruns and shows before/after.

New chat:

```
Show me the playbook's notes.md and the part of PLAYBOOK.md you changed last time.
```

✅ The fix is there.

## F. Save a script (Project home)

```
That run was right. Save the mechanical step as a script.
```

New chat:

```
Do my <job name> again, and tell me whether you used a saved script or wrote a new one.
```

✅ Uses the saved script unchanged (copied into its workspace to run).

## G. List

```
What playbooks do I have?
```

✅ Lists each with its "when to use" line.

## H. Copy to another Project

```
I need this playbook in my other Project too.
```

✅ Adds an Origin line, gives you the files to add there, flags client-specific details.

## I. Email triage from the example template

Gmail or Outlook connector switched on. In a Project or with your Playbooks folder connected:

```
Make me an email triage playbook.
```

✅ Says it's starting from the example template; asks first what a clean inbox would give you and what
you're afraid of missing (the intent), then what mail it must never open,
before reading anything; boldly recommends labelling and a summary email to your own
address (no warnings about sending) and does each only after your yes; asks about your VIPs, categories and what
it may do in the inbox, one question at a time; the files it writes have no "EXAMPLE
TEMPLATE" banner and no [brackets] left; sending is off unless you said otherwise.

Then:

```
Triage my email.
```

✅ Anything that could cause you trouble later is flagged "could matter later" even if it looked like FYI;
watched topics from newsletters appear as one-line items; every new email in one category, drafts saved as drafts, a summary email in your own inbox, check report shows sorted-once,
VIPs and no-send as PASS, and nothing was sent, labelled, archived or deleted.

## J. Schedule a playbook (after D and E)

```
That run was right. Make it run on its own every weekday at 8am.
```

✅ Adds a one-line "Job:" at the top of the playbook; creates a scheduled task; tells you the conditions for unattended runs; asks where you
already look and who checks the output until when; records the schedule in
`PLAYBOOKS.md` as "not yet verified".

Wait for the first scheduled run.

✅ It ran without you, found the playbook, and didn't redo items an earlier run handled.

## K. Independent review (after D)

Plant a mistake in the playbook's source material the checks can't catch (for example, an email that asks two
questions). Then:

```
Do my <job name>.
```

✅ After the checks, a reviewer looks at the output and says whether it was a sub-agent or a self-review pass.
The run ends with two lists. "Fixed, and the playbook updated" holds only things that broke a rule you already
wrote, each with what changed and where. "Needs your call" holds anything that could go either way, each with a
suggested rule; nothing in `rules.md` changes until you answer.

## L. Asking by phrase (Project home, after the instructions block is pasted)

New chat in the Project, using one of the playbook's "asked for with" phrases, not its name:

```
Anything urgent in my inbox?
```

✅ Runs the email-triage playbook (says so), rather than triaging from scratch with the connector.
After adding a second playbook, Claude hands you a complete updated instructions block with one
line per playbook.
