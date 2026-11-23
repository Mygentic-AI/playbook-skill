# Weekly client update

Purpose: a short Monday email telling one ad client how last week went against plan.

## When to use this
Monday update to an ad client about last week's spend and results vs plan.

## Inputs
- Last week's numbers — <home>/inputs/last-week.csv (export from the ads dashboard)
- Plan targets, client names, contact first names — references/data.md
- What we're changing this week — ask the user if leads are below plan

## Steps
1. Read last week's row for the client from the CSV.
2. Compare spend and leads to plan in references/data.md.
3. Fill assets/update-template.md.
4. Open with the number that moved most.

## Decisions
- If leads are below plan, lead with what we're changing, then the number.

## Definition of done
- [ ] Every actual figure appears in last-week.csv; every plan figure appears in references/data.md
- [ ] Under 200 words — scripts/check_word_count.py
- [ ] No adjective without a number next to it
- [ ] Rules in references/rules.md followed

## Edge cases
- Missing row for the client → stop and ask.
