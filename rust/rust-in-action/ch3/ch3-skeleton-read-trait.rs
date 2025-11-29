#![allow(unused_variables)]

#[derive(Debug)]
struct File;

trait Read { // Provides a specific name for the trait
  fn read(self: &Self, save_to: &mut Vec<u8>) -> Result<usize, String>;
}

impl Read for File { // Implements the Read trait for the File struct
  fn read(self: &File, save_to: &mut Vec<u8>) -> Result<usize, String> {
      Ok(0) // Dummy implementation
  }
}

fn main() {
    let f = File{};
    let mut buffer: Vec<u8> = vec![];

    let f_length = f.read(&mut buffer).unwrap();

    println!("Read {} bytes from file {:?}", f_length, f);
}
