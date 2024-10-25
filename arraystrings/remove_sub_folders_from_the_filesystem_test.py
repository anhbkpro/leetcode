from .remove_sub_folders_from_the_filesystem import Solution


def test_remove_sub_folders_from_the_filesystem():
    assert sorted(
        Solution().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    ) == ["/a", "/c/d", "/c/f"]
