from collections import defaultdict, deque
from typing import List


class Solution:
    @staticmethod
    def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        prices = [float('inf')] * n
        # save node and minimum total_cost to travel to the node until now
        dq = deque([(src, 0)])
        stops = 0
        for source, destination, cost in flights:
            adj[source].append((destination, cost))

        while stops <= k and dq:
            size = len(dq)
            while size > 0:
                size -= 1
                node, total_cost = dq.popleft()

                # there are no neighbours of this node
                if not adj[node]:
                    continue

                for neighbour, price in adj[node]:
                    # only update cost to travel to this node if
                    # the cost is cheaper
                    if price + total_cost >= prices[neighbour]:
                        continue

                    prices[neighbour] = price + total_cost
                    dq.append((neighbour, prices[neighbour]))
            stops += 1

        return -1 if prices[dst] == float('inf') else prices[dst]
