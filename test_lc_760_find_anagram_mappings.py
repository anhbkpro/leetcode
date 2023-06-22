from lc_760_find_anagram_mappings import anagramMappings


def test_anagram_mappings():
    assert anagramMappings(nums1=[12, 28, 46, 32, 50], nums2=[50, 12, 32, 46, 28]) == [1, 4, 3, 2, 0]
