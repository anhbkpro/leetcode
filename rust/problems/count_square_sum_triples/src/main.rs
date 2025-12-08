struct Solution;

impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut res = 0;
        for a in 1..=n {
            for b in 1..=n {
                let c = ((a*a + b *b) as f64).sqrt().floor() as i32;
                if c <= n && c*c == a*a + b *b {
                    res += 1;
                }
            }
        }
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_triples() {
        assert_eq!(Solution::count_triples(5), 2);
        assert_eq!(Solution::count_triples(10), 4);
    }
}
