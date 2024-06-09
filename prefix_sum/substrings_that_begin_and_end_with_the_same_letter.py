class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        prefix_count = [0] * 26

        for i in range(n):
            # Increment the number of times we encountered the current letter so far.
            prefix_count[ord(s[i]) - ord('a')] += 1

            # Current letter can be paired with all the occurrences of it that
            # comes before, including itself, to form a valid substring.
            count += prefix_count[ord(s[i]) - ord("a")]

        return count
