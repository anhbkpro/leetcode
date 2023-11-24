from typing import List


class Solution:
    @staticmethod
    def maxCoins(piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        turns = len(piles) // 3
        j = 0
        for i in range(len(piles) - 1, -1, -1):
            if j % 2 == 1 and turns > 0:
                max_coins += piles[i]
                turns -= 1
            j += 1

        return max_coins
