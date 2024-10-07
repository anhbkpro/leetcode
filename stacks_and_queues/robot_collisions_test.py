from .robot_collisions import Solution


def test_survived_robots_healths():
    assert Solution().survivedRobotsHealths(
        positions=[5, 4, 3, 2, 1], healths=[2, 17, 9, 15, 10], directions="RRRRR"
    ) == [2, 17, 9, 15, 10]
