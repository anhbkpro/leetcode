from lc_228_summary_ranges import summaryRanges


def test_summary_ranges():
    assert summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
