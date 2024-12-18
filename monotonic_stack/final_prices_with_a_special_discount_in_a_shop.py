from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        for i, num in enumerate(prices):
            while stk and prices[stk[-1]] >= num:
                idx = stk.pop()
                prices[idx] -= num

            stk.append(i)
        return prices
