from typing import List


class Solution:
    @staticmethod
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain: int, index: int, combi: List[int]):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(combi))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(index, len(candidates)):
                # add the number into the combination
                combi.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], i, combi)
                # backtrack, remove the number from the combination
                combi.pop()

        backtrack(target, 0, [])

        return results
