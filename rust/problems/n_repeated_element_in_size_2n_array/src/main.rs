struct Solution;

impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        for i in 0..nums.len() - 1 {
            if nums[i] == nums[i + 1] {
                return nums[i];
            }
            if i + 2 < nums.len() && nums[i] == nums[i + 2] {
                return nums[i];
            }
            if i + 3 < nums.len() && nums[i] == nums[i + 3] {
                return nums[i];
            }
        }
        unreachable!()
    }
}

fn main() {
    println!("{}", Solution::repeated_n_times(vec![1, 2, 3, 3]));
}
