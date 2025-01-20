from typing import List, Dict, Tuple


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        Finds the first index in the array where either a complete row or column
        in the matrix has been marked.

        :param arr: List of integers representing the order of marking.
        :param mat: 2D list representing the matrix.
        :return: The first index where a row or column is completely filled, or -1 if none.
        """
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * m, [0] * n
        num_to_pos: Dict[int, Tuple[int, int]] = {
            mat[r][c]: (r, c) for r in range(m) for c in range(n)
        }

        for i, num in enumerate(arr):
            r, c = num_to_pos[num]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i

        return -1
