from .append_characters_to_string_to_make_subsequence import Solution


def test_append_characters_to_string_to_make_subsequence():
    assert Solution().appendCharacters("zzazz", "zz") == 0
    assert Solution().appendCharacters("mbadm", "bda") == 1
    assert Solution().appendCharacters("coaching", "coding") == 4
