#!/usr/bin/env python3
"""Check a triage run. EXAMPLE TEMPLATE: adapt to the user's own playbook.

Usage: python3 check_triage.py <triage.json>

triage.json, written by Claude during the run:
{
  "sending": "off" | "on after approval",
  "fetched_ids": ["id1", "id2", ...],
  "items": [
    {"id": "id1", "from": "a@b.com", "category": "reply today", "flags": [],
     "drafted": true, "sent": false, "approved_in_chat": false}
  ]
}

Possible phishing goes in "fyi" with "possible phishing" in flags.
VIPs are read from ../references/people.md (any address or @domain in the "VIPs" section),
found relative to this script so it works in a local folder or recreated from a Project.
Exits 1 if any check fails.
"""

import json
import re
import sys
from pathlib import Path

CATEGORIES = {"reply today", "waiting on me", "someone else", "fyi", "newsletters and receipts"}
PEOPLE = Path(__file__).resolve().parent.parent / "references" / "people.md"


def vip_patterns() -> list[str]:
    text = PEOPLE.read_text()
    if "## VIPs" not in text:
        return []
    section = text.split("## VIPs", 1)[1].split("\n## ", 1)[0]
    # Any full address or @domain anywhere in the section, whatever the formatting.
    found = re.findall(r"[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", section)
    return sorted({f.lower() for f in found})


def is_vip(sender: str, patterns: list[str]) -> bool:
    sender = sender.lower()
    return any(sender == p or (p.startswith("@") and sender.endswith(p)) for p in patterns)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 1
    run = json.loads(Path(sys.argv[1]).read_text())
    items = run["items"]
    fetched = run["fetched_ids"]
    failures = []

    ids = [i["id"] for i in items]
    missing = sorted(set(fetched) - set(ids))
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    extra = sorted(set(ids) - set(fetched))
    bad_cat = [i["id"] for i in items if i["category"].lower() not in CATEGORIES]
    if missing or dupes or extra or bad_cat:
        failures.append(f"sorted once: missing={missing} duplicated={dupes} not-fetched={extra} bad-category={bad_cat}")
    print(f"Sorted once: {len(fetched)} fetched, {len(set(ids))} sorted -> {'FAIL' if failures else 'PASS'}")

    vips = vip_patterns()
    if not vips:
        failures.append("no VIP addresses found in references/people.md")
        print("VIPs in reply today: FAIL (no VIPs found in people.md)")
    misplaced = [i["id"] for i in items if is_vip(i["from"], vips) and i["category"].lower() != "reply today"]
    if vips:
        print(f"VIPs in reply today: {'FAIL ' + str(misplaced) if misplaced else 'PASS'}")
    if misplaced:
        failures.append(f"VIP not in reply today: {misplaced}")

    no_draft = [i["id"] for i in items if i["category"].lower() == "reply today"
                and not i.get("drafted") and "possible phishing" not in i.get("flags", [])]
    phish_drafted = [i["id"] for i in items if "possible phishing" in i.get("flags", []) and i.get("drafted")]
    ok = not no_draft and not phish_drafted
    print(f"Drafts: {'PASS' if ok else f'FAIL reply-today without draft={no_draft} phishing drafted={phish_drafted}'}")
    if not ok:
        failures.append(f"drafts: missing={no_draft} phishing={phish_drafted}")

    sending_on = run.get("sending", "off").lower().startswith("on")
    bad_sends = [i["id"] for i in items if i.get("sent") and not (sending_on and i.get("approved_in_chat"))]
    print(f"No unapproved sends: {'FAIL ' + str(bad_sends) if bad_sends else 'PASS'}")
    if bad_sends:
        failures.append(f"sent without approval: {bad_sends}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
