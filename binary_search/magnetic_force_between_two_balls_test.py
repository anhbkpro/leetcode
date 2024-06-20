from .magnetic_force_between_two_balls import Solution


def test_magnetic_force_between_two_balls():
    assert Solution().maxDistance(position=[1, 2, 3, 4, 7], m=3) == 3
    assert Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2) == 999999999
