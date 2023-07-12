from lc_207_course_schedule import canFinish


def test_can_finish():
    assert canFinish(2, [[1, 0]]) is True
    assert canFinish(2, [[1, 0], [0, 1]]) is False
