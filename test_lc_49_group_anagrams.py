from lc_49_group_anagrams import Solution


def test_group_anagrams():
    assert list(Solution.groupAnagrams(strs=[""])) == [[""]]
    assert list(Solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert list(Solution.groupAnagrams(strs=["a"])) == [["a"]]
