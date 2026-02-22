struct Solution;

impl Solution {
    pub fn binary_gap(mut n: i32) -> i32 {
        let mut last: Option<i32> = None;
        let mut ans = 0;
        let mut pos = 0;

        while n > 0 {
            if n & 1 == 1 {
                if let Some(prev) = last {
                    ans = ans.max(pos - prev);
                }
                last = Some(pos);
            }
            n >>= 1;
            pos += 1;
        }

        ans
    }
}

fn main() {
    println!("868. Binary Gap");
    println!("Input: n = 22");
    println!("Output: {}", Solution::binary_gap(22));
}
