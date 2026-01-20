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

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_basic_cases() {
        let nums = vec![2, 3, 5, 7];
        let result = Solution::min_bitwise_array(nums);
        assert_eq!(result, vec![-1, 1, 4, 3]);
    }

    #[test]
    fn test_even_numbers() {
        let nums = vec![2, 4, 6, 8];
        let result = Solution::min_bitwise_array(nums);
        assert_eq!(result, vec![-1, -1, -1, -1]);
    }

    #[test]
    fn test_mixed_numbers() {
        let nums = vec![10, 11, 12, 13];
        let result = Solution::min_bitwise_array(nums);
        assert_eq!(result, vec![-1, 9, -1, 12]);
    }

    #[test]
    fn test_single_element() {
        let nums = vec![3];
        let result = Solution::min_bitwise_array(nums);
        assert_eq!(result, vec![1]);
    }

    #[test]
    fn test_empty_input() {
        let nums: Vec<i32> = vec![];
        let result = Solution::min_bitwise_array(nums);
        assert!(result.is_empty());
    }

    #[test]
    fn test_large_values() {
        let nums = vec![1023, 1024];
        let result = Solution::min_bitwise_array(nums);
        assert_eq!(result, vec![511, -1]);
    }
}
