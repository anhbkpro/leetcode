use std::cmp;

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut buy = i32::MAX;
        let mut res = 0;
        for i in 0..prices.len() {
            if prices[i] < buy {
                buy = prices[i];
            } else {
                res = cmp::max(res, prices[i] - buy);
            }
        }

        return res;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_profit() {
        assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
        assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
    }
}
