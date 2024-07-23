from .sort_the_people import Solution


def test_sort_the_people():
    assert Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]) == ["Mary","Emma","John"]
    assert Solution().sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]) == ["Bob","Alice","Bob"]
