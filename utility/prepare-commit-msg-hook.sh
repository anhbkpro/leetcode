#!/bin/bash
# Git prepare-commit-msg hook to automatically add solution notes
#
# To install:
#   cp utility/prepare-commit-msg-hook.sh .git/hooks/prepare-commit-msg
#   chmod +x .git/hooks/prepare-commit-msg

# Get the commit message file
COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2

# Only process if it's a normal commit (not merge, amend, etc.)
if [ "$COMMIT_SOURCE" != "message" ] && [ "$COMMIT_SOURCE" != "" ]; then
    exit 0
fi

# Read the commit message
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Check if this looks like a LeetCode solution commit
if echo "$COMMIT_MSG" | grep -qiE "(leetcode|problem \d+|solution for \d+|\d+\.\s+[A-Z])"; then
    # Run the script to add solution note
    REPO_ROOT="$(git rev-parse --show-toplevel)"
    python3 "$REPO_ROOT/utility/add_solution_note.py" --commit-msg "$COMMIT_MSG"
fi

exit 0

