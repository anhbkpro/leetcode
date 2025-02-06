from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = Counter(s2)
        if s1_counter != s2_counter:
            return False

        swaps = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                swaps += 1

        return swaps <= 2


class SolutionFrequencyMapCheckDifferences:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1_frequency_map = [0] * 26
        s2_frequency_map = [0] * 26
        num_diffs = 0

        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]

            if s1_char != s2_char:
                num_diffs += 1
                # num_diffs is more than 2, one string swap will not make two strings equal
                if num_diffs > 2:
                    return False

            # increment frequencies
            s1_frequency_map[ord(s1_char) - ord("a")] += 1
            s2_frequency_map[ord(s2_char) - ord("a")] += 1

        # check if frequencies are equal
        return s1_frequency_map == s2_frequency_map


class SolutionOnlyCheckDifferences:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        first_index_diff = -1
        second_index_diff = -1
        num_diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                # num_diffs is more than 2, one string swap will not make two strings equal
                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    # store the index of first difference
                    first_index_diff = i
                else:
                    # store the index of second difference
                    second_index_diff = i
        # check if swap is possible
        return (
            s1[first_index_diff] == s2[second_index_diff]
            and s1[second_index_diff] == s2[first_index_diff]
        )
