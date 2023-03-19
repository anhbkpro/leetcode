from lc_2553_separate_the_digits_in_an_array import separateDigits


def test_separate_digits():
    assert separateDigits([123, 456]) == [1, 2, 3, 4, 5, 6]
    assert separateDigits([123, 456, 789]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert separateDigits([123, 456, 789, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
