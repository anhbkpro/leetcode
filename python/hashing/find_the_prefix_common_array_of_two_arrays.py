from typing import Counter, List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = Counter()
        ans = []
        for a, b in zip(A, B):
            common[a] += 1
            common[b] += 1
            cnt = len([x for x in common if common[x] == 2])
            ans.append(cnt)

        return ans
