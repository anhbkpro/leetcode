use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() {
  let f = File::open("readme.md").unwrap(); // panicked here if file not found
  let mut reader = BufReader::new(f);

  let mut line = String::new();

  loop {
    let bytes_read = reader.read_line(&mut line).unwrap();
    if bytes_read == 0 {
      break;
    }

    println!("{} ({} bytes long)", line.trim_end(), bytes_read);

    line.truncate(0); // Clear the string for the next line
  }
}
