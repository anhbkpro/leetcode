import string
from collections import defaultdict
from typing import List


def groupStrings(strings: List[str]) -> List[List[str]]:
    ans = []
    grouped_by_index = defaultdict(list)
    char_to_index = defaultdict(int)
    for i in range(len(string.ascii_lowercase)):
        char_to_index[string.ascii_lowercase[i]] = i

    # print(char_to_index)
    for s in strings:
        # print(s)
        group = []
        start_index = char_to_index[s[0]]
        for c in s:
            # az >> 0-25
            # ba >> 0--1 >> 0-25
            # 26 is the length of the alphabet, so we + 26 to avoid negative numbers,
            # `ba` means `0--1`, by adding 26 it will be converted to `0-25`, same group as `az`
            group.append((char_to_index[c] - start_index + 26) % 26)

        # print(group)
        group_str = "-".join(map(str, group))
        grouped_by_index[group_str].append(s)

    # print("grouped_by_index >> ", grouped_by_index)
    for item in grouped_by_index:
        # print('item=', item)
        ans.append(grouped_by_index[item])

    return ans


class Solution:
    pass
