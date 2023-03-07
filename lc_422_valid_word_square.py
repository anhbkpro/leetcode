from typing import List


def validWordSquare(words: List[str]) -> bool:
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                return False
    return True


class Solution:
    pass
