use rand::prelude::*;

fn one_in(denominator: u32) -> bool{
    thread_rng().gen_ratio(1, denominator)
}

#[derive(Debug)]
struct File {
    name: String,
    data: Vec<u8>,
}

impl File {
    fn new(name: &str) -> File
    {
        File {
            name: String::from(name),
            data: Vec::new(),
        }
    }

    fn new_with_data(name: &str, data: &Vec<u8>) -> File {
        let mut f = File::new(name);
        f.data = data.clone();
        f
    }

    fn read(self: &File, save_to: &mut Vec<u8>) -> Result<usize, String> {
        let mut tmp = self.data.clone();
        let len = tmp.len();
        save_to.reserve(len);
        save_to.append(&mut tmp);
        Ok(len) // In this code, read() never fails, but we still wrap read_length in Ok because we’re returning Result.
    }
}

fn open(f: File) -> Result<File, String> {
    if one_in(2) {
        let err_msg = String::from("Not enough data to open file!");
        return Err(err_msg);
    }
    Ok(f)
}

fn close(f: File) -> Result<File, String> {
    if one_in(2) {
        let err_msg = String::from("Interupted by signal!");
        return Err(err_msg);
    }
    Ok(f)
}

fn main() {
    let f4_data = vec![65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75];
    let mut f4 = File::new_with_data("f4.txt", &f4_data);

    let mut buffer: Vec<u8> = Vec::new();
    f4 = open(f4).unwrap();
    let f4_length = f4.read(&mut buffer).unwrap();
    f4 = close(f4).unwrap();

    let text = String::from_utf8_lossy(&buffer);

    println!("{:?}", f4.name);
    println!("{} is {} bytes long!", f4.name, f4_length);
    println!("{}", text);
}