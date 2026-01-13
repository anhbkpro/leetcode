struct Solution;

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut max_y: f64 = 0.0;
        let mut total_area: f64 = 0.0;

        // Precompute total area and max y
        for sq in &squares {
            let y = sq[1] as f64;
            let l = sq[2] as f64;
            total_area += l * l;
            max_y = max_y.max(y + l);
        }

        // Check if area below limit_y >= half of total area
        let check = |limit_y: f64| -> bool {
            let mut area = 0.0;
            for sq in &squares {
                let y = sq[1] as f64;
                let l = sq[2] as f64;

                if y < limit_y {
                    let height = (limit_y - y).min(l);
                    area += l * height;
                }
            }
            area >= total_area / 2.0
        };

        let mut lo = 0.0;
        let mut hi = max_y;
        let eps = 1e-5;

        while (hi - lo).abs() > eps {
            let mid = (lo + hi) / 2.0;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        hi
    }
}

fn main() {
    let squares = vec![vec![0, 0, 1], vec![1, 0, 1], vec![1, 1, 1]];
    let result = Solution::separate_squares(squares);
    println!("Result: {}", result);
}
