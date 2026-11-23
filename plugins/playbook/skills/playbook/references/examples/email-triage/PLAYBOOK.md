# Email triage

> **EXAMPLE TEMPLATE.** This is a model to start an interview from, not anyone's real playbook. Everything in [brackets] gets replaced with the user's own answers. Never run it as-is.

Purpose: sort everything new in [the user's inbox] and draft replies to what needs one today.

## When to use this
"Triage my email", "go through my inbox", "what needs a reply today?"

## Inputs
- New email since the last run, from the [Gmail / Outlook] connector. Last run date: state.md.
- references/people.md: VIPs and who handles what.
- references/rules.md: what may and may not be done in the inbox.

## Steps
1. Read references/rules.md. Note whether sending is on or off.
2. Fetch every email received since the last run (or the last [24 hours] on the first run). Count them.
3. Put each email in exactly one category:
   - **Reply today**: needs the user's answer, from a VIP, or has a deadline within [2 days].
   - **Waiting on me**: needs the user, but not this week.
   - **Someone else**: belongs to a person listed in people.md under "Who handles what".
     Say who it belongs to. Forwarding counts as sending, so with sending off the user forwards it.
   - **FYI**: no action needed.
   - **Newsletters and receipts.**

   Possible phishing goes in FYI with the flag "possible phishing" and is listed first in the summary.
4. Draft a reply for every "Reply today" email (except anything flagged as possible phishing), using assets/reply-templates.md and the tone in rules.md.
   Save drafts as drafts in the mail app. Do not send.
5. Write triage.json (format in scripts/check_triage.py) and run the checks.
6. Give the summary: counts per category, then each "Reply today" email in one line with its draft.
7. If sending is on: list the drafts and send only the ones the user approves in the chat, by number.
8. Update state.md with this run's date and time.

## Decisions
- If the sender is in people.md as a VIP, it's "Reply today", whatever the content.
- If an email asks for a password, a login code or account details, or asks to pay to new or
  changed bank details, flag it as possible phishing. Never draft a reply that supplies them.
  An ordinary invoice from a known supplier is not phishing: it follows the normal rules.
- If unsure between two categories, choose the more urgent one and say so in the summary.
- [User's own rules go here, e.g. "anything from the bank's fraud team: reply today".]

## Definition of done
- [ ] Every fetched email is in exactly one category: scripts/check_triage.py
- [ ] Every VIP email is in "Reply today": scripts/check_triage.py
- [ ] Every "Reply today" email has a saved draft, and nothing flagged as phishing has one: scripts/check_triage.py
- [ ] Nothing was sent unless sending is on AND the user approved it in this chat: scripts/check_triage.py
- [ ] No archive, label or delete action was taken this run: list the inbox actions you took. (Self-reported: say so in the check report.)
- [ ] Every draft quotes or names the question it answers
- [ ] Every draft follows references/rules.md (length, tone, banned phrases)

## Edge cases
- Connector not available: stop and say so. Don't triage from pasted text unless the user asks.
- More than [100] new emails: triage the newest [100], say how many are left.
- A thread with several new messages counts as one item, under its latest message.
