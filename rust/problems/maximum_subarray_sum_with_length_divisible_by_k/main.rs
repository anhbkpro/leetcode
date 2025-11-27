struct Solution;

pub fn main() {
  let solution = Solution;
  let nums = vec![2, -1, 3, 4, -2, 1, 5, -3];
  let k = 3;
  let result = solution.max_subarray_sum(nums, k);
  println!("Maximum subarray sum with length divisible by {}: {}", k, result);
}

impl Solution {
    pub fn max_subarray_sum(self, nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut prefix_sum: i64 = 0;
        let mut max_sum = i64::MIN;
        let mut k_sum = vec![i64::MAX / 2; k];
        k_sum[k - 1] = 0;

        for (i, &num) in nums.iter().enumerate() {
            prefix_sum += num as i64;
            max_sum = max_sum.max(prefix_sum - k_sum[i % k]);
            k_sum[i % k] = k_sum[i % k].min(prefix_sum);
        }

        max_sum
    }
}
