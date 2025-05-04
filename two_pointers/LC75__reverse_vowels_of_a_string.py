# 345. Reverse Vowels of a String
class Solution:
    def __init__(self):
        self.vowels = set(["a", "e", "i", "u", "o", "A", "E", "I", "U", "O"])

    def is_vowel(self, ch) -> bool:
        return ch in self.vowels

    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < len(arr) - 1 and not self.is_vowel(arr[left]):
                left += 1

            while right > 0 and not self.is_vowel(arr[right]):
                right -= 1

            if left >= right:
                break

            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return "".join(arr)
