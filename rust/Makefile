.PHONY: test test-one add

# Run all tests
test:
	cargo test --all

# Run tests for one problem directory
# Usage: make test-one name=two-sum
test-one:
	cargo test -p $(name)

# Create a new problem crate
# Usage: make add name=best-time-to-buy-stock
add:
	cargo new problems/$(name) --lib
