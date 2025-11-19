from .minimum_time_to_visit_a_cell_in_a_grid import Solution


def test_minimum_time():
    assert Solution().minimumTime(grid=[[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]) == 7
