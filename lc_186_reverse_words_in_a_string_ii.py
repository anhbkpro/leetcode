from typing import List


def reverse(l: list, left: int, right: int) -> None:
    while left < right:
        l[left], l[right] = l[right], l[left]
        left, right = left + 1, right - 1


def reverse_each_word(l: list) -> None:
    n = len(l)
    start = end = 0

    while start < n:
        # go to the end of the word
        while end < n and l[end] != ' ':
            end += 1
        # reverse the word
        reverse(l, start, end - 1)
        # move to the next word
        start = end + 1
        end += 1


def reverse_words(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # reverse the whole string
    reverse(s, 0, len(s) - 1)

    # reverse each word
    reverse_each_word(s)


class Solution:
    pass
