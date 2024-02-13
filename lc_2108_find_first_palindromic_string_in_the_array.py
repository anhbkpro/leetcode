from typing import List


class Solution:
    @staticmethod
    def firstPalindrome(words: List[str]) -> str:
        def is_palindrome(s: str) -> bool:
            lo, hi = 0, len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word

        return ""
