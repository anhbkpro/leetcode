from dfs.distribute_coins_in_binary_tree import Solution, TreeNode


def test_distribute_coins_in_binary_tree():
    assert Solution().distributeCoins(TreeNode(3, TreeNode(0), TreeNode(0))) == 2
    assert Solution().distributeCoins(TreeNode(0, TreeNode(3), TreeNode(0))) == 3
