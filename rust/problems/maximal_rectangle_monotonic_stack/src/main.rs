struct Solution;

impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }

        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut heights = vec![0; cols];
        let mut max_area = 0;

        for r in 0..rows {
            // Build histogram
            for c in 0..cols {
                if matrix[r][c] == '1' {
                    heights[c] += 1;
                } else {
                    heights[c] = 0;
                }
            }

            // Largest rectangle in histogram
            max_area = max_area.max(Self::largest_rectangle(&heights));
        }

        max_area
    }

    fn largest_rectangle(heights: &Vec<i32>) -> i32 {
        let mut stack: Vec<usize> = Vec::new();
        let mut max_area = 0;
        let mut extended = heights.clone();
        extended.push(0); // sentinel

        for i in 0..extended.len() {
            while let Some(&top) = stack.last() {
                if extended[i] < extended[top] {
                    stack.pop();
                    let height = extended[top];
                    let width = if let Some(&left) = stack.last() {
                        (i - left - 1) as i32
                    } else {
                        i as i32
                    };
                    max_area = max_area.max(height * width);
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        max_area
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
