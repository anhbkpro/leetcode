from .minimum_obstacle_removal_to_reach_corner import Solution


def test_minimum_obstacles():
    assert Solution().minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
