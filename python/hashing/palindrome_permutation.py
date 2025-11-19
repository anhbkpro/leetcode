from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """Determine if a string can be rearranged to form a palindrome.

        A string can be rearranged to form a palindrome if and only if at most one character
        appears an odd number of times. Case sensitive, treats spaces and special characters
        as distinct characters.

        Args:
            s: Input string

        Returns:
            True if string can be rearranged to form palindrome, False otherwise
        """
        if not s:
            return True

        count = Counter(s)
        # For a string to be a palindrome, at most one character can have an odd count
        odds = sum(1 for val in count.values() if val % 2 == 1)
        return odds <= 1
