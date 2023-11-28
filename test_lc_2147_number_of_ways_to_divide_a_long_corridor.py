from lc_2147_number_of_ways_to_divide_a_long_corridor import Solution


def test_number_of_ways():
    assert Solution.numberOfWays(corridor="S") == 0
    assert Solution.numberOfWays(corridor="SSPPSPS") == 3
    assert Solution.numberOfWays(corridor="PPSPSP") == 1
