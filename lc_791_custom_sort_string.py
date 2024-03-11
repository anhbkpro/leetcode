from collections import Counter


class Solution:
    @staticmethod
    def custom_sort_string(order: str, s: str) -> str:
        s_counter = Counter(s)
        o_counter = Counter(order)
        ans = []
        seen = set()
        for c in order:
            if c in s_counter:
                ans += [c] * s_counter[c]
                seen.add(c)
        remaining = []
        for c in s:
            if c not in o_counter and c not in seen:
                remaining += [c] * s_counter[c]
                seen.add(c)

        ans += remaining
        return "".join(ans)
