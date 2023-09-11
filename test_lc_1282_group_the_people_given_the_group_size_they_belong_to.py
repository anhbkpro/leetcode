from lc_1282_group_the_people_given_the_group_size_they_belong_to import Solution


def test_group_the_people():
    assert Solution.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]) == [[0, 1, 2], [3, 4, 6], [5]]
    assert Solution.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]) == [[0, 5], [1], [2, 3, 4]]
