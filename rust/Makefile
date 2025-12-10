.PHONY: test test-one add format lint check install-tools

# Run all tests
test:
	cargo test --all

# Run tests for one problem directory
# Usage: make test-one name=two-sum
test-one:
	cargo test -p $(name)

# Default space
space ?= rust-in-action

# Create a new problem crate
# Usage: make add space=problems name=best-time-to-buy-stock
#    or: make add name=enums   (will go into rust-by-example/)
#    or: make add space=rust-in-action/ch1 name=ch1-cereals
add:
	cargo new $(space)/$(name)

# Makefile for Rust linting & formatting with auto-install

RUSTFMT := $(shell rustup component list --installed | grep rustfmt || true)
CLIPPY := $(shell rustup component list --installed | grep clippy || true)

install-tools:
	@if [ -z "$(RUSTFMT)" ]; then \
		echo "Installing rustfmt..."; \
		rustup component add rustfmt; \
	fi
	@if [ -z "$(CLIPPY)" ]; then \
		echo "Installing clippy..."; \
		rustup component add clippy; \
	fi

CRATES = \
    rust-by-example/constants \
    rust-by-example/enums \
    rust-by-example/ferris_says \
    rust-by-example/first-application \
    rust-by-example/hello-world \
		problems/*

format:
	@for crate in $(CRATES); do \
		if [ -f $$crate/Cargo.toml ]; then \
			echo "Formatting $$crate"; \
			cargo fmt --manifest-path $$crate/Cargo.toml; \
		fi \
	done

lint:
	@for crate in $(CRATES); do \
		if [ -f $$crate/Cargo.toml ]; then \
			echo "Linting $$crate"; \
			cargo clippy --manifest-path $$crate/Cargo.toml -- -D warnings; \
		fi \
	done

check: format lint

