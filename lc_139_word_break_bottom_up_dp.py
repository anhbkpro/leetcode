from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]

    @staticmethod
    def word_break(s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s), -1, -1):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue

                if s[i: i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break

        return dp[0]
