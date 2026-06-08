from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0] * len(nums)
        less = 0
        greater = len(nums) - 1
        for i, j in zip[tuple[int, int]](range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less] = nums[i]
                less += 1
            if nums[j] > pivot:
                ans[greater] = nums[j]
                greater -= 1
        while less <= greater:
            ans[less] = pivot
            less += 1

        return ans


    def pivotArray2(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = list[int]()
        equal_pivot = list[int]()
        greater_than_pivot = list[int]()
        ans = list[int]()
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_pivot.append(num)
            else:
                greater_than_pivot.append(num)
        ans.extend(less_than_pivot)
        ans.extend(equal_pivot)
        ans.extend(greater_than_pivot)
        return ans
