from toposort.course_schedule_ii import Solution


def test_find_order():
    assert Solution().findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert Solution().findOrder(
        numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
    ) == [0, 1, 2, 3]
