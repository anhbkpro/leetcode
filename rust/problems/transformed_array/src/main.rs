struct Solution;

impl Solution {
    pub fn construct_transformed_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        nums.iter()
            .enumerate()
            .map(|(i, &num)| nums[((i as i32 + num) % n as i32 + n as i32) as usize % n])
            .collect()
    }
}

fn main() {
    let nums = vec![1, 2, 3, 4, 5];
    let result = Solution::construct_transformed_array(nums);
    println!("{:?}", result);
}
