struct Solution;

impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        let n = complexity.len();
        for i in 1..n {
            if complexity[i] <= complexity[0] {
                return 0;
            }
        }

        let mut ans: i64 = 1;
        let mod_val: i64 = 1_000_000_007;
        for i in 2..n {
            ans = (ans * i as i64) % mod_val;
        }
        ans as i32
    }
}

fn main() {
    println!("2360. Count the Number of Computer Unlocking Permutations");
    println!("Input: complexity = [3, 3, 3, 4, 4, 4]");
    println!(
        "Output: {}",
        Solution::count_permutations(vec![3, 3, 3, 4, 4, 4])
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_permutations() {
        assert_eq!(Solution::count_permutations(vec![3, 3, 3, 4, 4, 4]), 0);
    }
}
