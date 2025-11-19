from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        indegree = [0] * n

        # Build adjacency list and calculate indegrees
        for edge in edges:
            adj[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        # count[i][j] represents the maximum count of color j ending at node i
        count = [[0] * 26 for _ in range(n)]
        q = deque()

        # Push all nodes with indegree zero to the queue
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        answer = 1
        nodes_seen = 0

        while q:
            node = q.popleft()
            # Update count for current node's color and track maximum
            color_index = ord(colors[node]) - ord("a")
            count[node][color_index] += 1
            answer = max(answer, count[node][color_index])
            nodes_seen += 1

            # Process all neighbors
            for neighbor in adj[node]:
                # Update color counts for the neighbor
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[node][i])

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Return -1 if cycle detected, otherwise return the answer
        return -1 if nodes_seen < n else answer
