# 605. Can Place Flowers
from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0

        for i in range(len(flowerbed)):
            # Check if current plot is empty
            if flowerbed[i] == 0:
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt >= n:
                        return True

        return cnt >= n
