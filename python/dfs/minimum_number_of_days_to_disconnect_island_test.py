from .minimum_number_of_days_to_disconnect_island import Solution


def test_minimum_number_of_days_to_disconnect_island():
    # Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    # Output: 2
    grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    assert Solution().minDays(grid) == 2
    # Input: grid = [[1,1]]
    # Output: 2
    grid = [[1, 1]]
    assert Solution().minDays(grid) == 2
