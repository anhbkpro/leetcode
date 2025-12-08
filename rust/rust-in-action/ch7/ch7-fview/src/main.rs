use std::fs::File;
use std::io::prelude::*;
use std::env;

const BYTES_PER_LINE: usize = 16;

fn main() {
    let arg1 = env::args().nth(1); // get the first argument (Optional<String>)

    let fname = arg1.expect("usage: fview FILENAME");

    let mut f = File::open(fname).expect("could not open file"); // expect is a friendlier version of unwrap() that prints a message
    let mut pos = 0;
    let mut buffer = [0; BYTES_PER_LINE];

    while let Ok(_) = f.read_exact(&mut buffer) { // read until read_exact() returns an error
        print!("[0x{:08x}] ", pos);
        for byte in &buffer {
            match *byte {
                0x00 => print!(". "),
                0xff => print!("## "),
                _ => print!("{:02x} ", byte),
            }
        }
        println!();
        pos += BYTES_PER_LINE;
    }
}
