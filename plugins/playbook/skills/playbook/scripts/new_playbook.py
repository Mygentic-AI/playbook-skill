#!/usr/bin/env python3
"""Create a new playbook folder in a local playbook home.

Usage: python3 new_playbook.py <home> <job-name>

Copies assets/playbook-template/ to <home>/playbooks/<job-name>/ and creates
<home>/PLAYBOOKS.md from assets/PLAYBOOKS.md if it doesn't exist yet.
Local homes only: in a Claude Project, write the template files one by one.
"""

import re
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "assets" / "playbook-template"
INDEX_TEMPLATE = SKILL_DIR / "assets" / "PLAYBOOKS.md"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 1

    home = Path(sys.argv[1]).expanduser().resolve()
    name = sys.argv[2].strip()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        print(f"Job name must be kebab-case, e.g. weekly-client-update (got: {name!r})")
        return 1
    if not home.is_dir():
        print(f"Playbook home not found: {home}")
        return 1

    target = home / "playbooks" / name
    if target.exists():
        print(f"A playbook called {name} already exists: {target}")
        return 1

    shutil.copytree(TEMPLATE, target)
    print(f"Created {target}")

    index = home / "PLAYBOOKS.md"
    if not index.exists():
        shutil.copyfile(INDEX_TEMPLATE, index)
        print(f"Created {index}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
