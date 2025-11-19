from .minimum_limit_of_balls_in_a_bag import Solution


def test_minimum_size():
    assert Solution().minimumSize(nums=[9], max_operations=2) == 3
    assert Solution().minimumSize(nums=[2, 4, 8, 2], max_operations=4) == 2
