from .the_number_of_the_smallest_unoccupied_chair import Solution


def test_the_number_of_the_smallest_unoccupied_chair():
    assert Solution().smallestChair(times=[[1, 4], [2, 3], [4, 6]], targetFriend=1) == 1
    assert (
        Solution().smallestChair(times=[[3, 10], [1, 5], [2, 6]], targetFriend=0) == 2
    )
