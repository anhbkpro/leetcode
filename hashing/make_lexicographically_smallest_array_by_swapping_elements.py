from collections import deque
from typing import Dict, List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)

        group_idx = 0
        num_to_group: Dict[int, int] = {}
        num_to_group[sorted_nums[0]] = group_idx
        group_to_list: Dict[int, List[int]] = {}
        group_to_list[group_idx] = deque([sorted_nums[0]])

        for i in range(1, len(sorted_nums)):
            num = sorted_nums[i]
            if abs(num - sorted_nums[i - 1]) > limit:
                group_idx += 1
            curr_group_list = group_to_list.get(group_idx)
            if not curr_group_list:
                curr_group_list = deque()
            curr_group_list.append(num)
            group_to_list[group_idx] = curr_group_list
            num_to_group[num] = group_idx

        print(num_to_group)
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums
