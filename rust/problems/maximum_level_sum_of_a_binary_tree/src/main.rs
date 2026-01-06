use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

struct Solution;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_sum = i64::MIN;
        let mut answer = 0;
        let mut level = 0;

        let mut queue = VecDeque::new();
        if let Some(r) = root {
            queue.push_back(r);
        }

        while !queue.is_empty() {
            level += 1;
            let mut level_sum: i64 = 0;
            let size = queue.len();

            for _ in 0..size {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();

                level_sum += node.val as i64;

                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }

            if level_sum > max_sum {
                max_sum = level_sum;
                answer = level;
            }
        }

        answer
    }
}

fn main() {
    let root = TreeNode::new(1);
    let root = Some(Rc::new(RefCell::new(root)));
    let result = Solution::max_level_sum(root);
    println!("Result: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;
    use std::rc::Rc;

    fn node(val: i32) -> Rc<RefCell<TreeNode>> {
        Rc::new(RefCell::new(TreeNode::new(val)))
    }

    #[test]
    fn test_single_node() {
        let root = Some(node(5));
        assert_eq!(Solution::max_level_sum(root), 1);
    }

    #[test]
    fn test_example_case() {
        // Tree:
        //        1
        //       / \
        //      7   0
        //     / \
        //    7  -8
        //
        // Level sums:
        // 1 -> 1
        // 2 -> 7
        // 3 -> -1
        //
        // Answer: 2
        let root = node(1);
        let left = node(7);
        let right = node(0);

        let left_left = node(7);
        let left_right = node(-8);

        left.borrow_mut().left = Some(left_left);
        left.borrow_mut().right = Some(left_right);

        root.borrow_mut().left = Some(left);
        root.borrow_mut().right = Some(right);

        assert_eq!(Solution::max_level_sum(Some(root)), 2);
    }

    #[test]
    fn test_all_negative() {
        // Tree:
        //      -10
        //      /  \
        //    -20  -30
        //
        // Level sums:
        // 1 -> -10
        // 2 -> -50
        //
        // Answer: 1
        let root = node(-10);
        root.borrow_mut().left = Some(node(-20));
        root.borrow_mut().right = Some(node(-30));

        assert_eq!(Solution::max_level_sum(Some(root)), 1);
    }

    #[test]
    fn test_tie_returns_smallest_level() {
        // Tree:
        //       1
        //      / \
        //     2   3
        //    /
        //   5
        //
        // Level sums:
        // 1 -> 1
        // 2 -> 5
        // 3 -> 5
        //
        // Tie → return earliest level (2)
        let root = node(1);
        let left = node(2);
        let right = node(3);
        let left_left = node(5);

        left.borrow_mut().left = Some(left_left);
        root.borrow_mut().left = Some(left);
        root.borrow_mut().right = Some(right);

        assert_eq!(Solution::max_level_sum(Some(root)), 2);
    }

    #[test]
    fn test_deep_tree() {
        // 1 -> 2 -> 3 -> 4
        // Level sums increase each time
        let root = node(1);
        let n2 = node(2);
        let n3 = node(3);
        let n4 = node(4);

        n3.borrow_mut().left = Some(n4);
        n2.borrow_mut().left = Some(n3);
        root.borrow_mut().left = Some(n2);

        assert_eq!(Solution::max_level_sum(Some(root)), 4);
    }
}
