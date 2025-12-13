use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut last_seen: HashMap<char, usize> = HashMap::new();
        let mut left: usize = 0;
        let mut longest: usize = 0;

        for (right, ch) in s.chars().enumerate() {
            if let Some(&prev) = last_seen.get(&ch) {
                // move left pointer only forward
                left = left.max(prev + 1);
            }

            last_seen.insert(ch, right);
            longest = longest.max(right - left + 1);
        }

        longest as i32
    }
}

fn main() {
    println!("2381. Longest Substring Without Repeating Characters");
    println!("Input: s = \"abcabcbb\"");
    println!(
        "Output: {}",
        Solution::length_of_longest_substring("abcabcbb".to_string())
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_length_of_longest_substring() {
        assert_eq!(
            Solution::length_of_longest_substring("abcabcbb".to_string()),
            3
        );
    }
}
