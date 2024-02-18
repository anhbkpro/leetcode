import heapq
from typing import List


class Solution:
    @staticmethod
    def find_relative_ranks(score: List[int]) -> List[str]:
        rank = []
        ans = [""] * len(score)
        for i, s in enumerate(score):
            heapq.heappush(rank, [-s, i])  # use max-heap to store highest to lowest scores

        score_index = 0
        while rank:
            r = heapq.heappop(rank)
            if score_index == 0:
                medal = "Gold Medal"
            elif score_index == 1:
                medal = "Silver Medal"
            elif score_index == 2:
                medal = "Bronze Medal"
            else:
                medal = f"{score_index + 1}"
            ans[r[1]] = medal
            score_index += 1

        return ans
