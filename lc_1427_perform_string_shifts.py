from typing import List


def string_shift(string: str, shift: List[List[int]]) -> str:
    for direction, amount in shift:
        if direction == 0:
            string = string[amount:] + string[:amount]
        else:
            string = string[-amount:] + string[:-amount]
    return string


class Solution:
    pass
