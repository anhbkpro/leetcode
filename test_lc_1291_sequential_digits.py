from lc_1291_sequential_digits import Solution


def test_sequential_digits():
    assert Solution.sequentialDigits(low=100, high=300) == [123, 234]
    assert Solution.sequentialDigits(low=1000, high=13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
