from typing import List


class Solution:
    @staticmethod
    def find132pattern(nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        # nums = [6, 12, 3, 4, 6, 11, 20]
        # min_array = [6, 6, 3, 3, 3, 3, 3]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        print(f"min_array: {min_array}")
        for j in range(len(nums) - 1, -1, -1):
            print(f"=== j={j}, nums[{j}]={nums[j]}")
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                print(f"pop {stack[-1]} off stack")
                stack.pop()
            if stack and stack[-1] < nums[j]:
                print(f"found 132 pattern: {min_array[j]} < {stack[-1]} < {nums[j]}")
                return True
            stack.append(nums[j])
            print(f"stack: {stack}")
        return False
