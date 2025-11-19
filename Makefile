APP_NAME := leetcode
GOLANGCI_VERSION := v1.62.2

.PHONY: all fmt lint test cover tidy verify build run clean install-linter

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
