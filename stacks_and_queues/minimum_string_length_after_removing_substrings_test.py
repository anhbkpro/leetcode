from .minimum_string_length_after_removing_substrings import Solution


def test_minimum_string_length_after_removing_substrings():
    assert Solution().minLength(s="ABFCACDB") == 2
    assert Solution().minLength(s="ACBBD") == 5
