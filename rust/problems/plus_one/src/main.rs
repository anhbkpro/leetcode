struct Solution;

impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let n = digits.len();

        // Move from the end of the array
        for i in 0..n {
            let idx = n - 1 - i;

            if digits[idx] == 9 {
                digits[idx] = 0;
            } else {
                digits[idx] += 1;
                return digits;
            }
        }

        // All digits were 9
        let mut result = Vec::with_capacity(n + 1);
        result.push(1);
        result.extend(digits);
        result
    }
}

fn main() {
    println!("{:?}", Solution::plus_one(vec![1, 2, 3]));
}
