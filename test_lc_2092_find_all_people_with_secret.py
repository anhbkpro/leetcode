from lc_2092_find_all_people_with_secret import Solution


def test_find_all_people():
    assert Solution.find_all_people(
        n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1
    ) == [0, 1, 2, 3, 5]
    assert Solution.find_all_people(
        n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3
    ) == [0, 1, 3]
