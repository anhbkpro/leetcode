from .water_bottles import Solution


def test_water_bottles():
    assert Solution().numWaterBottles(numBottles=9, numExchange=3) == 13
    assert Solution().numWaterBottles(numBottles=15, numExchange=4) == 19
