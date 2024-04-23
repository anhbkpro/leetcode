from toposort.course_schedule import Solution


def test_can_finish():
    assert Solution().canFinish(numCourses=2, prerequisites=[[1, 0]]) is True
    assert Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]) is False
