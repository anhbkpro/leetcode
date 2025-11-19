# Python
## Alias collections
```bash
cd utility
chmod +x install_aliases.sh
./install_aliases.sh
source ~/.zshrc
```

## Virtual environment

1. Create virtual environment:
```bash
python -m venv venv
```
1. Activate virtual environment:
```bash
source .venv/bin/activate
```
1. Verify activation:
```bash
which python
python --version
pip list
pip install -r requirements.txt
```
1. Deactivate
```bash
deactivate
```

## Run tests
```bash
# Built-in unittest
python3 -m unittest intervals/summary_ranges_test.py -v

# Pytest
pytest intervals/summary_ranges_test.py
pytest intervals/summary_ranges_test.py -v
```

# Golang
This project includes a `Makefile` that provides formatter, linter, and testing utilities for Go development.

## 🔧 Requirements

- Go (version 1.23.0 or higher)

### 🧩 Install Linter

```bash
make install-linter
```

## 🚀 Makefile Commands

### ▶ Format Code

```bash
make fmt
```

### 🧹 Lint Code

```bash
make lint
```

### 🧪 Run Tests

```bash
make test
```

### 🧼 Clean Up

```bash
make clean
```
