from lc_1429_first_unique_number import FirstUnique


def test_first_unique():
    first_unique = FirstUnique([2, 3, 5])
    assert first_unique.showFirstUnique() == 2
    first_unique.add(5)
    assert first_unique.showFirstUnique() == 2
    first_unique.add(2)
    assert first_unique.showFirstUnique() == 3
    first_unique.add(3)
    assert first_unique.showFirstUnique() == -1
