from typing import List


class Solution:
    @staticmethod
    def find_duplicate(nums: List[int]) -> int:
        seen = set()
        for item in nums:
            if item in seen:
                return item
            seen.add(item)

    @staticmethod
    def find_duplicate_using_floyd_tortoise_and_hare(nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
