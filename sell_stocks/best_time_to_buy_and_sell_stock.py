from typing import List


class Solution:
    # prices = [7, 1, 5, 3, 6, 4]
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # price = 7 -> 1 -> 5 -> 3 -> 6 -> 4
            min_price = min(min_price, price) # min_price = 7 -> 1 -> 1 -> 1 -> 1 -> 1
            max_profit = max(max_profit, price - min_price) # max_profit = 0 -> 0 -> 4 -> 4 -> 5 -> 5

        return max_profit # 5
