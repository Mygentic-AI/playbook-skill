#!/usr/bin/env bash
# Validate the skill and build dist/playbook.zip for upload in the Claude app.
set -euo pipefail
cd "$(dirname "$0")"

SKILL=plugins/playbook/skills/playbook
CREATOR=$(ls -d ~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator 2>/dev/null || true)

if [ -n "$CREATOR" ]; then
  (cd "$CREATOR" && python3 -m scripts.quick_validate "$OLDPWD/$SKILL")
else
  echo "skill-creator not found; skipping validation"
fi

rm -rf dist && mkdir -p dist
(cd "$(dirname "$SKILL")" && zip -qr -X "$OLDPWD/dist/playbook.zip" playbook \
  -x '*/.DS_Store' '*/__pycache__/*' '*.pyc')
echo "Built dist/playbook.zip"
unzip -l dist/playbook.zip
