# Hello World in Rust

This is a simple "Hello, World!" program written in Rust.

```rust
fn main() {
    println!("Hello, World!");
}
```

To run this program, save it to a file named `hello.rs` and use the Rust compiler:

```bash
rustc hello.rs
./hello
```
## If we name main a different name, we will get an error like below:

```text
error[E0601]: `main` function not found in crate `hello`
 --> hello.rs:3:2
  |
3 | }
  |  ^ consider adding a `main` function to `hello.rs`

error: aborting due to 1 previous error

For more information about this error, try `rustc --explain E0601`.
```
