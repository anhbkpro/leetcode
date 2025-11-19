from typing import List


class SolutionSlidingWindow:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


class SolutionDictionary:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        return False
