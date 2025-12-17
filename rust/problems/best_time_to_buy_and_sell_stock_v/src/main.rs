struct Solution;

impl Solution {
    pub fn maximum_profit(prices: Vec<i32>, k: i32) -> i64 {
        let n = prices.len();
        let k = k as usize;
        let mut dp = vec![vec![0_i64; 3]; k + 1];
        for j in 1..=k {
            dp[j][1] = -(prices[0] as i64);
            dp[j][2] = prices[0] as i64;
        }

        for i in 1..n {
            for j in (1..=k).rev() {
                dp[j][0] = dp[j][0]
                    .max(dp[j][1] + prices[i] as i64)
                    .max(dp[j][2] - prices[i] as i64);
                dp[j][1] = dp[j][1].max(dp[j - 1][0] - prices[i] as i64);
                dp[j][2] = dp[j][2].max(dp[j - 1][0] + prices[i] as i64);
            }
        }

        dp[k][0]
    }
}

fn main() {
    let prices = vec![1, 2, 3, 4, 5];
    let k = 2;
    let result = Solution::maximum_profit(prices, k);
    println!("Maximum profit: {}", result);
}
