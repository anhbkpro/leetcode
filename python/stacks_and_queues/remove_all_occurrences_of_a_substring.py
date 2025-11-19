from collections import Counter


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if not part:
            return s

        sub_len = len(part)
        stack = []
        s_counter = Counter(s)
        part_counter = Counter(part)
        for c in s:
            stack.append(c)
            if (
                c == part[-1]
                and len(stack) >= sub_len
                and s_counter[c] >= part_counter[c]
            ):
                sub_stack = "".join(stack[-sub_len:])
                if sub_stack == part:
                    for _ in range(sub_len):
                        stack.pop()

                continue
        return "".join(stack)
