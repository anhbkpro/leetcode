from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for k in range(len(nums)):
            num = nums[k]
            num_str = str(num)
            order = ""
            for i in range(len(num_str)):
                order = order + str(mapping[int(num_str[i])])

            pairs.append((int(order), k))

        pairs.sort()
        ans = []
        for _, i in pairs:
            ans.append(nums[i])

        return ans
