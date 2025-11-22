fn main() {
    let fruit = vec!["apple", "oranges", "banana"];
    let buffer_overflow = fruit[4];
    assert_eq!(buffer_overflow, "watermelon");
}