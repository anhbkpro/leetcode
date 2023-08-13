from lc_70_climbing_stairs import Solution


def test_climb_stairs():
    assert Solution.climbStairs(0) == 0
    assert Solution.climbStairs(1) == 1
    assert Solution.climbStairs(2) == 2
    assert Solution.climbStairs(3) == 3
    assert Solution.climbStairs(4) == 5
