from lc_249_group_shifted_strings import groupStrings


def test_group_strings():
    assert groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]) == [
        ['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]
