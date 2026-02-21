struct Solution;

impl Solution {
    pub fn count_prime_set_bits(l: i32, r: i32) -> i32 {
        // Max set bits for 32-bit integer is 32,
        // but within constraints (like LeetCode 762) 20 is enough.
        let primes = [2, 3, 5, 7, 11, 13, 17, 19];

        let mut count = 0;

        for x in l..=r {
            let bits = x.count_ones() as i32;
            if primes.contains(&bits) {
                count += 1;
            }
        }

        count
    }
}

fn main() {
    println!("2044. Prime Number of Set Bits in Binary Representation");
    println!("Input: l = 6, r = 10");
    println!("Output: {}", Solution::count_prime_set_bits(6, 10));
}
