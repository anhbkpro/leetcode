from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                # down trend
                i += 1
            # find the local min (vally) for this down trend
            valley = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                # up trend
                i += 1
            # find the local max (peak) for this up trend
            peak = prices[i]

            max_profit += peak - valley

        return max_profit
