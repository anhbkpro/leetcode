class Solution:
    def minChanges(self, s: str) -> int:
        # Initialize with first character
        current_char = s[0]

        consecutive_count = 0
        min_changes_required = 0

        # Iterate through each character
        for char in s:
            # If current character matches the previous sequence
            if char == current_char:
                consecutive_count += 1
                continue

            # If we have even count of characters, start new sequence
            if consecutive_count % 2 == 0:
                consecutive_count = 1
            # If odd count, we need to change current character
            else:
                consecutive_count = 0
                min_changes_required += 1

            # Update current character for next iteration
            current_char = char

        return min_changes_required


class GreedySolution:
    def minChanges(self, s: str) -> int:
        min_changes_required = 0

        # Check pairs of characters (i, i+1) with step size 2
        for i in range(0, len(s), 2):
            # If characters in current pair don't match,
            # we need one change to make them equal
            if s[i] != s[i + 1]:
                min_changes_required += 1
        return min_changes_required


"""
pythonic one liner:

class Solution:
    def minChanges(self, s: str) -> int:
        # Count changes needed for each unmatched pair
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
"""
