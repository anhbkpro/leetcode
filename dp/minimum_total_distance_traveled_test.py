from .minimum_total_distance_traveled import Solution


def test_minimum_total_distance_traveled():
    assert (
        Solution().minimumTotalDistance(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]) == 4
    )
