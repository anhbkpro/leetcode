from .remove_sub_folders_from_the_filesystem import (
    SolutionSet,
    SolutionSort,
    SolutionTrie,
)


def test_remove_sub_folders_from_the_filesystem():
    # Test cases for SolutionSet
    assert sorted(
        SolutionSet().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    ) == ["/a", "/c/d", "/c/f"]
    assert sorted(
        SolutionSet().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"])
    ) == ["/a"]
    # Test cases for SolutionSort
    assert sorted(
        SolutionSort().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    ) == ["/a", "/c/d", "/c/f"]
    assert sorted(
        SolutionSort().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"])
    ) == ["/a"]
    # Test cases for SolutionTrie
    assert sorted(
        SolutionTrie().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    ) == ["/a", "/c/d", "/c/f"]
    assert sorted(
        SolutionTrie().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"])
    ) == ["/a"]
