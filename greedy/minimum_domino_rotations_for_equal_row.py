from typing import List


class Solution:
    def min_domino_rotations(self, top_row: List[int], bottom_row: List[int]) -> int:
        """
        Return the minimum number of rotations needed to make all the values in either the top or bottom row equal.
        If not possible, return -1.
        """
        n: int = len(top_row)
        rotations: int = self._get_min_rotations(top_row, bottom_row, n, top_row[0])
        if rotations != -1 or top_row[0] == bottom_row[0]:
            return rotations
        return self._get_min_rotations(top_row, bottom_row, n, bottom_row[0])

    def _get_min_rotations(
        self, top_row: List[int], bottom_row: List[int], n: int, target: int
    ) -> int:
        rotations_top: int = 0
        rotations_bottom: int = 0
        for i in range(n):
            if top_row[i] != target and bottom_row[i] != target:
                return -1
            if top_row[i] != target:
                rotations_top += 1
            elif bottom_row[i] != target:
                rotations_bottom += 1
        return min(rotations_top, rotations_bottom)
