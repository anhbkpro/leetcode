from typing import List


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        def backtrack(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            need = k - len(curr)  # the number of elements we still need to add.
            remain = n - first_num + 1
            available = remain - need  # the amount of numbers we can consider at the current node.

            for num in range(first_num, first_num + available + 1):
                curr.append(
                    num)  # Modifying curr and making a recursive call is equivalent to "traversing" to a child node
                # in the tree.
                backtrack(curr, num + 1)
                curr.pop()  # "backtracking" step

            return  # When we return from a function call, it's equivalent to moving back up the tree (exactly like
            # in a DFS)

        ans = []
        backtrack([], 1)
        return ans
