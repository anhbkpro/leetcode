struct Solution;

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::new();

        let mut iter1 = word1.chars();
        let mut iter2 = word2.chars();

        loop {
            match (iter1.next(), iter2.next()) {
                (Some(c1), Some(c2)) => {
                    result.push(c1);
                    result.push(c2);
                }
                (Some(c1), None) => {
                    result.push(c1);
                    result.extend(iter1);
                    break;
                }
                (None, Some(c2)) => {
                    result.push(c2);
                    result.extend(iter2);
                    break;
                }
                (None, None) => break,
            }
        }

        result
    }
}


fn main() {
    let word1 = "abc".to_string();
    let word2 = "pqr".to_string();
    let result = Solution::merge_alternately(word1, word2);
    println!("Result: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_merge_alternately() {
        assert_eq!(Solution::merge_alternately("abc".to_string(), "pqr".to_string()), "apbqcr".to_string());
    }
}
