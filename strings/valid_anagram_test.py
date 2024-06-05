from strings.valid_anagram import Solution


def test_valid_anagram():
    assert Solution().isAnagram("anagram", "nagaram") is True
    assert Solution().isAnagram("rat", "car") is False
