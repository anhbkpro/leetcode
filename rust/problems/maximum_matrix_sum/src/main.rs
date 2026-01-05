struct Solution;

impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut matrix_sum: i64 = 0;
        let mut min_abs_val: i64 = i64::MAX;
        let mut negative_count: i32 = 0;

        for row in matrix {
            for val in row {
                let abs_val = (val as i64).abs();
                matrix_sum += abs_val;

                if val < 0 {
                    negative_count += 1;
                }

                min_abs_val = min_abs_val.min(abs_val);
            }
        }

        if negative_count % 2 != 0 {
            matrix_sum -= 2 * min_abs_val;
        }

        matrix_sum
    }
}

fn main() {
    let matrix: Vec<Vec<i32>> = vec![vec![1, 2, 3], vec![-4, -5, -6], vec![7, 8, 9]];
    let result: i64 = Solution::max_matrix_sum(matrix);
    println!("Result: {}", result);
}
