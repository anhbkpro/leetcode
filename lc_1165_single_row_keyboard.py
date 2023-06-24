from collections import defaultdict


def calculateTime(keyboard: str, word: str) -> int:
    char_to_index = defaultdict()
    for i in range(len(keyboard)):
        char_to_index[keyboard[i]] = i

    prev = 0
    ans = 0
    for i in range(len(word)):
        ans += abs(char_to_index[word[i]] - prev)
        prev = char_to_index[word[i]]

    return ans


class Solution:
    pass
