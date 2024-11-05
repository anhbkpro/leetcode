from .minimum_number_of_changes_to_make_binary_string_beautiful import (
    Solution,
    GreedySolution,
)


def test_minimum_number_of_changes_to_make_binary_string_beautiful():
    assert Solution().minChanges(s="1001") == 2
    assert Solution().minChanges(s="10") == 1
    assert GreedySolution().minChanges(s="1001") == 2
    assert GreedySolution().minChanges(s="10") == 1
