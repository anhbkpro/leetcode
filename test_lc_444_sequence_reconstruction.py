from lc_444_sequence_reconstruction import sequenceReconstruction


def test_sequence_reconstruction():
    assert sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]]) is False
    assert sequenceReconstruction([1, 2, 3], [[1, 2]]) is False
    assert sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]]) is True
