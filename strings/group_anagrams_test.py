from .group_anagrams import Solution


def test_group_anagrams():
    assert sorted(Solution().groupAnagrams(["eat", "tea", "bat"])) == [["bat"], ["eat", "tea"]]
    assert sorted(Solution().groupAnagrams([""])) == [[""]]
    assert sorted(Solution().groupAnagrams(["a"])) == [["a"]]
