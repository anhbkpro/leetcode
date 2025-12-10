use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut num_cnt: HashMap<i32, i32> = HashMap::new();
        let mut num_partial_cnt: HashMap<i32, i32> = HashMap::new();

        for &v in &nums {
            *num_cnt.entry(v).or_insert(0) += 1;
        }

        let mut ans: i64 = 0;
        for v in nums {
            let target = v * 2;
            let l_cnt = *num_partial_cnt.get(&target).unwrap_or(&0);
            *num_partial_cnt.entry(v).or_insert(0) += 1;
            let total_cnt = *num_cnt.get(&target).unwrap_or(&0);
            let partial_cnt = *num_partial_cnt.get(&target).unwrap_or(&0);
            let r_cnt = total_cnt - partial_cnt;
            ans = (ans + l_cnt as i64 * r_cnt as i64) % MOD;
        }

        ans as i32
    }
}

fn main() {
    println!("1550. Count Special Triplets");
    println!("Input: nums = [6, 3, 6]");
    println!("Output: {}", Solution::special_triplets(vec![6, 3, 6]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_special_triplets() {
        assert_eq!(Solution::special_triplets(vec![6, 3, 6]), 1);
        assert_eq!(Solution::special_triplets(vec![8, 4, 2, 8, 4]), 2);
    }
}
