struct Solution {}

impl Solution {
    pub fn max_run_time(n: i32, mut batteries: Vec<i32>) -> i64 {
        let n: usize = n as usize;

        // Sort batteries
        batteries.sort();

        // Sum of all but the largest n batteries = extra
        let mut extra: i64 = batteries[..batteries.len() - n]
            .iter()
            .map(|&x| x as i64)
            .sum();

        // The largest n batteries
        let live: Vec<i64> = batteries[batteries.len() - n..]
            .iter()
            .map(|&x| x as i64)
            .collect();

        // Level up the smallest batteries among the n chosen
        for i in 0..n - 1 {
            let diff = live[i + 1] - live[i];
            let needed = diff * (i as i64 + 1);

            // If we cannot fully reach live[i+1], return partial answer
            if extra < needed {
                return live[i] + extra / (i as i64 + 1);
            }

            // Otherwise deduct the extra used
            extra -= needed;
        }

        // If leftover extra, distribute evenly over all n
        live[n - 1] + extra / (n as i64)
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_case() {
        // Example: n = 2, batteries = [3,3,3]
        // Extra = 3, live = [3,3]
        assert_eq!(Solution::max_run_time(2, vec![3, 3, 3]), 4);
    }

    #[test]
    fn test_partial_leveling() {
        // n = 2, batteries = [1,1,10]
        // live = [1,10], extra = 1
        // extra / 1 < live[1] - live[0] → 1 < 9 → true
        assert_eq!(Solution::max_run_time(2, vec![1, 1, 10]), 2);
    }

    #[test]
    fn test_all_equal() {
        // All batteries equal → runtime = value
        assert_eq!(Solution::max_run_time(3, vec![5, 5, 5]), 5);
    }

    #[test]
    fn test_exact_match() {
        // n = 3, batteries = [10,10,10]
        assert_eq!(Solution::max_run_time(3, vec![10, 10, 10]), 10);
    }

    #[test]
    fn test_large_values() {
        // Large test: ensure no overflow
        assert_eq!(
            Solution::max_run_time(2, vec![1_000_000_000, 1_000_000_000, 1_000_000_000]),
            1_500_000_000
        );
    }

    #[test]
    fn test_exact_n_batteries() {
        // No "extra", batteries match exactly n
        assert_eq!(
            Solution::max_run_time(2, vec![4, 7]),
            4 + 0 // smallest battery + ∅ extra
        );
    }
}
