struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut rx = self.find(x);
        let mut ry = self.find(y);

        if rx == ry {
            return;
        }

        if self.size[rx] > self.size[ry] {
            std::mem::swap(&mut rx, &mut ry);
        }

        self.parent[rx] = ry;
        self.size[ry] += self.size[rx];
    }
}

struct Solution;

impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let row = row as usize;
        let col = col as usize;
        let n = row * col;

        let top = 0;
        let bottom = n + 1;

        let mut dsu = DSU::new(n + 2);
        let mut grid = vec![vec![0; col]; row];

        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];

        // Iterate days in reverse
        for day in (0..cells.len()).rev() {
            let r = (cells[day][0] - 1) as usize;
            let c = (cells[day][1] - 1) as usize;

            grid[r][c] = 1;
            let idx = r * col + c + 1;

            // Connect to neighbors
            for (dr, dc) in directions {
                let nr = r as isize + dr;
                let nc = c as isize + dc;

                if nr >= 0
                    && nr < row as isize
                    && nc >= 0
                    && nc < col as isize
                    && grid[nr as usize][nc as usize] == 1
                {
                    let nidx = nr as usize * col + nc as usize + 1;
                    dsu.union(idx, nidx);
                }
            }

            // Connect to top / bottom virtual nodes
            if r == 0 {
                dsu.union(idx, top);
            }
            if r == row - 1 {
                dsu.union(idx, bottom);
            }

            // Check connectivity
            if dsu.find(top) == dsu.find(bottom) {
                return day as i32;
            }
        }

        0
    }
}

fn main() {
    println!("1970. Last Day Where You Can Still Cross");
    println!("Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]");
    println!(
        "Output: {}",
        Solution::latest_day_to_cross(2, 2, vec![vec![1, 1], vec![2, 1], vec![1, 2], vec![2, 2]])
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        // LeetCode example
        let row = 2;
        let col = 2;
        let cells = vec![vec![1, 1], vec![2, 1], vec![1, 2], vec![2, 2]];
        assert_eq!(Solution::latest_day_to_cross(row, col, cells), 2);
    }

    #[test]
    fn example_2() {
        let row = 2;
        let col = 2;
        let cells = vec![vec![1, 1], vec![1, 2], vec![2, 1], vec![2, 2]];
        assert_eq!(Solution::latest_day_to_cross(row, col, cells), 1);
    }

    #[test]
    fn single_column() {
        let row = 3;
        let col = 1;
        let cells = vec![vec![1, 1], vec![2, 1], vec![3, 1]];
        // Can cross until the cell in the column is fully blocked
        assert_eq!(Solution::latest_day_to_cross(row, col, cells), 0);
    }

    #[test]
    fn single_row() {
        let row = 1;
        let col = 3;
        let cells = vec![vec![1, 1], vec![1, 2], vec![1, 3]];
        // One row is always crossable until fully flooded
        assert_eq!(Solution::latest_day_to_cross(row, col, cells), 2);
    }

    #[test]
    fn minimal_grid() {
        let row = 1;
        let col = 1;
        let cells = vec![vec![1, 1]];
        assert_eq!(Solution::latest_day_to_cross(row, col, cells), 0);
    }

    #[test]
    fn zigzag_path() {
        let row = 3;
        let col = 3;
        let cells = vec![
            vec![1, 1],
            vec![2, 3],
            vec![3, 1],
            vec![1, 2],
            vec![2, 2],
            vec![3, 2],
            vec![1, 3],
            vec![2, 1],
            vec![3, 3],
        ];
        assert_eq!(Solution::latest_day_to_cross(row, col, cells), 3);
    }
}
