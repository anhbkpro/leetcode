struct Solution;

impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        // Sort in descending order
        happiness.sort_by(|a, b| b.cmp(a));

        let mut total_happiness_sum: i64 = 0;
        let mut turns: i32 = 0;

        for i in 0..k as usize {
            let adjusted = happiness[i] - turns;
            if adjusted > 0 {
                total_happiness_sum += adjusted as i64;
            }
            turns += 1;
        }

        total_happiness_sum
    }

    pub fn maximum_happiness_sum_v2(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_unstable_by(|a, b| b.cmp(a));

        (0..k as usize)
            .map(|i| (happiness[i] - i as i32).max(0) as i64)
            .sum()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_case() {
        let happiness = vec![1, 2, 3];
        let k = 2;
        assert_eq!(Solution::maximum_happiness_sum(happiness, k), 4);
        // picks 3 + (2 - 1) = 4
    }

    #[test]
    fn test_all_positive() {
        let happiness = vec![10, 9, 8, 7];
        let k = 3;
        assert_eq!(Solution::maximum_happiness_sum(happiness, k), 24);
        // 10 + (9-1) + (8-2) = 24
    }

    #[test]
    fn test_zero_result() {
        let happiness = vec![1, 1, 1];
        let k = 3;
        assert_eq!(Solution::maximum_happiness_sum(happiness, k), 1);
        // 1 + 0 + 0
    }

    #[test]
    fn test_single_element() {
        let happiness = vec![5];
        let k = 1;
        assert_eq!(Solution::maximum_happiness_sum(happiness, k), 5);
    }

    #[test]
    fn test_large_values() {
        let happiness = vec![1_000_000_000, 1_000_000_000];
        let k = 2;
        assert_eq!(Solution::maximum_happiness_sum(happiness, k), 1_999_999_999);
    }

    #[test]
    fn test_k_equals_zero() {
        let happiness = vec![5, 4, 3];
        let k = 0;
        assert_eq!(Solution::maximum_happiness_sum(happiness, k), 0);
    }

    #[test]
    fn test_basic_case_v2() {
        let happiness = vec![1, 2, 3];
        let k = 2;
        assert_eq!(Solution::maximum_happiness_sum_v2(happiness, k), 4);
        // picks 3 + (2 - 1) = 4
    }
}

fn main() {
    let happiness = vec![5, 3, 8, 6];
    let k = 3;
    let result = Solution::maximum_happiness_sum(happiness, k);
    println!("Maximum happiness sum for selected children: {}", result);
}
