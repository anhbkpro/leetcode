from lc_111_minimum_depth_of_binary_tree import TreeNode


class Solution:
    @staticmethod
    def pseudoPalindromicPaths(root: TreeNode) -> int:
        count = 0

        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurrences of each digit
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count
