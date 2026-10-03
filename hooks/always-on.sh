#!/usr/bin/env sh
# SessionStart hook: loads the i-have-dyslexia rules, and the person's own
# profile, at the start of every session.
#
# It only fires for someone who ran `/i-have-dyslexia setup`, which writes
# the profile below. Someone who installed the plugin only for the thinking
# strategies never gets the reading rules forced on them.
#
# Never blocks a session: any failure exits 0 and prints nothing.
#
# Pattern from i-have-adhd (github.com/ayghri/i-have-adhd).

claude_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
profile="$claude_dir/i-have-dyslexia/profile.md"
[ -f "$profile" ] || exit 0

script_dir=$(dirname -- "$0")
skill="$script_dir/../skills/i-have-dyslexia/SKILL.md"
[ -f "$skill" ] || exit 0

# SKILL.md without its YAML frontmatter.
body=$(awk 'NR == 1 && /^---/ { fm = 1; next } fm && /^---/ { fm = 0; next } !fm' "$skill") || exit 0

printf '%s\n\n' "I-HAVE-DYSLEXIA IS ON (always-on). The person set it up, so the rules below apply to every answer in this session. \"stop dyslexia mode\" turns it off for this session. Deleting $profile turns always-on off for good."
printf '%s\n\n' "## This person's profile (their own words beat the general rules)"
cat "$profile"
printf '\n\n%s\n\n%s\n' "## The skill" "$body"
exit 0
