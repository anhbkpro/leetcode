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

    pub fn max_matrix_sum_functional_style(matrix: Vec<Vec<i32>>) -> i64 {
        let (sum, min_abs, neg_count) =
            matrix
                .into_iter()
                .flatten()
                .fold((0i64, i64::MAX, 0i64), |(sum, min_abs, neg), v| {
                    let abs = (v as i64).abs();
                    (sum + abs, min_abs.min(abs), neg + if v < 0 { 1 } else { 0 })
                });

        if neg_count % 2 == 0 {
            sum
        } else {
            sum - 2 * min_abs
        }
    }
}

fn main() {
    let matrix: Vec<Vec<i32>> = vec![vec![1, 2, 3], vec![-4, -5, -6], vec![7, 8, 9]];
    let result: i64 = Solution::max_matrix_sum(matrix);
    println!("Result: {}", result);

    let matrix = vec![vec![1, 2, 3], vec![-4, -5, -6], vec![7, 8, 9]];
    let result_functional: i64 = Solution::max_matrix_sum_functional_style(matrix);
    println!("Result functional: {}", result_functional);
}
