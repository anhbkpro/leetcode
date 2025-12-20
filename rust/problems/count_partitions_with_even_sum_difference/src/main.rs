struct Solution;

impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let total_sum: i32 = nums.iter().sum();
        if total_sum % 2 == 0 {
            nums.len() as i32 - 1
        } else {
            0
        }
    }
}

fn main() {
    let result = Solution::count_partitions(vec![2, 5, 3, 4, 2]);
    println!("result = {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_even_sum() {
        // nums = [2, 4], total_sum = 6 (even) → n-1 = 1
        assert_eq!(Solution::count_partitions(vec![2, 4]), 1);
    }

    #[test]
    fn test_odd_sum() {
        // nums = [1, 2, 3], total_sum = 6 (even) → n-1 = 2
        assert_eq!(Solution::count_partitions(vec![1, 2, 3]), 2);
    }

    #[test]
    fn test_odd_total_sum() {
        // nums = [1, 2], total_sum = 3 (odd) → 0
        assert_eq!(Solution::count_partitions(vec![1, 2]), 0);
    }

    #[test]
    fn test_single_even_element() {
        // nums = [4], total_sum = 4 (even) → n-1 = 0
        assert_eq!(Solution::count_partitions(vec![4]), 0);
    }

    #[test]
    fn test_single_odd_element() {
        // nums = [3], total_sum = 3 (odd) → 0
        assert_eq!(Solution::count_partitions(vec![3]), 0);
    }

    #[test]
    fn test_all_zeros() {
        // nums = [0, 0, 0], total_sum = 0 (even) → n-1 = 2
        assert_eq!(Solution::count_partitions(vec![0, 0, 0]), 2);
    }

    #[test]
    fn test_larger_array_even_sum() {
        // nums = [1, 1, 2, 2], total_sum = 6 (even) → n-1 = 3
        assert_eq!(Solution::count_partitions(vec![1, 1, 2, 2]), 3);
    }

    #[test]
    fn test_larger_array_odd_sum() {
        // nums = [1, 1, 1], total_sum = 3 (odd) → 0
        assert_eq!(Solution::count_partitions(vec![1, 1, 1]), 0);
    }
}
