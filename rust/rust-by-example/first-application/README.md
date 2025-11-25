# How to create your first Rust application
This guide will help you set up your first Rust application using Cargo, Rust's package manager and build system.
## Step 1: Install Rust and Cargo
If you haven't already, install Rust and Cargo by following the instructions at [rustup.rs](
https://rustup.rs). This will install both Rust and Cargo on your system.
## Step 2: Create a New Cargo Project
Open your terminal and run the following command to create a new Cargo project named `first_application`:
```bash
cargo new first_application
```
This command creates a new directory called `first_application` with the following structure:
```first_application/
├── Cargo.toml
└── src/
    └── main.rs
```
- Cargo.toml: This file contains metadata about your project (such as name, version, and authors) and its dependencies.
- src/: This directory contains your Rust source code.
    - main.rs: This is the main source file for your application.
## Step 3: Navigate to the Project Directory
Change into the newly created project directory:
```bash
cd first_application
```
## Step 4: Write Your First Rust Program
Open the `src/main.rs` file in your favorite text editor and replace its contents with the following code:
```rust
fn main() {
    println!("Hello, World!");
}
```

## Step 5: Build and Run the Application
To build and run your Rust application, use the following command in your terminal:
```bash
cargo run
```
You should see the output:
```text
Hello, World!
```

Congratulations! You've successfully created and run your first Rust application using Cargo.
