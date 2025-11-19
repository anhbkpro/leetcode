from typing import List


class Solution:
    @staticmethod
    def find_farmland(land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        ans = []
        visited_farm = set()

        def dfs(r: int, c: int, max_x: int, max_y: int):
            """
            Find the right corner of farm land
            :param r: row
            :param c: column
            :param max_x: max row
            :param max_y: max column
            :return: max row and max column
            """
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] != 1:
                # if out of bound or not farm land
                return max_x, max_y

            land[r][c] = 0  # mark as visited
            max_x = max(r, max_x)
            max_y = max(c, max_y)
            # print(f"--- found farm land at [{r}, {c}]")
            data = dfs(r + 1, c, max_x, max_y)
            max_x = max(max_x, data[0])
            max_y = max(max_y, data[1])
            data = dfs(r - 1, c, max_x, max_y)
            max_x = max(max_x, data[0])
            max_y = max(max_y, data[1])
            data = dfs(r, c + 1, max_x, max_y)
            max_x = max(max_x, data[0])
            max_y = max(max_y, data[1])
            data = dfs(r, c - 1, max_x, max_y)
            max_x = max(max_x, data[0])
            max_y = max(max_y, data[1])
            return max_x, max_y

        for r in range(m):
            for c in range(n):
                min_x = r
                min_y = c
                max_x = r
                max_y = c
                if land[r][c] == 1:  # found left corner of farm
                    # print(f"start farm [{r}, {c}]")
                    min_x = min(min_x, r)
                    min_y = min(min_y, c)
                    max_x, max_y = dfs(r, c, max_x, max_y)  # find right corner of farm
                    # print(f"end farm [{max_x}, {max_y}]")
                    if (min_x, min_y) not in visited_farm:
                        visited_farm.add((r, c))
                        ans.append([min_x, min_y, max_x, max_y])
        return ans
