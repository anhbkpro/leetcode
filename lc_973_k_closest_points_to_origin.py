import heapq
from typing import List


class Solution:
    @staticmethod
    def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
        distances = {index: (point[0]**2 + point[1]**2) for index, point in enumerate(points)}
        rv = heapq.nsmallest(k, distances.keys(), key = distances.get)
        return [points[item] for item in rv]
