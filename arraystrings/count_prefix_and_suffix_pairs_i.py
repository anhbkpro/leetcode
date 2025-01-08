from typing import List


class Solution:
    def isPrefixAndSuffix(self, str1, str2) -> bool:
        if len(str1) > len(str2):
            return False
        return str2[: len(str1)] == str1 and str2[-len(str1) :] == str1

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(1, len(words)):
            for j in range(i):
                if self.isPrefixAndSuffix(words[j], words[i]):
                    ans += 1

        return ans
