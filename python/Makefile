PYTHON := python3
VENV := .venv
SRC := .

.PHONY: all venv install fmt lint check fix test clean

all: check

## ----------------------
## Virtual environment
## ----------------------

venv:
	@echo "👉 Creating virtualenv..."
	@$(PYTHON) -m venv $(VENV)

install: venv
	@echo "👉 Installing dependencies..."
	@$(VENV)/bin/pip install --upgrade pip
	@$(VENV)/bin/pip install ruff pytest

## ----------------------
## Ruff
## ----------------------

## Format code (ruff format)
fmt:
	@echo "👉 Formatting Python code with ruff..."
	@$(VENV)/bin/ruff format $(SRC)

## Lint only (no auto-fix)
lint:
	@echo "👉 Linting Python code with ruff..."
	@$(VENV)/bin/ruff check $(SRC)

## Lint + auto-fix (recommended for local dev)
fix:
	@echo "👉 Auto-fixing Python code with ruff..."
	@$(VENV)/bin/ruff check --fix $(SRC)

## CI target (fail on any issue)
check:
	@$(VENV)/bin/ruff format --check $(SRC)
	@$(VENV)/bin/ruff check $(SRC)

## ----------------------
## Testing
## ----------------------

test:
	@echo "👉 Running Python tests..."
	@$(VENV)/bin/pytest

## ----------------------
## Cleanup
## ----------------------

clean:
	@echo "👉 Cleaning Python environment..."
	@rm -rf $(VENV) .pytest_cache __pycache__
