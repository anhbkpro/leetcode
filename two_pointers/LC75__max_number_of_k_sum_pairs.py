from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p_left = 0
        p_right = len(nums) - 1
        pairs = 0
        while p_left < p_right:
            if nums[p_left] + nums[p_right] == k:
                p_left += 1
                p_right -= 1
                pairs += 1
            elif nums[p_left] + nums[p_right] > k:
                p_right -= 1
            else:
                p_left += 1

        return pairs

    def maxOperationsWithHashmap(self, nums: List[int], k: int) -> int:
        count_map = {}
        count = 0

        # Build the hashmap with count of occurrence of every element in array
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        for num in nums:
            current = num
            complement = k - num

            if count_map.get(current, 0) > 0 and count_map.get(complement, 0) > 0:
                if current == complement and count_map[current] < 2:
                    continue

                count_map[current] -= 1
                count_map[complement] -= 1
                count += 1

        return count
