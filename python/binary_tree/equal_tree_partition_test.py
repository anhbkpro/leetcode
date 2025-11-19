from binary_tree.equal_tree_partition import Solution, TreeNode


def create_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def test_leetcode_example1():
    """
    Input: root = [5,10,10,null,null,2,3]
    Output: true

    Explanation:
    - Total sum of the tree is 30
    - If we remove the edge between 5 and 10, we get two subtrees:
      * Left subtree: 10 (sum = 10)
      * Right subtree: 10 + 2 + 3 = 15
    - The sums are equal (10 = 10), so return true
    """
    solution = Solution()
    root = create_tree([5, 10, 10, None, None, 2, 3])
    assert solution.checkEqualTree(root) is True


def test_leetcode_example2():
    """
    Input: root = [1,2,10,null,null,2,20]
    Output: false

    Explanation:
    - Total sum of the tree is 35
    - No matter which edge we remove, we cannot split the tree into two subtrees with equal sums
    - Therefore, return false
    """
    solution = Solution()
    root = create_tree([1, 2, 10, None, None, 2, 20])
    assert solution.checkEqualTree(root) is False
