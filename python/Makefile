PYTHON := python3
VENV := .venv
SRC := .

.PHONY: all venv install fmt lint test clean

all: fmt lint test

## ----------------------
## Virtual environment
## ----------------------

venv:
	@echo "👉 Creating virtualenv..."
	@$(PYTHON) -m venv $(VENV)

install: venv
	@echo "👉 Installing dependencies..."
	@$(VENV)/bin/pip install --upgrade pip
	@$(VENV)/bin/pip install black isort flake8 pytest

## ----------------------
## Formatting
## ----------------------

fmt:
	@echo "👉 Formatting Python code..."
	@$(VENV)/bin/isort $(SRC)
	@$(VENV)/bin/black $(SRC)

## ----------------------
## Linting
## ----------------------

lint:
	@echo "👉 Linting Python code..."
	@$(VENV)/bin/flake8 $(SRC)

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
