from collections import deque
from typing import List


class Solution:
    @staticmethod
    def getWinner(arr: List[int], k: int) -> int:
        max_element = max(arr)
        queue = deque(arr[1:])
        curr = arr[0]
        win_streak = 0

        while queue:
            opponent = queue.popleft()
            if curr > opponent:
                queue.append(opponent)
                win_streak += 1
            else:
                queue.append(curr)
                curr = opponent
                win_streak = 1

            if win_streak == k or curr == max_element:
                return curr
