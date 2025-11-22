fn main() {
    let twenty = 20; // Rust infers a type on your behalf
    let twenty_one: i32 = 21; // add type annotations
    let twenty_two = 22i32; // type suffixes

    let addition = twenty + twenty_one + twenty_two;
    println!("{} + {} + {} = {}", twenty, twenty_one, twenty_two, addition);

    let one_million: i64 = 1_000_000; // underscores increase readability
    println!("{}", one_million.pow(2)); // Numbers have methods

    let forty_two = [ // create an array of numbers, which must all be the same type
        42.0,
        42f32,
        42.0_f32,
    ];
    println!("{:02}", forty_two[0]);
}