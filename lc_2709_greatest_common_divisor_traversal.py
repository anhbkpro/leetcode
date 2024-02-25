from typing import List


class Solution:
    @staticmethod
    def can_traverse_all_pairs(nums: List[int]) -> bool:
        def find_set_leader(disjoint: list, x: int) -> int:
            if disjoint[x] == x:
                return x
            disjoint[x] = find_set_leader(disjoint, disjoint[x])
            return disjoint[x]

        def union_sets(disjoint: list, size: list, x: int, y: int):
            x_leader = find_set_leader(disjoint, x)
            y_leader = find_set_leader(disjoint, y)
            if x_leader == y_leader:
                return
            if size[x_leader] < size[y_leader]:
                disjoint[x_leader] = y_leader
                size[y_leader] += size[x_leader]
            else:
                disjoint[y_leader] = x_leader
                size[x_leader] += size[y_leader]

        num_elements = len(nums)
        if num_elements == 1:
            return True

        disjoint_set = list(range(num_elements))
        set_size = [1] * num_elements
        factor_first_occurrence = {}

        for i, num in enumerate(nums):
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:
                    if divisor in factor_first_occurrence:
                        union_sets(
                            disjoint_set, set_size, i, factor_first_occurrence[divisor]
                        )
                    else:
                        factor_first_occurrence[divisor] = i
                    while num % divisor == 0:
                        num //= divisor
                divisor += 1
            if num > 1:
                if num in factor_first_occurrence:
                    union_sets(disjoint_set, set_size, i, factor_first_occurrence[num])
                else:
                    factor_first_occurrence[num] = i

        return set_size[find_set_leader(disjoint_set, 0)] == num_elements
