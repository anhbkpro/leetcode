from .string_compression_iii import Solution


def test_string_compression_iii():
    assert Solution().compressedString("aaabcccd") == "3a1b3c1d"
    assert Solution().compressedString("aaaaaaaaaaaaaabb") == "9a5a2b"
