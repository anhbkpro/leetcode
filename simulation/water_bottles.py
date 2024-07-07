class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            numBottles = empty // numExchange
            ans += numBottles
            empty = numBottles + empty % numExchange

        return ans
