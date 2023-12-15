from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def dest_city(paths: List[List[str]]) -> str:
        path_map = defaultdict(int)
        for src, dst in paths:
            path_map[src] += 1
            if dst not in path_map:
                path_map[dst] = 0

        return [dst for dst in path_map if path_map[dst] == 0][0]
