struct Solution;

impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut result = Vec::with_capacity(nums.len());

        for &num in &nums {
            let mut candidate = -1;

            for j in 1..num {
                if (j | (j + 1)) == num {
                    candidate = j;
                    break;
                }
            }

            result.push(candidate);
        }

        result
    }
}

fn main() {
    let nums = vec![2, 3, 5];
    let result = Solution::min_bitwise_array(nums);
    println!("{:?}", result); // Output: [-1, 1, 4]
}
