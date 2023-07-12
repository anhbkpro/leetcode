from lc_210_course_schedule_ii import find_order


def test_find_order():
    assert find_order(2, [[1, 0]]) == [0, 1]
    assert find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert find_order(1, []) == [0]
