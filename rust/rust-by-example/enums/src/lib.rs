pub enum CardinalDirection {
    North,
    East,
    South,
    West,
}

impl CardinalDirection {
    pub fn description(&self) -> &str {
        match self {
            CardinalDirection::North => "heading North",
            CardinalDirection::East => "heading East",
            CardinalDirection::South => "heading South",
            CardinalDirection::West => "heading West",
        }
    }
}

pub enum Animal {
    Dog(String),
    Cat { name: String, age: u8 },
    Bird,
}

impl Animal {
    pub fn name(&self) -> String {
        match self {
            Animal::Dog(name) => name.clone(),
            Animal::Cat { name, .. } => name.clone(),
            Animal::Bird => String::from("Bird"),
        }
    }

    pub fn age(&self) -> u8 {
        match self {
            Animal::Cat { age, .. } => *age,
            _ => 0,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_cardinal_direction_description() {
        let north = CardinalDirection::North;
        let east = CardinalDirection::East;
        let south = CardinalDirection::South;
        let west = CardinalDirection::West;

        assert_eq!(north.description(), "heading North");
        assert_eq!(east.description(), "heading East");
        assert_eq!(south.description(), "heading South");
        assert_eq!(west.description(), "heading West");
    }

    #[test]
    fn test_animal_dog_name() {
        let dog = Animal::Dog(String::from("Rex"));
        assert_eq!(dog.name(), "Rex");
    }

    #[test]
    fn test_animal_dog_age() {
        let dog = Animal::Dog(String::from("Rex"));
        assert_eq!(dog.age(), 0);
    }

    #[test]
    fn test_animal_cat_name() {
        let cat = Animal::Cat {
            name: String::from("Whiskers"),
            age: 3,
        };
        assert_eq!(cat.name(), "Whiskers");
    }

    #[test]
    fn test_animal_cat_age() {
        let cat = Animal::Cat {
            name: String::from("Whiskers"),
            age: 3,
        };
        assert_eq!(cat.age(), 3);
    }

    #[test]
    fn test_animal_bird_name() {
        let bird = Animal::Bird;
        assert_eq!(bird.name(), "Bird");
    }

    #[test]
    fn test_animal_bird_age() {
        let bird = Animal::Bird;
        assert_eq!(bird.age(), 0);
    }

    #[test]
    fn test_animal_cat_with_different_ages() {
        let young_cat = Animal::Cat {
            name: String::from("Kitten"),
            age: 1,
        };
        let old_cat = Animal::Cat {
            name: String::from("Senior"),
            age: 15,
        };
        
        assert_eq!(young_cat.age(), 1);
        assert_eq!(old_cat.age(), 15);
    }
}
