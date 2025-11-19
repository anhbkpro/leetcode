import pytest
from stacks_and_queues.LC75__removing_stars_from_a_string import Solution


@pytest.mark.parametrize(
    "input_s, expected_output",
    [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
        ("a*b*c*", ""),
        ("abc", "abc"),
        ("ab**", ""),
        ("a", "a"),
        ("", ""),
        ("abc*def*", "abde"),
        ("a*b*c", "c"),
    ],
)
def test_remove_stars(input_s, expected_output):
    solution = Solution()
    actual_output = solution.removeStars(input_s)
    assert actual_output == expected_output
