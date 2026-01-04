struct Solution;

impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            let limit = (x as f64).sqrt() as i32;
            for i in 2..=limit {
                if x % i == 0 {
                    return false;
                }
            }
            true
        }

        let mut total = 0;

        for n in nums {
            // Case 1: n = p^3
            let p = (n as f64).cbrt().round() as i32;
            if p * p * p == n && is_prime(p) {
                total += 1 + p + p * p + n;
                continue;
            }

            // Case 2: n = p * q (p != q, both prime)
            let limit = (n as f64).sqrt() as i32;
            for i in 2..=limit {
                if n % i == 0 {
                    let j = n / i;
                    if i != j && is_prime(i) && is_prime(j) {
                        total += 1 + i + j + n;
                    }
                    break; // only need first factor
                }
            }
        }

        total
    }
}

fn main() {
    let result = Solution::sum_four_divisors(vec![21, 4, 7]);
    println!("result = {}", result);
}
