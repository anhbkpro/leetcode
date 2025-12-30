import pytest

from .partition_labels import MergeIntervals, TwoPointers


class TestMergeIntervals:
    @pytest.fixture
    def solution(self):
        return MergeIntervals()

    def test_example1(self, solution):
        s = "ababcbacadefegdehijhklij"
        assert solution.partitionLabels(s) == [9, 7, 8]

    def test_example2(self, solution):
        s = "eccbbbbdec"
        assert solution.partitionLabels(s) == [10]

    def test_single_char(self, solution):
        s = "a"
        assert solution.partitionLabels(s) == [1]

    def test_all_same(self, solution):
        s = "aaa"
        assert solution.partitionLabels(s) == [3]

    def test_no_overlap(self, solution):
        s = "abc"
        assert solution.partitionLabels(s) == [1, 1, 1]

    def test_empty(self, solution):
        s = ""
        assert solution.partitionLabels(s) == []

    def test_complex(self, solution):
        s = "abacbdefghijklmnopqrstuvwxyz"
        assert solution.partitionLabels(s) == [5] + [1] * 23

    def test_overlapping(self, solution):
        s = "ababab"
        assert solution.partitionLabels(s) == [6]


class TestTwoPointers:
    @pytest.fixture
    def solution(self):
        return TwoPointers()

    def test_example1(self, solution):
        s = "ababcbacadefegdehijhklij"
        assert solution.partitionLabels(s) == [9, 7, 8]

    def test_example2(self, solution):
        s = "eccbbbbdec"
        assert solution.partitionLabels(s) == [10]

    def test_single_char(self, solution):
        s = "a"
        assert solution.partitionLabels(s) == [1]

    def test_all_same(self, solution):
        s = "aaa"
        assert solution.partitionLabels(s) == [3]

    def test_no_overlap(self, solution):
        s = "abc"
        assert solution.partitionLabels(s) == [1, 1, 1]

    def test_empty(self, solution):
        s = ""
        assert solution.partitionLabels(s) == []

    def test_complex(self, solution):
        s = "abacbdefghijklmnopqrstuvwxyz"
        assert solution.partitionLabels(s) == [5] + [1] * 23

    def test_overlapping(self, solution):
        s = "ababab"
        assert solution.partitionLabels(s) == [6]

    def test_all_alphabet(self, solution):
        s = "abcdefghijklmnopqrstuvwxyz"
        assert solution.partitionLabels(s) == [1] * 26

    def test_reverse_alphabet(self, solution):
        s = "zyxwvutsrqponmlkjihgfedcba"
        assert solution.partitionLabels(s) == [1] * 26

    def test_alternating_pairs(self, solution):
        s = "aabbccddee"
        assert solution.partitionLabels(s) == [2] * 5
