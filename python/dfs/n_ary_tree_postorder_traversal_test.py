from .n_ary_tree_postorder_traversal import Solution
from .tree_node import NAryTree


def test_n_ary_tree_postorder_traversal():
    # Input: root = [1,null,3,2,4,null,5,6]
    # Output: [5,6,3,2,4,1]
    root = NAryTree(1)
    root.children = [NAryTree(3), NAryTree(2), NAryTree(4)]
    root.children[0].children = [NAryTree(5), NAryTree(6)]
    assert Solution().postorder(root) == [5, 6, 3, 2, 4, 1]
