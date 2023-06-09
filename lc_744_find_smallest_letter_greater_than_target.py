from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]


class Solution:
    pass
