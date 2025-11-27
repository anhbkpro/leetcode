const GLOBAL_CONSTANT: i32 = 100_000;

fn main() {
    println!("The global constant is: {}", GLOBAL_CONSTANT);

    const ONE: i32 = 0;
    println!("{}", ONE);
    
    const PI: f32 = 3.14;
    println!("{}", PI);
}
