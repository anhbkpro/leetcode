import pytest
from partition_labels import Solution


def test_partition_labels_example1():
    solution = Solution()
    s = "ababcbacadefegdehijhklij"
    assert solution.partitionLabels(s) == [9, 7, 8]


def test_partition_labels_example2():
    solution = Solution()
    s = "eccbbbbdec"
    assert solution.partitionLabels(s) == [10]


def test_partition_labels_single_char():
    solution = Solution()
    s = "a"
    assert solution.partitionLabels(s) == [1]


def test_partition_labels_all_same():
    solution = Solution()
    s = "aaa"
    assert solution.partitionLabels(s) == [3]


def test_partition_labels_no_overlap():
    solution = Solution()
    s = "abc"
    assert solution.partitionLabels(s) == [1, 1, 1]


def test_partition_labels_empty():
    solution = Solution()
    s = ""
    assert solution.partitionLabels(s) == []


def test_partition_labels_complex():
    solution = Solution()
    s = "abacbdefghijklmnopqrstuvwxyz"
    assert solution.partitionLabels(s) == [
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]


def test_partition_labels_overlapping():
    solution = Solution()
    s = "ababab"
    assert solution.partitionLabels(s) == [6]
