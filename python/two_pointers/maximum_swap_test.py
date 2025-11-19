from .maximum_swap import Solution


def test_maximum_swap():
    assert Solution().maximumSwap(num=2736) == 7236
    assert Solution().maximumSwap(num=9973) == 9973
