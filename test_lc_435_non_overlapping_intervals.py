from lc_435_non_overlapping_intervals import erase_overlap_intervals


def test_erase_overlap_intervals():
    assert erase_overlap_intervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals(intervals=[[1, 2], [2, 3]]) == 0

