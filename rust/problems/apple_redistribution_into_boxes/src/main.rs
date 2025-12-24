struct Solution;


impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>) -> i32 {
        let mut sum: i32 = apple.iter().sum();
        let mut sorted_capacity = capacity.clone();
        sorted_capacity.sort_by(|a, b| b.cmp(a));

        let mut need = 0;
        while sum > 0 {
            sum -= sorted_capacity[need as usize];
            need += 1;
        }

        need
    }
}

fn main() {
    let apples = vec![5, 10, 15];
    let capacities = vec![10, 10, 10, 10];
    let result = Solution::minimum_boxes(apples, capacities);
    println!("Minimum number of boxes needed: {}", result);
}

// add test cases if needed
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_minimum_boxes() {
        let apples = vec![5, 10, 15];
        let capacities = vec![10, 10, 10, 10];
        assert_eq!(Solution::minimum_boxes(apples, capacities), 3); // 10 + 10 + 10 >= 30
    }
    #[test]
    fn test_minimum_boxes_edge() {
        let apples = vec![1];
        let capacities = vec![1];
        assert_eq!(Solution::minimum_boxes(apples, capacities), 1); // 1 >= 1
    }
}
