# LeetCode Rust Workspace

A Rust workspace to solve LeetCode problems.
Each problem lives in its own crate under `problems/`.

## 📁 Project Structure

```
leetcode-rust/
├── Cargo.toml           # Workspace manifest
├── Makefile             # Build and test commands
├── README.md
├── .gitignore
└── problems/
    ├── two-sum/
    │   ├── Cargo.toml
    │   └── src/
    │       ├── lib.rs
    │       └── tests.rs
    └── longest-substring/
        ├── Cargo.toml
        └── src/
            ├── lib.rs
            └── tests.rs
```

---

## 🚀 Getting Started

### Prerequisites

- Rust (install via [rustup](https://rustup.rs))
- Cargo (comes with Rust)
- Optional: `make` for using Makefile commands

Check installation:

```bash
rustc --version
cargo --version
```

---

## 🧰 Commands

### Build

```bash
make build
```

Build all crates in the workspace.

### Run Tests

Run all problem tests:

```bash
make test
```

Run tests for a single problem (example: `two-sum`):

```bash
make test-one name=two-sum
```

---

### Add a New Problem

```bash
make add name=best-time-to-buy-stock
```

This creates a new crate under `problems/` with a `lib.rs` skeleton.

---

### Clean Build Artifacts

```bash
make clean
```

Removes all `target/` directories.

---

### Formatting & Linting

Format code:

```bash
make fmt
```

Lint code using Clippy:

```bash
make lint
```

---

## 📂 Git Ignore

This workspace ignores:

- Cargo build artifacts (`target/`)
- Editor configs (`.vscode/`, `.idea/`)
- OS temp files (`.DS_Store`)
- Logs and temporary files (`*.log`, `*.tmp`, `*~`)

---

## 🧪 Testing

Rust has built-in test support. Each problem crate should have:

- `src/lib.rs` — solution
- `src/tests.rs` — test cases

Example test command:

```bash
cargo test -p two-sum
```

To see test output:

```bash
cargo test -p two-sum -- --nocapture
```

---

## ⚡ Notes

- Each problem crate is independent, but all are under a single workspace.
- Prefix unused variables with `_` to suppress warnings while implementing.

---

## 📄 License

MIT (update as needed)
