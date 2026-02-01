use enums::{Animal, CardinalDirection};

fn main() {
    // Cardinal Direction examples
    let north = CardinalDirection::North;
    let east = CardinalDirection::East;
    let south = CardinalDirection::South;
    let west = CardinalDirection::West;

    fn move_to(direction: CardinalDirection) {
        println!("You are {}!", direction.description());
    }

    move_to(north);
    move_to(east);
    move_to(south);
    move_to(west);

    // Animal examples
    let dog = Animal::Dog(String::from("Rex"));
    let cat = Animal::Cat {
        name: String::from("Whiskers"),
        age: 3,
    };
    let bird = Animal::Bird;

    println!("The name of the dog is: {}", dog.name());
    println!(
        "The name of the cat is: {}, and its age is: {}",
        cat.name(),
        cat.age()
    );
    println!("The name of the bird is: {}", bird.name());
}
