.PHONY: test test-one add

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

