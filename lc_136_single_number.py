from typing import List


class SolutionBitManipulation:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


class SolutionMath:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


class SolutionListOperation:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []
        for num in nums:
            if num not in no_duplicate_list:
                no_duplicate_list.append(num)
            else:
                no_duplicate_list.remove(num)
        return no_duplicate_list.pop()


class SolutionHash:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = 1
        return hash_table.popitem()[0]
