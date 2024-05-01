from stacks_and_queues.daily_temperatures import Solution


def test_daily_temperatures():
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
