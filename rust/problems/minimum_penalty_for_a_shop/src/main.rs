struct Solution;

impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        // Initial penalty: count of 'Y'
        let mut cur_penalty: i32 = customers.chars().filter(|&c| c == 'Y').count() as i32;

        let mut min_penalty = cur_penalty;
        let mut earliest_hour: i32 = 0;

        for (i, ch) in customers.chars().enumerate() {
            if ch == 'Y' {
                cur_penalty -= 1;
            } else {
                cur_penalty += 1;
            }

            if cur_penalty < min_penalty {
                min_penalty = cur_penalty;
                earliest_hour = (i + 1) as i32;
            }
        }

        earliest_hour
    }
}

fn main() {
    let customers = "YYNY".to_string();
    let result = Solution::best_closing_time(customers);
    println!("{}", result); // Output: 2
}
