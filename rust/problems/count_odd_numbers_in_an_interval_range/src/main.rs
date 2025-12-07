struct Solution;

impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        (high + (high & 1) - low + (low & 1)) >> 1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_both_odd() {
        // [3, 7] → 3, 5, 7 → 3 odds
        assert_eq!(Solution::count_odds(3, 7), 3);
    }

    #[test]
    fn test_both_even() {
        // [8, 10] → 9 → 1 odd
        assert_eq!(Solution::count_odds(8, 10), 1);
    }

    #[test]
    fn test_single_odd() {
        // [1, 1] → 1 → 1 odd
        assert_eq!(Solution::count_odds(1, 1), 1);
    }

    #[test]
    fn test_single_even() {
        // [2, 2] → no odds → 0
        assert_eq!(Solution::count_odds(2, 2), 0);
    }

    #[test]
    fn test_range_1_to_10() {
        // [1, 10] → 1, 3, 5, 7, 9 → 5 odds
        assert_eq!(Solution::count_odds(1, 10), 5);
    }

    #[test]
    fn test_zero() {
        // [0, 0] → no odds → 0
        assert_eq!(Solution::count_odds(0, 0), 0);
    }

    #[test]
    fn test_zero_to_one() {
        // [0, 1] → 1 → 1 odd
        assert_eq!(Solution::count_odds(0, 1), 1);
    }

    #[test]
    fn test_large_range() {
        // [1, 100] → 50 odds
        assert_eq!(Solution::count_odds(1, 100), 50);
    }
}
