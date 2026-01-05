# Commitlint Guide

This project uses [commitlint](https://commitlint.js.org/) to enforce consistent commit message formats.

## Commit Message Format

Commit messages must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `build`: Build system changes
- `ci`: CI/CD changes

### Examples

**Valid:**
```
feat: add solution notes automation utility

Script to automatically maintain solution_notes.md files for Python and Rust
LeetCode solutions with git hook support
```

```
fix: correct language detection in commit message parser
```

```
docs: update README with commitlint usage
```

```
feat(rust): add solution for 1975. Maximum Matrix Sum

Greedy approach: sum absolute values, if odd negatives remain,
subtract 2 * minimum absolute value
```

**Invalid:**
```
Add solution notes automation utility  ❌ (missing type)
```

```
feat:Add solution notes  ❌ (missing space after colon)
```

```
feat: add  ❌ (subject too short)
```

## Rules

- **Type is required**: Must be one of the allowed types
- **Subject is required**: Cannot be empty
- **No period**: Subject should not end with a period
- **Case**: Subject should be lowercase (except for proper nouns)
- **Length**: Header should not exceed 100 characters
- **Body**: Body should be separated by a blank line from the header

## LeetCode Solution Commits

For LeetCode solutions, use this format:

```
feat(<lang>): add solution for <problem-number>. <problem-name>

<solution-note>
```

Example:
```
feat(rust): add solution for 1975. Maximum Matrix Sum

Greedy approach: sum absolute values, if odd negatives remain,
subtract 2 * minimum absolute value
```

## Bypassing Commitlint

If you need to bypass commitlint (not recommended), use:

```bash
git commit --no-verify -m "your message"
```

## Testing Commit Messages

Test a commit message before committing:

```bash
echo "your commit message" | npx commitlint
```

## Configuration

The configuration is in `commitlint.config.js` and extends the conventional config with custom rules.

