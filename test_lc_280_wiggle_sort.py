from lc_280_wiggle_sort import wiggleSort


def test_wiggle_sort():
    array = [3, 5, 2, 1, 6, 4]
    wiggleSort(array)
    assert array == [1, 3, 2, 5, 4, 6]
