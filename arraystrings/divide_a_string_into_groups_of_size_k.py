from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Divide a string into groups of size k, padding the last group with fill character if needed.

        Args:
            s: Input string to divide
            k: Size of each group
            fill: Character to fill the last group if it's incomplete

        Returns:
            List of strings, each of size k (except possibly the last one)
        """
        if not s:
            return []

        result = []
        # Process complete groups
        for i in range(0, len(s) - len(s) % k, k):
            result.append(s[i:i + k])

        # Handle the remaining characters
        remaining_start = len(s) - len(s) % k
        if remaining_start < len(s):
            remaining = s[remaining_start:]
            # Pad with fill character to make it size k
            remaining += fill * (k - len(remaining))
            result.append(remaining)

        return result
