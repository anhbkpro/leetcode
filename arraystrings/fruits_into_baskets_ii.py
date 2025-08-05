from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced_count = 0
        
        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                basket = baskets[i]
                if basket >= fruit and not used[i]:
                    used[i] = True
                    placed = True
                    break
            
            if not placed:
                unplaced_count += 1

        return unplaced_count