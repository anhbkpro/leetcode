#![allow(unused_variables)]

type File = String; // Creates a type alias. The compiler won’t distinguish between String & File, but your source code will.

fn open(f: &mut File) -> bool{
    true // Let’s assume for the moment that these two functions always succeed.
}

fn close(f: &mut File) -> bool{
    true // Let’s assume for the moment that these two functions always succeed.
}

#[allow(dead_code)]
fn read(f: &mut File, save_to: &mut Vec<u8>) -> ! { // The ! return type indicates to the Rust compiler that the function never returns.
    unimplemented!(); // This crashes the program
}

fn main() {
    let mut f = File::from("f1.txt"); // File inherits all of String’s methods.
    open(&mut f);
    // read(&mut f, save_to);
    close(&mut f);
}
