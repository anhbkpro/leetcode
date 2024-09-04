from .walking_robot_simulation import Solution


def test_walking_robot_simulation():
    assert Solution().robotSim([4, -1, 3], []) == 25
    assert Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]) == 65
