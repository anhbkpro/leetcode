import collections


# My solution:
class Solution:
    @staticmethod
    def min_deletions(s: str) -> int:
        c = collections.Counter(s)
        print(c)
        c = sorted(c.items(), key=lambda x: -x[1])  # sort by frequency
        seen_count = {}
        count = 0
        for k, v in c:
            print(k)
            print(v)
            if v not in seen_count:
                seen_count[v] = True
            else:
                freq = v - 1
                count += 1
                while freq in seen_count:
                    freq -= 1
                    count += 1

                if freq == 0:  # frequency of 0 is ignored
                    continue

                seen_count[freq] = True

        print(seen_count)
        return count
