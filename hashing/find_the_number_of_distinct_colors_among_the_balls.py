from collections import defaultdict
from typing import List


class Solution:
    def distinctColors(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        ball_map = defaultdict(int)
        color_map = defaultdict(int)

        for ball, color in queries:
            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1

                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            ball_map[ball] = color
            color_map[color] += 1
            ans.append(len(color_map))

        return ans
