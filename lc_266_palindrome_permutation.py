import collections


def can_permute_palindrome(s: str) -> bool:
    counter = collections.Counter(s)
    num_odds = 0

    for item in counter:
        if counter[item] % 2 is not 0:
            num_odds += 1

    return num_odds <= 1


class Solution:
    pass
