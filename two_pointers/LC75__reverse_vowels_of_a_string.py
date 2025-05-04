# 345. Reverse Vowels of a String
from typing import Set

VOWELS: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


class Solution:
    def is_vowel(self, ch: str) -> bool:
        """Check if a character is a vowel."""
        return ch in VOWELS

    def reverse_vowels(self, s: str) -> str:
        """Reverse only the vowels in a string."""
        arr: list[str] = list(s)
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            left = self._find_next_vowel(arr, left, right)
            right = self._find_prev_vowel(arr, left, right)
            if left >= right:
                break
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return "".join(arr)

    def _find_next_vowel(self, arr: list[str], left: int, right: int) -> int:
        while left < right and not self.is_vowel(arr[left]):
            left += 1
        return left

    def _find_prev_vowel(self, arr: list[str], left: int, right: int) -> int:
        while right > left and not self.is_vowel(arr[right]):
            right -= 1
        return right
