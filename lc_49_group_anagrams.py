from collections import defaultdict


class Solution(object):
    @staticmethod
    def groupAnagrams(strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
