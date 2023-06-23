from lc_2336_smallest_number_in_infinite_set_of_arrays import SmallestInfiniteSet

smallestInfiniteSet = SmallestInfiniteSet()


def test_pop_smallest():
    assert smallestInfiniteSet.popSmallest() == 1
    assert smallestInfiniteSet.popSmallest() == 2
    assert smallestInfiniteSet.popSmallest() == 3
    smallestInfiniteSet.addBack(1)
    assert smallestInfiniteSet.popSmallest() == 1
    smallestInfiniteSet.addBack(2)
    assert smallestInfiniteSet.popSmallest() == 2
