class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = numBottles
        empty = numBottles
        while empty >= numExchange:
            numBottles = empty // numExchange
            consumed_bottles += numBottles
            empty = numBottles + empty % numExchange

        return consumed_bottles
