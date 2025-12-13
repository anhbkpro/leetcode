struct Solution;

impl Solution {
    pub fn validate_coupons(code: Vec<String>,
                            business_line: Vec<String>,
                            is_active: Vec<bool>) -> Vec<String> {
        let mut e = vec![];
        let mut g = vec![];
        let mut p = vec![];
        let mut r = vec![];

        for i in 0..is_active.len() {
            if !is_active[i] { continue; }

            let bl = &business_line[i];
            if bl != "electronics" && bl != "grocery" &&
               bl != "pharmacy" && bl != "restaurant" {
                continue;
            }

            if code[i].is_empty() { continue; }

            if !code[i].chars().all(|c| c.is_ascii_alphanumeric() || c == '_') {
                continue;
            }

            match bl.as_bytes()[0] {
                b'e' => e.push(code[i].clone()),
                b'g' => g.push(code[i].clone()),
                b'p' => p.push(code[i].clone()),
                b'r' => r.push(code[i].clone()),
                _ => {}
            }
        }

        e.sort(); g.sort(); p.sort(); r.sort();
        e.into_iter().chain(g).chain(p).chain(r).collect()
    }
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_validate_coupons() {
        assert_eq!(Solution::validate_coupons(vec!["SAVE20".to_string(), "SAVE@20".to_string()], vec!["restaurant".to_string(), "grocery".to_string()], vec![true, true]), vec!["SAVE20".to_string()]);
    }
}
