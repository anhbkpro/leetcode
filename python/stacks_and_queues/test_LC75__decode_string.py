import pytest

from stacks_and_queues.LC75__decode_string import Solution


@pytest.mark.parametrize(
    "input_s, expected_output",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("", ""),
        ("a", "a"),
        ("10[a]", "aaaaaaaaaa"),
        ("2[3[a]b]", "aaabaaab"),
        (
            "3[z]2[2[y]pq4[2[jk]e1[f]]]ef",
            "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",
        ),
        ("100[leetcode]", "leetcode" * 100),
    ],
)
def test_decode_string(input_s, expected_output):
    solution = Solution()
    actual_output = solution.decodeString(input_s)
    assert actual_output == expected_output
