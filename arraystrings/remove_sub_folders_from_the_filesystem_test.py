from .remove_sub_folders_from_the_filesystem import SolutionSet, SolutionSort


def test_remove_sub_folders_from_the_filesystem():
    assert sorted(
        SolutionSet().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    ) == ["/a", "/c/d", "/c/f"]
    assert sorted(
        SolutionSet().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"])
    ) == ["/a"]
    assert sorted(
        SolutionSort().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    ) == ["/a", "/c/d", "/c/f"]
    assert sorted(
        SolutionSort().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"])
    ) == ["/a"]
