from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)
        # to indicate whether each box can be opened
        can_open = [status[x] == 1 for x in range(n)]
        # to indicate whether each box is owned
        has_box, used = [False] * n, [False] * n
        q = deque()
        ans = 0

        for box in initialBoxes:
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                used[box] = True
                ans += candies[box]

        while q:
            # For the i-th box, we can only obtain the candies inside if we own the box (either from the beginning or from some other box)
            # and can open it (either it is already open from the beginning or we have obtained the key to it).
            big_box = q.popleft()
            for key in keys[big_box]:
                # we can open the box with the key
                can_open[key] = True
                # we can obtain the box with the key
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    ans += candies[key]

            for box in containedBoxes[big_box]:
                # we can obtain the box from the big box
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans += candies[box]

        return ans
