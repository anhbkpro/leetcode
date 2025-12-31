use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    // Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        // (u, v) -> possible w
        let mut t: HashMap<(char, char), Vec<char>> = HashMap::new();
        for rule in allowed {
            let chars: Vec<char> = rule.chars().collect();
            t.entry((chars[0], chars[1])).or_default().push(chars[2]);
        }
        // t = {('B', 'C'): ['C'], ('C', 'D'): ['E'], ('C', 'E'): ['A'], ('F', 'F'): ['F']}

        let mut failed: HashSet<String> = HashSet::new();
        let bottom_row: Vec<char> = bottom.chars().collect();
        // bottom_row = ['B', 'C', 'D']

        fn solve(
            row: &Vec<char>,
            t: &HashMap<(char, char), Vec<char>>,
            failed: &mut HashSet<String>,
        ) -> bool {
            if row.len() == 1 {
                return true;
            }

            let key: String = row.iter().collect();
            if failed.contains(&key) {
                return false;
            }

            let mut next = Vec::with_capacity(row.len() - 1);
            if build(row, 0, &mut next, t, failed) {
                return true;
            }

            // Cache failure
            failed.insert(key);
            false
        }

        fn build(
            row: &Vec<char>,
            i: usize,
            next: &mut Vec<char>,
            t: &HashMap<(char, char), Vec<char>>,
            failed: &mut HashSet<String>,
        ) -> bool {
            if i + 1 == row.len() {
                return solve(next, t, failed);
            }

            if let Some(candidates) = t.get(&(row[i], row[i + 1])) {
                for &c in candidates {
                    next.push(c);
                    if build(row, i + 1, next, t, failed) {
                        return true;
                    }
                    next.pop();
                }
            }

            false
        }

        solve(&bottom_row, &t, &mut failed)
    }
}

fn main() {
    let bottom = "XYZ".to_string();
    let allowed = vec!["XYA".to_string(), "YZB".to_string(), "ABA".to_string()];
    let result = Solution::pyramid_transition(bottom, allowed);
    println!("Can build pyramid: {}", result); // Output: Can build pyramid: true
}
