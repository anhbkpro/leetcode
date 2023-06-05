from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for x, y in coordinates[2:]:
            if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
                return False

        return True
