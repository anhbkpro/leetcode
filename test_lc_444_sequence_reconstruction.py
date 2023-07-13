from lc_444_sequence_reconstruction import sequence_reconstruction


def test_sequence_reconstruction():
    assert sequence_reconstruction([1, 2, 3], [[1, 2], [1, 3]]) is False
    assert sequence_reconstruction([1, 2, 3], [[1, 2]]) is False
    assert sequence_reconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]]) is True
