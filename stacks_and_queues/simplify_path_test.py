from stacks_and_queues.simplify_path import Solution


def test_simplify_path():
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/../") == "/"
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"
    assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
