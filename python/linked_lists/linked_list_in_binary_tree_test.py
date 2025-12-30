from .linked_list_in_binary_tree import ListNode, Solution, TreeNode


def test_linked_list_in_binary_tree():
    # Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    # Output: true
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(8)

    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(8)
    root.right.left.right.left = TreeNode(1)
    root.right.left.right.right = TreeNode(3)
    assert Solution().isSubPath(head, root) is True
