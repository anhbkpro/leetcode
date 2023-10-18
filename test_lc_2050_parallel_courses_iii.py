from lc_2050_parallel_courses_iii import Solution


def test_minimum_time():
    assert Solution.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]) == 8
    assert Solution.minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]) == 12
