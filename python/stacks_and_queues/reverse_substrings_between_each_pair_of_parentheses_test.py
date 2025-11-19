from .reverse_substrings_between_each_pair_of_parentheses import Solution


def test_reverse_substrings_between_each_pair_of_parentheses():
    assert Solution().reverseParentheses("(abcd)") == "dcba"
    assert Solution().reverseParentheses("(u(love)i)") == "iloveu"
    assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
