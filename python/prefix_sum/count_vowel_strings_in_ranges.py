from functools import lru_cache
from typing import List, Set


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Class constants
        VOWELS: Set[str] = {"a", "e", "i", "o", "u"}

        @lru_cache(maxsize=None)
        def is_vowel_string(word: str) -> bool:
            """
            Check if a string starts and ends with a vowel.
            Using lru_cache to memoize results for repeated words.
            """
            return word[0] in VOWELS and word[-1] in VOWELS

        def build_prefix_sum(words: List[str]) -> List[int]:
            """
            Build a prefix sum array where each element represents the cumulative
            count of valid vowel strings up to that index.
            """
            prefix = [0] * (len(words) + 1)
            for i, word in enumerate(words, 1):
                prefix[i] = prefix[i - 1] + (1 if is_vowel_string(word) else 0)
            return prefix

        def process_queries(prefix: List[int], queries: List[List[int]]) -> List[int]:
            """
            Process each query using the prefix sum array to get the count of
            valid strings in the given range.
            """
            return [prefix[right + 1] - prefix[left] for left, right in queries]

        # Main execution flow
        prefix_sums = build_prefix_sum(words)
        return process_queries(prefix_sums, queries)
