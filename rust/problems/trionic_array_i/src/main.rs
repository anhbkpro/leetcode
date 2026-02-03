struct Solution;

impl Solution {
    pub fn is_trionic(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if nums[0] >= nums[1] {
            return false;
        }
        let mut count = 1;
        for i in 2..n {
            if nums[i - 1] == nums[i] {
                return false;
            }
            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0 {
                count += 1;
            }
        }
        count == 3
    }
}

fn main() {
    let nums = vec![1, 3, 5, 4, 2, 6];
    let result = Solution::is_trionic(nums);
    println!("result = {}", result);
}
