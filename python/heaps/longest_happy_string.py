import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        result = []
        while pq:
            count, ch = heapq.heappop(pq)
            count = -count
            if len(result) >= 2 and result[-1] == ch and result[-2] == ch:
                if not pq:
                    break
                tmp_count, tmp_ch = heapq.heappop(pq)
                result.append(tmp_ch)
                if tmp_count + 1 < 0:
                    heapq.heappush(pq, (tmp_count + 1, tmp_ch))
                heapq.heappush(pq, (-count, ch))
            else:
                count -= 1
                result.append(ch)
                if count > 0:
                    heapq.heappush(pq, (-count, ch))

        return "".join(result)
