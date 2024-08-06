import heapq
from collections import Counter


class Solution:
    def minimum_pushes_sort(self, word: str) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord("a")] += 1

        freq.sort(reverse=True)
        total_pushes = 0
        for i in range(26):
            if freq[i] == 0:
                break
            total_pushes += (i // 8 + 1) * freq[i]

        return total_pushes

    def minimum_pushes_heap(self, word: str) -> int:
        # Frequency map to store count of each letter
        frequency_map = Counter(word)

        # Priority queue to store frequencies in descending order
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)

        total_pushes = 0
        index = 0

        # Calculate total number of presses
        while frequency_queue:
            total_pushes += (1 + (index // 8)) * (
                -heapq.heappop(frequency_queue)
            )
            index += 1
        return total_pushes
