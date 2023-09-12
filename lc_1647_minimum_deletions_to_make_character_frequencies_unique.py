import collections


class Solution:
    @staticmethod
    def min_deletions(s: str) -> int:
        c = collections.Counter(s)
        print(c)
        c = sorted(c.items(), key=lambda x: -x[1])
        seen_count = {}
        count = 0
        for k, v in c:
            print(k, v)
            if v not in seen_count:
                seen_count[v] = True
            else:
                while v in seen_count:
                    v -= 1
                    count += 1

                if v == 0:  # frequency of 0 is ignored
                    continue

                seen_count[v] = True

        print(seen_count)
        return count
