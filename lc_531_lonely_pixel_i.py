from collections import Counter
from typing import List


def findLonelyPixel(picture: List[List[str]]) -> int:
    m = len(picture)
    n = len(picture[0])

    lonely_rows = [-1] * m
    lonely_cols = [False] * n

    for row in range(m):
        r_counter = Counter(picture[row])
        if 'B' in r_counter and r_counter['B'] == 1:
            b_index = picture[row].index('B')
            lonely_rows[row] = b_index

    for col in range(n):
        current_col = []
        for row in picture:
            current_col.append(row[col])
        c_counter = Counter(current_col)
        if 'B' in c_counter and c_counter['B'] == 1:
            lonely_cols[col] = True

    ans = 0
    for row in range(m):
        if lonely_rows[row] >= 0 and lonely_cols[lonely_rows[row]]:
            ans += 1

    return ans


class Solution:
    pass
