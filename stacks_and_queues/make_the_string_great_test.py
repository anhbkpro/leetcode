from stacks_and_queues.make_the_string_great import Solution


def test_make_the_string_great():
    assert Solution().makeGood("leEeetcode") == "leetcode"
    assert Solution().makeGood("abBAcC") == ""
