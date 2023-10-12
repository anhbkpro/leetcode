from lc_2140_solving_questions_with_brainpower import Solution


def test_most_points():
    assert Solution.mostPoints(questions=[[1, 2], [2, 3], [3, 1]]) == 3
    assert Solution.mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
    assert Solution.mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
