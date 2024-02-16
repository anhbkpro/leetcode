import heapq
from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def find_least_num_of_unique_ints(arr: List[int], k: int) -> int:
        freq = Counter(arr)
        least_frequency_numbers = heapq.nsmallest(k, freq.keys(), freq.get)

        index = 0
        while k > 0 and least_frequency_numbers:
            item = least_frequency_numbers[index]
            to_removed_count = min(k, freq[item])
            k -= to_removed_count
            freq[item] -= to_removed_count
            if freq[item] == 0:
                del freq[item]
            index += 1

        return len(freq)
