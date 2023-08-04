from functools import cache
from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True

            return False

        return dp(len(s) - 1)
