use std::cell::RefCell;
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
    pub fn subtree_with_all_deepest(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (Option<Rc<RefCell<TreeNode>>>, i32) {
            match node {
                None => (None, 0),
                Some(n) => {
                    let n_ref = n.borrow();

                    let (left_node, left_depth) = dfs(n_ref.left.clone());
                    let (right_node, right_depth) = dfs(n_ref.right.clone());

                    if left_depth > right_depth {
                        (left_node, left_depth + 1)
                    } else if right_depth > left_depth {
                        (right_node, right_depth + 1)
                    } else {
                        (Some(n.clone()), left_depth + 1)
                    }
                }
            }
        }

        dfs(root).0
    }
}

fn main() {
    let root = TreeNode::new(1);
    let root = Some(Rc::new(RefCell::new(root)));
    let result = Solution::subtree_with_all_deepest(root);
    println!("Result: {:?}", result);
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
        let root = Some(node(1));
        let ans = Solution::subtree_with_all_deepest(root.clone());
        assert_eq!(ans.unwrap().borrow().val, 1);
    }

    #[test]
    fn test_balanced_tree() {
        //      1
        //     / \
        //    2   3
        //
        // Deepest nodes: 2, 3
        // Answer: 1
        let root = node(1);
        root.borrow_mut().left = Some(node(2));
        root.borrow_mut().right = Some(node(3));

        let ans = Solution::subtree_with_all_deepest(Some(root));
        assert_eq!(ans.unwrap().borrow().val, 1);
    }

    #[test]
    fn test_left_skewed_tree() {
        // 1
        // |
        // 2
        // |
        // 3
        //
        // Deepest node: 3
        // Answer: 3
        let root = node(1);
        let n2 = node(2);
        let n3 = node(3);

        n2.borrow_mut().left = Some(n3);
        root.borrow_mut().left = Some(n2);

        let ans = Solution::subtree_with_all_deepest(Some(root));
        assert_eq!(ans.unwrap().borrow().val, 3);
    }

    #[test]
    fn test_example_case() {
        //        3
        //       / \
        //      5   1
        //     / \
        //    6   2
        //       / \
        //      7   4
        //
        // Deepest nodes: 7, 4
        // Answer: 2
        let root = node(3);
        let n5 = node(5);
        let n1 = node(1);
        let n6 = node(6);
        let n2 = node(2);
        let n7 = node(7);
        let n4 = node(4);

        n2.borrow_mut().left = Some(n7);
        n2.borrow_mut().right = Some(n4);

        n5.borrow_mut().left = Some(n6);
        n5.borrow_mut().right = Some(n2);

        root.borrow_mut().left = Some(n5);
        root.borrow_mut().right = Some(n1);

        let ans = Solution::subtree_with_all_deepest(Some(root));
        assert_eq!(ans.unwrap().borrow().val, 2);
    }

    #[test]
    fn test_two_deepest_on_different_sides() {
        //      1
        //     / \
        //    2   3
        //     \   \
        //      4   5
        //
        // Deepest nodes: 4, 5
        // Answer: 1
        let root = node(1);
        let n2 = node(2);
        let n3 = node(3);
        let n4 = node(4);
        let n5 = node(5);

        n2.borrow_mut().right = Some(n4);
        n3.borrow_mut().right = Some(n5);

        root.borrow_mut().left = Some(n2);
        root.borrow_mut().right = Some(n3);

        let ans = Solution::subtree_with_all_deepest(Some(root));
        assert_eq!(ans.unwrap().borrow().val, 1);
    }
}
