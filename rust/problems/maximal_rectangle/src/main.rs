struct Solution;

impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }

        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut max_area = 0;

        // dp[r][c] = number of consecutive '1's ending at (r, c) in the row
        let mut dp = vec![vec![0; cols]; rows];

        for r in 0..rows {
            for c in 0..cols {
                if matrix[r][c] == '0' {
                    continue;
                }

                // compute width ending at (r, c)
                dp[r][c] = if c == 0 { 1 } else { dp[r][c - 1] + 1 };
                let mut width = dp[r][c];

                // scan upward to compute max rectangle with bottom-right corner at (r, c)
                for k in (0..=r).rev() {
                    width = width.min(dp[k][c]);
                    let height = r - k + 1;
                    max_area = max_area.max(width * height);
                }
            }
        }

        max_area as i32
    }
}

fn main() {
    let matrix = vec![
        vec!['1', '0', '1', '0', '0'],
        vec!['1', '0', '1', '1', '1'],
        vec!['1', '1', '1', '1', '1'],
        vec!['1', '0', '0', '1', '0'],
    ];
    let result = Solution::maximal_rectangle(matrix);
    println!("Result: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn to_matrix(rows: Vec<&str>) -> Vec<Vec<char>> {
        rows.into_iter().map(|r| r.chars().collect()).collect()
    }

    #[test]
    fn test_empty_matrix() {
        let matrix: Vec<Vec<char>> = vec![];
        assert_eq!(Solution::maximal_rectangle(matrix), 0);
    }

    #[test]
    fn test_single_zero() {
        let matrix = to_matrix(vec!["0"]);
        assert_eq!(Solution::maximal_rectangle(matrix), 0);
    }

    #[test]
    fn test_single_one() {
        let matrix = to_matrix(vec!["1"]);
        assert_eq!(Solution::maximal_rectangle(matrix), 1);
    }

    #[test]
    fn test_single_row() {
        let matrix = to_matrix(vec!["10111"]);
        // Largest rectangle: "111" → area = 3
        assert_eq!(Solution::maximal_rectangle(matrix), 3);
    }

    #[test]
    fn test_single_column() {
        let matrix = to_matrix(vec!["1", "1", "0", "1"]);
        // Two consecutive '1's → area = 2
        assert_eq!(Solution::maximal_rectangle(matrix), 2);
    }

    #[test]
    fn test_all_zeros() {
        let matrix = to_matrix(vec!["000", "000", "000"]);
        assert_eq!(Solution::maximal_rectangle(matrix), 0);
    }

    #[test]
    fn test_all_ones() {
        let matrix = to_matrix(vec!["111", "111", "111"]);
        // Full matrix → 3 x 3 = 9
        assert_eq!(Solution::maximal_rectangle(matrix), 9);
    }

    #[test]
    fn test_leetcode_example() {
        let matrix = to_matrix(vec!["10100", "10111", "11111", "10010"]);
        // Expected answer from LeetCode
        assert_eq!(Solution::maximal_rectangle(matrix), 6);
    }

    #[test]
    fn test_irregular_rectangles() {
        let matrix = to_matrix(vec!["1101", "1101", "1111"]);
        // Best rectangle: rows 0..2, cols 0..1 → 3 x 2 = 6
        assert_eq!(Solution::maximal_rectangle(matrix), 6);
    }

    #[test]
    fn test_checkerboard() {
        let matrix = to_matrix(vec!["1010", "0101", "1010"]);
        // No rectangle larger than 1
        assert_eq!(Solution::maximal_rectangle(matrix), 1);
    }
}
