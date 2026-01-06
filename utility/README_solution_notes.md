# Solution Notes Automation

This utility helps automatically maintain `solution_notes.md` files for Python and Rust LeetCode solutions.

## Files

- `add_solution_note.py` - Main script to add/update solution notes
- `prepare-commit-msg-hook.sh` - Git hook to automatically run on commits
- `python/solution_notes.md` - Python solutions notes
- `rust/solution_notes.md` - Rust solutions notes

## Usage

### Method 1: Interactive Mode (Recommended)

```bash
python utility/add_solution_note.py
```

This will prompt you for:

- Problem number and name
- Solution note
- Tag(s)
- Difficulty
- Time complexity
- Space complexity
- Language (python/rust)

### Method 2: From Commit Message

```bash
python utility/add_solution_note.py --commit-msg "$(cat .git/COMMIT_EDITMSG)"
```

The script will parse commit messages like:

- "Add Rust solution for 1975. Maximum Matrix Sum"
- "Solve 1975. Maximum Matrix Sum"
- "1975. Maximum Matrix Sum"

### Method 3: Direct Input

```bash
python utility/add_solution_note.py \
    --problem 1975 \
    --name "Maximum Matrix Sum" \
    --note "Greedy approach: sum absolute values..." \
    --tag "Greedy, Matrix" \
    --difficulty "Medium" \
    --time "O(n²)" \
    --space "O(1)" \
    --lang rust
```

## Git Hook Setup (Automatic)

To automatically add notes when you commit:

1. Install the git hook:

```bash
cp utility/prepare-commit-msg-hook.sh .git/hooks/prepare-commit-msg
chmod +x .git/hooks/prepare-commit-msg
```

1. Commit as usual with a message like:

```bash
git commit -m "Add Rust solution for 1975. Maximum Matrix Sum

Greedy approach: sum absolute values, if odd negatives remain,
subtract 2 * minimum absolute value"
```

The hook will automatically detect LeetCode solution commits and add them to the notes.

## Commit Message Format

The script recognizes these patterns:

- `Add Rust solution for 1975. Maximum Matrix Sum`
- `Add Python solution for 1975. Maximum Matrix Sum`
- `Solve 1975. Maximum Matrix Sum`
- `1975. Maximum Matrix Sum`

The note is extracted from the commit message body (lines after the first).

## Manual Updates

If you need to update an existing entry, just run the script again with the same problem number - it will update the existing entry.

## Example

```bash
# Interactive
$ python utility/add_solution_note.py
=== Add LeetCode Solution Note ===

Problem (e.g., '1975. Maximum Matrix Sum'): 1975. Maximum Matrix Sum
Enter solution note (press Enter twice to finish):
Greedy approach: sum absolute values, if odd negatives remain,
subtract 2 * minimum absolute value

Tag (e.g., 'Greedy, Matrix'): Greedy, Matrix
Difficulty (Easy/Medium/Hard): Medium
Time Complexity (e.g., 'O(n²)'): O(n²)
Space Complexity (e.g., 'O(1)'): O(1)
Language (python/rust) [python]: rust
✓ Added to rust solution_notes.md
```
