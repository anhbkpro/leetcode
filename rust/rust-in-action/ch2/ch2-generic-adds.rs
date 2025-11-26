use std::ops::{Add};
use std::time::{Duration};

fn add<T: Add<Output = T>>(i: T, j: T) -> T {
    i + j
}

fn main() {
  let float_sum = add(1.2, 3.4);
  let int_sum = add(10, 20);
  let duration_sum = add(Duration::new(5, 0), Duration::new(10, 0));

  println!("{}", float_sum);
  println!("{}", int_sum);
  println!("{}", duration_sum.as_secs());
}
