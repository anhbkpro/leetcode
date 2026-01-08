use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut memo: HashMap<(usize, usize), i64> = HashMap::new();
        const NEG_INF: i64 = i64::MIN / 4; // a safe sentinel (avoid potential overflow if added)

        fn dp(
            i: usize,
            j: usize,
            nums1: &Vec<i32>,
            nums2: &Vec<i32>,
            memo: &mut HashMap<(usize, usize), i64>,
        ) -> i64 {
            if i == nums1.len() || j == nums2.len() {
                return NEG_INF;
            }

            if let Some(&v) = memo.get(&(i, j)) {
                return v;
            }

            let take = nums1[i] as i64 * nums2[j] as i64;

            // continue_val is dp(i+1, j+1)
            let cont = dp(i + 1, j + 1, nums1, nums2, memo);
            // only add cont if cont is not NEG_INF (otherwise that branch is invalid)
            let take_and_continue = if cont == NEG_INF {
                NEG_INF
            } else {
                // safe to add because both are i64 and cont != NEG_INF
                take.saturating_add(cont)
            };

            let take_only = take;
            let skip_i = dp(i + 1, j, nums1, nums2, memo);
            let skip_j = dp(i, j + 1, nums1, nums2, memo);

            let res = *[take_and_continue, take_only, skip_i, skip_j]
                .iter()
                .max()
                .unwrap();

            memo.insert((i, j), res);
            res
        }

        // compute answer and cast to i32 (LeetCode returns i32)
        let ans = dp(0, 0, &nums1, &nums2, &mut memo);
        ans as i32
    }
}

fn main() {
    let nums1 = vec![2, 1, -2, 5];
    let nums2 = vec![3, 0, -6];
    let result = Solution::max_dot_product(nums1, nums2);
    println!("Result: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_single_positive() {
        let nums1 = vec![5];
        let nums2 = vec![4];
        assert_eq!(Solution::max_dot_product(nums1, nums2), 20);
    }

    #[test]
    fn test_single_negative_and_positive() {
        // Must pick at least one pair
        let nums1 = vec![-1];
        let nums2 = vec![1];
        assert_eq!(Solution::max_dot_product(nums1, nums2), -1);
    }

    #[test]
    fn test_all_negative() {
        // Best is to pick the least negative product
        let nums1 = vec![-1, -2];
        let nums2 = vec![-3, -4];
        // Pick (-1) * (-3) + (-2) * (-4) = 3 + 8 = 11
        assert_eq!(Solution::max_dot_product(nums1, nums2), 11);
    }

    #[test]
    fn test_all_positive() {
        let nums1 = vec![1, 2, 3];
        let nums2 = vec![4, 5, 6];
        // Full subsequence gives max
        // 1*4 + 2*5 + 3*6 = 32
        assert_eq!(Solution::max_dot_product(nums1, nums2), 32);
    }

    #[test]
    fn test_mixed_signs() {
        let nums1 = vec![3, -2];
        let nums2 = vec![2, -6];
        // Best: 3*2 + (-2)*(-6) = 6 + 12 = 18
        assert_eq!(Solution::max_dot_product(nums1, nums2), 18);
    }

    #[test]
    fn test_non_empty_enforced() {
        let nums1 = vec![-5, -1];
        let nums2 = vec![2, 3];
        // Must choose at least one pair → -1*2 = -2
        assert_eq!(Solution::max_dot_product(nums1, nums2), -2);
    }
}
