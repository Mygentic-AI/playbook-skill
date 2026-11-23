# Example template: email triage

> **EXAMPLE TEMPLATE.** This is a model to start an interview from, not anyone's real playbook. Everything in [brackets] gets replaced with the user's own answers. Never run it as-is.

A worked example of a complete playbook for one of the most common jobs: going through new
email, sorting it, and drafting replies. When a user wants an email-triage playbook, use
this as the starting shape for the interview (`../../interview.md`), then write the user's
own version into their playbook home. Don't copy these files over unchanged.

What it shows:

- **Steps** that sort every new email into one category and draft replies for the urgent ones.
- **A toolbox**: who matters (`references/people.md`), what Claude may do in the inbox
  (`references/rules.md`), reply templates (`assets/`), an approved draft (`references/examples/`).
- **Checks that can fail**, including a script (`scripts/check_triage.py`) that proves every
  email was sorted exactly once, VIPs landed in "reply today", and nothing was sent without approval.
- **Safe defaults**: read and draft only. Sending is off unless the user turns it on, and even
  then only drafts the user has approved in the chat are sent.

## Questions this example adds to the interview

1. Which inbox, through which connector?
2. Who are your VIPs, whose email always needs a reply today? (exact addresses or domains)
3. What belongs to someone else, and who handles it?
4. What makes an email need a reply today, apart from VIPs? Any deadline window?
5. What may I do in your inbox: read, draft, send (only after your approval in the chat), label, archive?
6. Any senders or kinds of email to never reply to?
7. Can you show me a past reply you liked? (it becomes the approved example)
8. How far back should the first run go, and is there a maximum number of emails per run?
9. Is there any mail I should never open (banks, health, legal)? I'll file it by sender
   and subject only.

Before question 2, sample the last two weeks of the inbox read-only and show the user the
senders grouped by kind: it is much easier to name VIPs and categories from a real list.

In this example `references/people.md` replaces the generic template's `data.md`, and
`state.md` holds the last-run date so it isn't buried in the corrections log.

It needs an email connector (Gmail or Outlook) switched on in the Claude app.
