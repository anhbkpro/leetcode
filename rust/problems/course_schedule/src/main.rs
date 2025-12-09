struct Solution;


impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let n = num_courses as usize;

        // adjacency list
        let mut graph = vec![Vec::new(); n];

        // indegree of each node
        let mut indegree = vec![0; n];

        // Build graph
        for pair in prerequisites {
            let course = pair[0] as usize;
            let prereq = pair[1] as usize;

            graph[prereq].push(course);
            indegree[course] += 1;
        }

        // Queue of all courses with no prerequisites
        let mut queue = std::collections::VecDeque::new();
        for i in 0..n {
            if indegree[i] == 0 {
                queue.push_back(i);
            }
        }

        // Count of processed nodes
        let mut taken = 0;

        while let Some(cur) = queue.pop_front() {
            taken += 1;

            // Reduce indegree of neighbors
            for &next in &graph[cur] {
                indegree[next] -= 1;
                if indegree[next] == 0 {
                    queue.push_back(next);
                }
            }
        }

        // If we processed all courses → no cycle
        taken == n
    }
}


fn main() {
    println!("207. Course Schedule");
    println!("Input: num_courses = 2, prerequisites = [[1, 0]]");
    println!("Output: {}", Solution::can_finish(2, vec![vec![1, 0]]));
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_can_finish_basic() {
        // Simple valid dependency
        assert_eq!(Solution::can_finish(2, vec![vec![1, 0]]), true);
    }

    #[test]
    fn test_cycle_simple() {
        // Simple cycle 0 → 1 → 0
        assert_eq!(Solution::can_finish(2, vec![vec![1, 0], vec![0, 1]]), false);
    }

    #[test]
    fn test_multiple_prerequisites() {
        // 0 → 1 → 2 → 3
        // No cycle
        assert_eq!(
            Solution::can_finish(
                4,
                vec![
                    vec![1, 0],
                    vec![2, 1],
                    vec![3, 2]
                ]
            ),
            true
        );
    }

    #[test]
    fn test_multiple_independent_chains() {
        // 0→1, 2→3
        assert_eq!(
            Solution::can_finish(
                4,
                vec![
                    vec![1, 0],
                    vec![3, 2]
                ]
            ),
            true
        );
    }

    #[test]
    fn test_empty_prerequisites() {
        // No deps => always true
        assert_eq!(Solution::can_finish(5, vec![]), true);
    }

    #[test]
    fn test_cycle_long_chain() {
        // 0→1→2→3→1 (cycle)
        assert_eq!(
            Solution::can_finish(
                4,
                vec![
                    vec![1, 0],
                    vec![2, 1],
                    vec![3, 2],
                    vec![1, 3], // cycle back to 1
                ]
            ),
            false
        );
    }

    #[test]
    fn test_self_cycle() {
        // Course depends on itself
        assert_eq!(Solution::can_finish(1, vec![vec![0, 0]]), false);
    }

    #[test]
    fn test_large_no_cycle() {
        // 0→1, 2→3, 4→5, ... etc
        let prereqs: Vec<Vec<i32>> =
            (0..20).step_by(2).map(|i: i32| vec![i + 1, i]).collect();

        assert_eq!(Solution::can_finish(40, prereqs), true);
    }
}
