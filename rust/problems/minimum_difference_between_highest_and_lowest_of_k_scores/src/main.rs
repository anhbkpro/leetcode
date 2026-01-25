struct Solution;

impl Solution {
    pub fn minimum_difference(mut nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        nums.sort();

        let mut ans = i32::MAX;
        for i in 0..=nums.len() - k {
            ans = ans.min(nums[i + k - 1] - nums[i]);
        }
        ans
    }
}

fn main() {
    let nums = vec![1, 3, 6, 7, 9];
    let k = 3;
    let result = Solution::minimum_difference(nums, k);
    println!("Result: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_case() {
        let nums = vec![9, 4, 1, 7];
        let k = 2;
        assert_eq!(Solution::minimum_difference(nums, k), 2);
    }

    #[test]
    fn test_already_sorted() {
        let nums = vec![1, 2, 3, 4];
        let k = 3;
        assert_eq!(Solution::minimum_difference(nums, k), 2);
    }

    #[test]
    fn test_reverse_sorted() {
        let nums = vec![10, 8, 6, 4, 2];
        let k = 2;
        assert_eq!(Solution::minimum_difference(nums, k), 2);
    }

    #[test]
    fn test_all_same_values() {
        let nums = vec![5, 5, 5, 5];
        let k = 2;
        assert_eq!(Solution::minimum_difference(nums, k), 0);
    }

    #[test]
    fn test_k_equals_1() {
        let nums = vec![100, 200, 300];
        let k = 1;
        // any single element window → diff = 0
        assert_eq!(Solution::minimum_difference(nums, k), 0);
    }

    #[test]
    fn test_k_equals_len() {
        let nums = vec![3, 6, 9];
        let k = 3;
        assert_eq!(Solution::minimum_difference(nums, k), 6);
    }

    #[test]
    fn test_large_numbers() {
        let nums = vec![1_000_000_000, 999_999_998, 999_999_999];
        let k = 2;
        assert_eq!(Solution::minimum_difference(nums, k), 1);
    }

    #[test]
    fn test_single_window_minimum() {
        let nums = vec![1, 5, 6, 14, 15];
        let k = 3;
        assert_eq!(Solution::minimum_difference(nums, k), 5);
    }
}
