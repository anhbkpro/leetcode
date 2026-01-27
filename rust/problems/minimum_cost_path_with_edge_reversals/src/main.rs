use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;

        // adjacency list: g[x] = Vec<(y, weight)>
        let mut g = vec![Vec::<(usize, i64)>::new(); n];
        for e in edges {
            let x = e[0] as usize;
            let y = e[1] as usize;
            let w = e[2] as i64;
            g[x].push((y, w));
            g[y].push((x, 2 * w));
        }

        let mut dist = vec![i64::MAX; n];
        let mut visited = vec![false; n];
        dist[0] = 0;

        // Min-heap using Reverse
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0i64, 0usize))); // (distance, node)

        while let Some(Reverse((cur_dist, x))) = heap.pop() {
            if x == n - 1 {
                return cur_dist as i32;
            }

            if visited[x] {
                continue;
            }
            visited[x] = true;

            for &(y, w) in &g[x] {
                let new_dist = cur_dist + w;
                if new_dist < dist[y] {
                    dist[y] = new_dist;
                    heap.push(Reverse((new_dist, y)));
                }
            }
        }

        -1
    }
}

fn main() {
    let n = 4;
    let edges = vec![vec![0, 1, 100], vec![1, 2, 100], vec![2, 3, 100]];
    let result = Solution::min_cost(n, edges);
    println!("Result: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_single_edge() {
        let n = 2;
        let edges = vec![vec![0, 1, 5]];
        // 0 -> 1 cost = 5
        assert_eq!(Solution::min_cost(n, edges), 5);
    }

    #[test]
    fn test_two_paths_choose_min() {
        let n = 3;
        let edges = vec![vec![0, 1, 1], vec![1, 2, 1], vec![0, 2, 5]];
        // Path 0 -> 1 -> 2 = 1 + 1 = 2
        assert_eq!(Solution::min_cost(n, edges), 2);
    }

    #[test]
    fn test_reverse_edge_cost() {
        let n = 3;
        let edges = vec![vec![1, 0, 1], vec![1, 2, 1]];
        // 0 -> 1 costs 2 (reverse edge)
        // 1 -> 2 costs 1
        // total = 3
        assert_eq!(Solution::min_cost(n, edges), 3);
    }

    #[test]
    fn test_unreachable() {
        let n = 3;
        let edges = vec![vec![0, 1, 1]];
        // Node 2 is unreachable
        assert_eq!(Solution::min_cost(n, edges), -1);
    }

    #[test]
    fn test_single_node() {
        let n = 1;
        let edges: Vec<Vec<i32>> = vec![];
        // Start == end
        assert_eq!(Solution::min_cost(n, edges), 0);
    }
}
