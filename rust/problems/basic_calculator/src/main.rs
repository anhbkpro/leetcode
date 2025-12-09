struct Solution;

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let mut result = 0;
        let mut number = 0;
        let mut sign = 1;

        let mut chars = s.chars().peekable();

        while let Some(c) = chars.next() {
            match c {
                '0'..='9' => {
                    number = number * 10 + (c as i32 - '0' as i32);
                }
                '+' => {
                    result += sign * number;
                    number = 0;
                    sign = 1;
                }
                '-' => {
                    result += sign * number;
                    number = 0;
                    sign = -1;
                }
                '(' => {
                    // push current result and sign
                    stack.push(result);
                    stack.push(sign);

                    // reset for expression inside parentheses
                    result = 0;
                    sign = 1;
                }
                ')' => {
                    // complete this inner expression
                    result += sign * number;
                    number = 0;

                    // apply sign before '('
                    let prev_sign = stack.pop().unwrap();
                    result *= prev_sign;

                    // add previous result
                    let prev_result = stack.pop().unwrap();
                    result += prev_result;
                }
                ' ' => {} // skip spaces
                _ => {}
            }
        }

        // Add last pending number
        result += sign * number;

        result
    }
}


fn main() {
    println!("{:?}", Solution::calculate("1 + 2".to_string()))
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate() {
        assert_eq!(Solution::calculate("1 + 2".to_string()), 3);
        assert_eq!(Solution::calculate(" 2-1 + 2 ".to_string()), 3);
        assert_eq!(Solution::calculate("(1+(4+5+2)-3)+(6+8)".to_string()), 23);
        assert_eq!(Solution::calculate("1 - (2 - (3 - (4 - 5)))".to_string()), 3);
    }
}
