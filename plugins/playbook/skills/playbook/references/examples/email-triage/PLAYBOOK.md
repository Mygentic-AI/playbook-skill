# Email triage

> **EXAMPLE TEMPLATE.** This is a model to start an interview from, not anyone's real playbook. Everything in [brackets] gets replaced with the user's own answers. Never run it as-is.

Purpose: sort everything new in [the user's inbox] and draft replies to what needs one today.

## Intent
- What I want: [a clean inbox I'm not afraid to open, where the things that matter don't get lost].
- What I'm afraid of: [missing something that could cause me harm, confusion or problems later:
  a deadline, a payment, a change to an account or a plan, something I'm expected to act on].
- The trade-off: [most email can go unread and nothing bad happens. The rest must reach me.]
- Newsletters: [I don't want to read them, but certain topics matter to me wherever they turn up
  (references/topics.md).]
- Decide on your own when: [it's clearly harmless to leave unread]. Ask me when: [you're not sure
  whether missing it could hurt me].

## When to use this
"Triage my email", "go through my inbox", "what needs a reply today?"

## Inputs
- New email since the last run, from the [Gmail / Outlook] connector. Last run date: state.md.
- references/people.md: VIPs and who handles what.
- references/rules.md: what may and may not be done in the inbox.
- references/topics.md: topics to watch for, in any email or newsletter.

## Steps
1. Read references/rules.md. Note whether sending to other people is on or off.
2. Fetch every email received since a day before the last run (or the last [24 hours] on the first run).
   Drop any id already listed under "Handled ids" in state.md. Count what's left.
3. Put each email in exactly one category:
   - **Reply today**: needs the user's answer, from a VIP, or has a deadline within [2 days].
   - **Waiting on me**: needs the user, but not this week.
   - **Someone else**: belongs to a person listed in people.md under "Who handles what".
     Say who it belongs to. Forwarding counts as sending, so with sending off the user forwards it.
   - **FYI**: no action needed.
   - **Newsletters and receipts.**

   Possible phishing goes in FYI with the flag "possible phishing" and is listed first in the summary.
   **Harm test, for anything headed to FYI or Newsletters:** could not reading this cause the user
   harm, confusion or problems later (a deadline, money, a change to an account, a plan or a
   commitment, something they're expected to act on)? If yes, it goes to Reply today or Waiting on
   me, flagged "could matter later", with one line saying why. If you can't tell, put it in
   "Needs your call".
   **Watched topics:** scan FYI and Newsletters for the topics in references/topics.md. Pull each
   match into the summary as one line (the topic, what it says, which email), so the user doesn't
   have to open the newsletter.
4. Draft a reply for every "Reply today" email (except anything flagged as possible phishing), using assets/reply-templates.md and the tone in rules.md.
   Save drafts as drafts in the mail app. Do not send.
5. Write triage.json (format in scripts/check_triage.py) and run the checks.
6. Give the summary: what needs the user first, then anything flagged "could matter later", then
   watched-topic items, then counts per category, then each "Reply today" email
   in one line with its draft. Email it to the user's own address if rules.md says yes.
7. If sending is on: list the drafts and send only the ones the user approves in the chat, by number.
8. Update state.md: this run's date and time, and this run's ids at the top of "Handled ids".

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
- [ ] Nothing was sent to anyone but the user unless sending is on AND the user approved it in this chat: scripts/check_triage.py
- [ ] The summary email went to the user's own address and nowhere else
- [ ] No label, move, archive or delete action above what rules.md allows: scripts/check_triage.py (from what you record in triage.json, so self-reported: say so in the check report)
- [ ] No email from a "Never read" sender in rules.md was opened: list them by sender and subject only
- [ ] Every draft quotes or names the question it answers
- [ ] Every draft follows references/rules.md (length, tone, banned phrases)

## Reviewer focus
A fresh reviewer (references/review.md in the skill) reads each draft against the email it answers and checks:
does it answer every question asked, does it promise anything the user hasn't agreed to, and does anything
filed as FYI or Newsletters fail the harm test, or mention a watched topic that wasn't pulled out.

## Edge cases
- Connector not available: stop and say so. Don't triage from pasted text unless the user asks.
- More than [100] new emails: triage the newest [100], say how many are left.
- A thread with several new messages counts as one item, under its latest message.
