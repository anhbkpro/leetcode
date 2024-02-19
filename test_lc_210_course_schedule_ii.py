from lc_210_course_schedule_ii import Solution


def test_find_order():
    assert Solution.find_order(2, [[1, 0]]) == [0, 1]
    assert Solution.find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert Solution.find_order(1, []) == [0]
    # cyclic graph
    assert Solution.find_order(numCourses = 3, prerequisites = [[1, 0], [1, 2], [0, 1]]) == []
