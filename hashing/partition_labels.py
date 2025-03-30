from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        merged = []
        char_to_index_pairs = {}
        for index, c in enumerate(s):
            if c not in char_to_index_pairs:
                char_to_index_pairs[c] = [index, index]
            else:
                char_to_index_pairs[c][-1] = index
        index_pairs = list(char_to_index_pairs.values())
        index_pairs.sort()
        merged.append(index_pairs[0])
        for start, end in index_pairs[1:]:
            if merged[-1][-1] > start:
                merged[-1][-1] = max(merged[-1][-1], end)
            else:
                merged.append([start, end])
        return [end - start + 1 for start, end in merged]
