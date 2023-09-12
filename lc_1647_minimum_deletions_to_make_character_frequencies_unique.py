import collections


class Solution:
    @staticmethod
    def min_deletions(s: str) -> int:
        c = collections.Counter(s)
        c = sorted(c.items(), key=lambda x: -x[1])  # sort by frequency in descending order
        print(c)  # "ceabaacb" => [('a', 3), ('c', 2), ('b', 2), ('e', 1)]
        frequency = {}
        delete_count = 0
        for k, v in c:
            print(k, v)
            if v not in frequency:
                frequency[v] = True
            else:
                while v and v in frequency:  # frequency of 0 is ignored
                    v -= 1
                    delete_count += 1

                frequency[v] = True

        print(frequency)
        return delete_count
