from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # right contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the right would be 1
        right = 1
        for i in reversed(range(length)):
            # For the index 'i', right would contain the
            # product of all elements to the right. We update right accordingly
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer
