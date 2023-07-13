from lc_1136_parallel_courses import minimum_semesters


def test_minimum_semesters():
    assert minimum_semesters(3, [[1, 3], [2, 3]]) == 2
    assert minimum_semesters(3, [[1, 2], [2, 3], [3, 1]]) == -1
    assert minimum_semesters(3, [[1, 2], [2, 3]]) == 3
