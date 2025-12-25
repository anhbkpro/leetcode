from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        turn = 0
        res = 0
        while turn < len(happiness) and happiness[turn] - turn > 0 and k > 0:
            res += happiness[turn] - turn
            turn += 1
            k -= 1
        return res
