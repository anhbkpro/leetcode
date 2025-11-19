import pytest
from .lowest_common_ancestor_of_deepest_leaves import Solution, TreeNode


class TestLowestCommonAncestorOfDeepestLeaves:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        # Input: root = [1,2,3]
        # Output: [1,2,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 1
        assert result.left.val == 2
        assert result.right.val == 3

    def test_example2(self, solution):
        # Input: root = [1,2,3,4]
        # Output: [4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 4
        assert result.left is None
        assert result.right is None

    def test_example3(self, solution):
        # Input: root = [1,2,3,4,5]
        # Output: [2,4,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 2
        assert result.left.val == 4
        assert result.right.val == 5

    def test_empty_tree(self, solution):
        # Input: root = []
        # Output: None
        result = solution.lcaDeepestLeaves(None)
        assert result is None

    def test_single_node(self, solution):
        # Input: root = [1]
        # Output: [1]
        root = TreeNode(1)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 1
        assert result.left is None
        assert result.right is None

    def test_unbalanced_left(self, solution):
        # Input: root = [1,2,null,3,null,4]
        # Output: [4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 4
        assert result.left is None
        assert result.right is None

    def test_unbalanced_right(self, solution):
        # Input: root = [1,null,2,null,3,null,4]
        # Output: [4]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 4
        assert result.left is None
        assert result.right is None

    def test_complex_tree(self, solution):
        # Input: root = [1,2,3,4,5,6,7,8]
        # Output: [8]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 8
        assert result.left is None
        assert result.right is None

    def test_same_depth_leaves(self, solution):
        # Input: root = [1,2,3,4,5,6]
        # Output: [1,2,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 1
        assert result.left.val == 2
        assert result.right.val == 3

    def test_deep_tree(self, solution):
        # Input: root = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        # Output: [1,2,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        result = solution.lcaDeepestLeaves(root)
        assert result.val == 1
        assert result.left.val == 2
        assert result.right.val == 3
