from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def findWinners(matches: List[List[int]]) -> List[List[int]]:
        won_count = defaultdict()
        for match in matches:
            won_count.setdefault(match[0], 1)
            won_count.setdefault(match[1], 1)

        for match in matches:
            if match[1] in won_count:
                if won_count[match[1]] == 0:
                    del won_count[match[1]]
                    continue

                won_count[match[1]] -= 1

        return [sorted([k for k in won_count if won_count[k] == 1]),
                sorted([k for k in won_count if won_count[k] == 0])]

