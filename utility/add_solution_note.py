#!/usr/bin/env python3
"""
Helper script to add LeetCode solution notes to solution_notes.md files.

Usage:
    # Interactive mode
    python utility/add_solution_note.py

    # From git commit message
    python utility/add_solution_note.py --commit-msg "Add Rust solution for 1975. Maximum Matrix Sum\n\nGreedy approach: sum absolute values, if odd negatives remain,\nsubtract 2 * minimum absolute value"

    # Direct input
    python utility/add_solution_note.py --problem 1975 --name "Maximum Matrix Sum" --note "Greedy approach..." --tag "Greedy, Matrix" --lang rust
"""

import re
import sys
import argparse
from pathlib import Path
from typing import Optional, Tuple

# Get the repository root
REPO_ROOT = Path(__file__).parent.parent
PYTHON_NOTES = REPO_ROOT / "python" / "solution_notes.md"
RUST_NOTES = REPO_ROOT / "rust" / "solution_notes.md"


def parse_commit_message(commit_msg: str) -> Optional[dict]:
    """Parse commit message to extract problem information."""
    lines = commit_msg.strip().split('\n')
    if not lines:
        return None

    # Extract problem number and name from first line
    # Patterns: "Add Rust solution for 1975. Maximum Matrix Sum"
    #           "Solve 1975. Maximum Matrix Sum"
    #           "1975. Maximum Matrix Sum"
    first_line = lines[0]
    match = re.search(r'(\d+)\.\s+(.+?)(?:\s*$|$)', first_line)
    if not match:
        return None

    problem_num = match.group(1)
    problem_name = match.group(2).strip()

    # Detect language
    lang = 'rust' if 'rust' in first_line.lower() else 'python'

    # Extract note from remaining lines
    note = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""

    return {
        'problem_num': problem_num,
        'problem_name': problem_name,
        'note': note,
        'lang': lang
    }


def parse_problem_info(problem_str: str) -> Tuple[str, str]:
    """Parse problem string like '1975. Maximum Matrix Sum' into number and name."""
    match = re.match(r'(\d+)\.\s+(.+)', problem_str)
    if match:
        return match.group(1), match.group(2)
    return "", problem_str


def read_notes_file(filepath: Path) -> list:
    """Read existing notes from markdown file."""
    if not filepath.exists():
        return []

    content = filepath.read_text()
    lines = content.split('\n')

    # Find the table header and data rows
    data_rows = []
    in_table = False

    for line in lines:
        if '| Problem #' in line:
            in_table = True
            continue
        if in_table and line.startswith('|') and '---' not in line:
            # Parse table row
            parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove empty first/last
            if len(parts) >= 2:
                data_rows.append(parts)

    return data_rows


def write_notes_file(filepath: Path, rows: list, lang: str):
    """Write notes to markdown file."""
    header = f"# Solution Notes - {lang.capitalize()}\n\n"
    table_header = "| Problem # | Problem Name | Note | Tag | Difficulty | Time Complexity | Space Complexity |\n"
    table_separator = "|-----------|--------------|------|-----|------------|-----------------|------------------|\n"

    # Sort rows by problem number
    rows.sort(key=lambda x: int(x[0]) if x[0].isdigit() else 999999)

    table_rows = []
    for row in rows:
        # Ensure row has 7 columns
        while len(row) < 7:
            row.append("")
        table_rows.append("| " + " | ".join(row) + " |\n")

    content = header + table_header + table_separator + "".join(table_rows) + "\n"
    filepath.write_text(content)


def sanitize_for_table(text: str) -> str:
    """Sanitize text for markdown table (replace newlines with spaces, escape pipes)."""
    if not text:
        return ""
    # Replace newlines with spaces and clean up multiple spaces
    text = re.sub(r'\s+', ' ', text.replace('\n', ' ').strip())
    # Escape pipe characters (though they shouldn't appear in notes)
    text = text.replace('|', '\\|')
    return text


