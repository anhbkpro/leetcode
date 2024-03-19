from task_scheduler import Solution


def test_least_interval():
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
