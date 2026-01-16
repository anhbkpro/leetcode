use std::collections::HashSet;

struct Solution;

impl Solution {
    fn get_edges(fences: Vec<i32>, border: i32) -> HashSet<i32> {
        let mut points = Vec::with_capacity(fences.len() + 2);
        points.push(1);
        points.extend(fences);
        points.push(border);

        points.sort_unstable();

        let mut edges = HashSet::new();
        let n = points.len();

        for i in 0..n {
            for j in (i + 1)..n {
                edges.insert(points[j] - points[i]);
            }
        }

        edges
    }

    pub fn maximize_square_area(
        m: i32,
        n: i32,
        h_fences: Vec<i32>,
        v_fences: Vec<i32>,
    ) -> i64 {
        const MOD: i64 = 1_000_000_007;

        let h_edges = Self::get_edges(h_fences, m);
        let v_edges = Self::get_edges(v_fences, n);

        let max_edge = h_edges
            .intersection(&v_edges)
            .copied()
            .max()
            .unwrap_or(0);

        if max_edge == 0 {
            -1
        } else {
            let edge = max_edge as i64;
            (edge * edge) % MOD
        }
    }
}

fn main() {
    let m = 5;
    let n = 4;
    let h_fences = vec![1, 2, 3];
    let v_fences = vec![1, 2, 3];
    let result = Solution::maximize_square_area(m, n, h_fences, v_fences);
    println!("Result: {}", result);
}
