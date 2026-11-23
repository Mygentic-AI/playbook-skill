# Saving what worked: the toolbox

When a run went well, freeze the reusable parts so the next run starts from them instead
of rebuilding them.

## Look for code first

Ask "which step was mechanical?" before "which output was good?". Pulling numbers,
reformatting a file, counting words, checking a link: these belong in `scripts/`. If the
same helper was written on two runs, that is the signal to save it as a script.

## What goes where

| Kind | Folder | Examples |
|---|---|---|
| Scripts for mechanical steps and checks | `scripts/` | `pull_numbers.py`, `check_word_count.py` |
| Rules | `references/rules.md` | tone, formatting, banned words |
| Reference data | `references/data.md` (or one file per topic) | client names, prices, targets, links, account IDs |
| Approved examples | `references/examples/` | a past output the user praised |
| Templates copied into the output | `assets/` | `update-template.md`, email templates with `[placeholders]` |
| Prompts for a sub-step | `references/` | a saved prompt for summarising a call |

Templates use `[square-bracket placeholders]`. Save one filled-in example next to each
template so the next run sees what "filled in well" looks like.

## What never goes in

- Passwords, API keys, tokens, private keys.
- One-off outputs nobody will reuse.
- Drafts the user hasn't approved.

The test: would you hand it to a new hire on their first day?

## How to save

1. Give the file a descriptive name with no dates or version numbers
   (`late-invoice-email-stage-2.md`, not `email-v3-final.md`). Exception: approved
   examples in `references/examples/` may start with their date.
2. Add a line to `references/INDEX.md`: file, what it's for, when to use it, when not to,
   date added.
3. Point to it from the step in `PLAYBOOK.md` that uses it.
4. If a file now overlaps an older one, merge them. One file per purpose.
5. Tell the user what you saved and where, in one line each.

Once a month, or when the user asks, review the toolbox: delete files the index shows
nobody has used, and merge near-duplicates.
