from lc_435_non_overlapping_intervals import eraseOverlapIntervals


def test_erase_overlap_intervals():
    assert eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2
    assert eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]) == 0

