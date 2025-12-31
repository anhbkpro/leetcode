struct DSU {
    root: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        DSU {
            root: (0..n).collect(),
            size: vec![1; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.root[x] != x {
            let parent = self.find(self.root[x]);
            self.root[x] = parent;
        }
        self.root[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut root_x = self.find(x);
        let mut root_y = self.find(y);

        if root_x == root_y {
            return;
        }

        // Union by size
        if self.size[root_x] > self.size[root_y] {
            std::mem::swap(&mut root_x, &mut root_y);
        }

        self.root[root_x] = root_y;
        self.size[root_y] += self.size[root_x];
    }
}

struct Solution;

impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let row = row as usize;
        let col = col as usize;

        // +2 for left virtual node (0) and right virtual node (row*col + 1)
        let mut dsu = DSU::new(row * col + 2);
        let mut grid = vec![vec![0; col]; row];

        let directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ];

        for i in 0..row * col {
            let r = (cells[i][0] - 1) as isize;
            let c = (cells[i][1] - 1) as isize;

            grid[r as usize][c as usize] = 1;

            let index_1 = r as usize * col + c as usize + 1;

            for (dr, dc) in directions.iter() {
                let new_r = r + dr;
                let new_c = c + dc;

                if new_r >= 0
                    && new_r < row as isize
                    && new_c >= 0
                    && new_c < col as isize
                    && grid[new_r as usize][new_c as usize] == 1
                {
                    let index_2 = new_r as usize * col + new_c as usize + 1;
                    dsu.union(index_1, index_2);
                }
            }

            // Connect to left virtual node
            if c == 0 {
                dsu.union(0, index_1);
            }

            // Connect to right virtual node
            if c == col as isize - 1 {
                dsu.union(row * col + 1, index_1);
            }

            if dsu.find(0) == dsu.find(row * col + 1) {
                return i as i32;
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
