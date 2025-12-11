struct Solution;

impl Solution {
    pub fn count_covered_buildings(n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut max_row = vec![0; n_usize + 1];
        let mut min_row = vec![n + 1; n_usize + 1];
        let mut max_col = vec![0; n_usize + 1];
        let mut min_col = vec![n + 1; n_usize + 1];

        for p in &buildings {
            let x = p[0] as usize;
            let y = p[1] as usize;

            max_row[y] = max_row[y].max(x as i32);
            min_row[y] = min_row[y].min(x as i32);
            max_col[x] = max_col[x].max(y as i32);
            min_col[x] = min_col[x].min(y as i32);
        }

        let mut res = 0;
        for p in &buildings {
            let x = p[0] as usize;
            let y = p[1] as usize;

            if (x as i32) > min_row[y]
                && (x as i32) < max_row[y]
                && (y as i32) > min_col[x]
                && (y as i32) < max_col[x]
            {
                res += 1;
            }
        }

        res
    }
}

fn main() {
    println!("2381. Count Covered Buildings");
    println!("Input: n = 5, buildings = [[1, 2], [2, 3], [3, 4], [4, 5]]");
    println!(
        "Output: {}",
        Solution::count_covered_buildings(5, vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![4, 5]])
    );
}

#[cfg(test)]
mod tests {
    use std::vec;

    use super::*;

    #[test]
    fn test_count_covered_buildings() {
        assert_eq!(
            Solution::count_covered_buildings(
                5,
                vec![vec![1, 2], vec![2, 2], vec![3, 2], vec![2, 1], vec![2, 3]]
            ),
            1
        );
    }
}