def add_solution_note(
    problem_num: str,
    problem_name: str,
    note: str,
    tag: str = "",
    difficulty: str = "",
    time_complexity: str = "",
    space_complexity: str = "",
    lang: str = "python"
):
    """Add a solution note to the appropriate markdown file."""
    if lang == "python":
        notes_file = PYTHON_NOTES
    elif lang == "rust":
        notes_file = RUST_NOTES
    else:
        print(f"Error: Unknown language '{lang}'. Use 'python' or 'rust'.")
        return False

    # Sanitize inputs for table format
    problem_name = sanitize_for_table(problem_name)
    note = sanitize_for_table(note)
    tag = sanitize_for_table(tag)
    difficulty = sanitize_for_table(difficulty)
    time_complexity = sanitize_for_table(time_complexity)
    space_complexity = sanitize_for_table(space_complexity)

    # Read existing notes
    rows = read_notes_file(notes_file)

    # Check if problem already exists
    for i, row in enumerate(rows):
        if row[0] == problem_num:
            print(f"Warning: Problem {problem_num} already exists. Updating entry...")
            rows[i] = [problem_num, problem_name, note, tag, difficulty, time_complexity, space_complexity]
            write_notes_file(notes_file, rows, lang)
            print(f"✓ Updated {lang} solution_notes.md")
            return True

    # Add new entry
    new_row = [problem_num, problem_name, note, tag, difficulty, time_complexity, space_complexity]
    rows.append(new_row)
    write_notes_file(notes_file, rows, lang)
    print(f"✓ Added to {lang} solution_notes.md")
    return True


def interactive_mode():
    """Run in interactive mode to collect problem information."""
    print("=== Add LeetCode Solution Note ===\n")

    # Problem number and name
    problem_input = input("Problem (e.g., '1975. Maximum Matrix Sum'): ").strip()
    problem_num, problem_name = parse_problem_info(problem_input)

    if not problem_num:
        problem_num = input("Problem number: ").strip()
    if not problem_name:
        problem_name = input("Problem name: ").strip()

    # Note
    print("\nEnter solution note (press Enter twice to finish):")
    note_lines = []
    while True:
        line = input()
        if not line and note_lines and not note_lines[-1]:
            break
        note_lines.append(line)
    note = "\n".join(note_lines).strip()

    # Tag
    tag = input("\nTag (e.g., 'Greedy, Matrix'): ").strip()

    # Difficulty
    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()

    # Time complexity
    time_complexity = input("Time Complexity (e.g., 'O(n²)'): ").strip()

    # Space complexity
    space_complexity = input("Space Complexity (e.g., 'O(1)'): ").strip()

    # Language
    lang = input("Language (python/rust) [python]: ").strip().lower() or "python"

    # Add the note
    add_solution_note(
        problem_num=problem_num,
        problem_name=problem_name,
        note=note,
        tag=tag,
        difficulty=difficulty,
        time_complexity=time_complexity,
        space_complexity=space_complexity,
        lang=lang
    )


def main():
    parser = argparse.ArgumentParser(
        description="Add LeetCode solution notes to solution_notes.md files"
    )
    parser.add_argument(
        "--commit-msg",
        type=str,
        help="Parse commit message to extract problem info"
    )
    parser.add_argument("--problem", type=str, help="Problem number")
    parser.add_argument("--name", type=str, help="Problem name")
    parser.add_argument("--note", type=str, help="Solution note")
    parser.add_argument("--tag", type=str, default="", help="Tag(s)")
    parser.add_argument("--difficulty", type=str, default="", help="Difficulty")
    parser.add_argument("--time", type=str, default="", help="Time complexity")
    parser.add_argument("--space", type=str, default="", help="Space complexity")
    parser.add_argument("--lang", type=str, default=None, choices=["python", "rust"], help="Language (overrides auto-detection)")

    args = parser.parse_args()

    # Parse from commit message
    if args.commit_msg:
        info = parse_commit_message(args.commit_msg)
        if not info:
            print("Error: Could not parse commit message.")
            sys.exit(1)

        # Use explicitly provided lang, otherwise use detected lang from commit message
        lang = args.lang if args.lang else info['lang']

        add_solution_note(
            problem_num=info['problem_num'],
            problem_name=info['problem_name'],
            note=info['note'],
            tag=args.tag or "",
            difficulty=args.difficulty or "",
            time_complexity=args.time or "",
            space_complexity=args.space or "",
            lang=lang
        )
        return

    # Direct input mode
    if args.problem and args.name:
        add_solution_note(
            problem_num=args.problem,
            problem_name=args.name,
            note=args.note or "",
            tag=args.tag,
            difficulty=args.difficulty,
            time_complexity=args.time,
            space_complexity=args.space,
            lang=args.lang or "python"
        )
        return

    # Interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()

