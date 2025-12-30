import heapq
from collections import defaultdict, deque


class BFSSolution:
    def networkDelayTime(self, times, n, k):
        # Adjacency list
        adj = defaultdict(list)

        def bfs(signal_received_at, source_node):
            q = deque()
            q.append(source_node)

            # Time for starting node is 0
            signal_received_at[source_node] = 0

            while q:
                curr_node = q.popleft()

                if curr_node not in adj:
                    continue

                # Broadcast the signal to adjacent nodes
                for time, neighbor_node in adj[curr_node]:
                    # Fastest signal time for neighbor_node so far
                    # signal_received_at[curr_node] + time :
                    # time when signal reaches neighbor_node
                    arrival_time = signal_received_at[curr_node] + time
                    if signal_received_at[neighbor_node] > arrival_time:
                        signal_received_at[neighbor_node] = arrival_time
                        q.append(neighbor_node)

        # Build the adjacency list
        for source, dest, travel_time in times:
            adj[source].append((travel_time, dest))

        signal_received_at = [float("inf")] * (n + 1)

        bfs(signal_received_at, k)

        answer = -float("inf")
        for i in range(1, n + 1):
            answer = max(answer, signal_received_at[i])

        # float('inf') signifies at least one node is unreachable
        return -1 if answer == float("inf") else answer


class DijkstraSolution:
    def networkDelayTime(self, times, n, k):
        # Adjacency list
        adj = defaultdict(list)

        def dijkstra(signal_received_at, source, n):
            # Priority queue to store (time, node) pairs
            pq = [(0, source)]

            # Time for starting node is 0
            signal_received_at[source] = 0

            while pq:
                curr_node_time, curr_node = heapq.heappop(pq)

                if curr_node_time > signal_received_at[curr_node]:
                    continue

                if curr_node not in adj:
                    continue

                # Broadcast the signal to adjacent nodes
                for time, neighbor_node in adj[curr_node]:
                    # Fastest signal time for neighbor_node so far
                    # signal_received_at[curr_node] + time :
                    # time when signal reaches neighbor_node
                    if signal_received_at[neighbor_node] > curr_node_time + time:
                        signal_received_at[neighbor_node] = curr_node_time + time
                        heapq.heappush(
                            pq, (signal_received_at[neighbor_node], neighbor_node)
                        )

        # Build the adjacency list
        for source, dest, travel_time in times:
            adj[source].append((travel_time, dest))

        signal_received_at = [float("inf")] * (n + 1)

        dijkstra(signal_received_at, k, n)

        answer = -float("inf")
        for i in range(1, n + 1):
            answer = max(answer, signal_received_at[i])

        # float('inf') signifies at least one node is unreachable
        return -1 if answer == float("inf") else answer
