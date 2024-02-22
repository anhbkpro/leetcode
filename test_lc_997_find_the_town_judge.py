from lc_997_find_the_town_judge import Solution


def test_find_judge():
    assert Solution.find_judge(n=2, trust=[[1, 2]]) == 2
    assert Solution.find_judge(n=3, trust=[[1, 3], [2, 3]]) == 3
    assert Solution.find_judge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
