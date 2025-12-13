use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.into_iter().collect();
        let mut longest = 0;

        for &num in &set {
            // Only start counting if num is the start of a sequence
            if !set.contains(&(num - 1)) {
                let mut current = num;
                let mut length = 1;

                while set.contains(&(current + 1)) {
                    current += 1;
                    length += 1;
                }

                longest = longest.max(length);
            }
        }

        longest
    }
}

fn main() {
    println!("2381. Longest Consecutive Sequence");
    println!("Input: nums = [100, 4, 200, 1, 3, 2]");
    println!(
        "Output: {}",
        Solution::longest_consecutive(vec![100, 4, 200, 1, 3, 2])
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_longest_consecutive() {
        assert_eq!(Solution::longest_consecutive(vec![100, 4, 200, 1, 3, 2]), 4);
    }
}
