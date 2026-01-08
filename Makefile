APP_NAME := leetcode
GOLANGCI_VERSION := v1.62.2

.PHONY: all fmt lint test cover tidy verify build run clean install-linter venv venv-activate venv-install venv-shell

all: fmt lint test

## Install golangci-lint if not installed
install-linter:
	@echo "👉 Installing golangci-lint $(GOLANGCI_VERSION)..."
	@curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh \
	  | sh -s -- -b $$(go env GOPATH)/bin $(GOLANGCI_VERSION)
	@echo "✅ golangci-lint installed at $$(go env GOPATH)/bin/golangci-lint"

## Format code
fmt:
	@echo "👉 Running go fmt..."
	@go fmt ./...

## Lint using golangci-lint
lint:
	@echo "👉 Running golangci-lint..."
	@golangci-lint run --timeout=5m

## Run tests
test:
	@echo "👉 Running tests..."
	@go test ./... -cover

## Test with coverage file
cover:
	@echo "👉 Generating coverage.out..."
	@go test ./... -coverprofile=coverage.out

## go mod tidy / verify
tidy:
	@go mod tidy

verify:
	@go mod verify

## Build binary
build:
	@echo "👉 Building $(APP_NAME)..."
	@go build -o bin/$(APP_NAME) .

run: build
	@echo "👉 Running $(APP_NAME)..."
	@./bin/$(APP_NAME)

clean:
	@echo "👉 Cleaning..."
	@rm -rf bin coverage.out

## Create Python virtual environment
venv:
	@echo "👉 Creating Python virtual environment..."
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
		echo "✅ Virtual environment created at .venv"; \
	else \
		echo "✅ Virtual environment already exists at .venv"; \
	fi

## Show activation command for virtual environment
venv-activate:
	@echo "👉 To activate the virtual environment, run:"
	@echo "   source .venv/bin/activate"
	@echo ""
	@echo "Or on Windows:"
	@echo "   .venv\Scripts\activate"
	@echo ""
	@echo "Or use: eval \"\$$(make venv-shell)\" to activate in current shell"

## Generate shell activation command (use with eval)
venv-shell:
	@echo "source .venv/bin/activate"

## Install Python dependencies
venv-install: venv
	@echo "👉 Installing Python dependencies..."
	@.venv/bin/pip install --upgrade pip
	@if [ -f "requirements.txt" ]; then \
		.venv/bin/pip install -r requirements.txt; \
		echo "✅ Dependencies installed from requirements.txt"; \
	else \
		echo "⚠️  No requirements.txt found"; \
	fi
