from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # print the tree in a platen format
        return str(self.val) + " " + str(self.left) + " " + str(self.right)


class Solution:
    def allPossibleBST(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]

        # Iterate through all values from start to end to construct left and right subtree recursively.
        for i in range(start, end + 1):
            left_sub_trees = self.allPossibleBST(start, i - 1, memo)
            right_sub_trees = self.allPossibleBST(i + 1, end, memo)

            # Loop through all left and right subtrees and connect them to ith root.
            for left in left_sub_trees:
                for right in right_sub_trees:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossibleBST(1, n, memo)
