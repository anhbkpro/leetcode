class Solution:
    def dfs(self, node, edges, dist, visit):
        visit[node] = True
        neighbor = edges[node]
        if neighbor != -1 and not visit[neighbor]:
            dist[neighbor] = 1 + dist[node]
            self.dfs(neighbor, edges, dist, visit)

    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        dist1 = [float("inf")] * n
        dist2 = [float("inf")] * n
        visit1 = [False] * n
        visit2 = [False] * n

        dist1[node1] = 0
        dist2[node2] = 0

        self.dfs(node1, edges, dist1, visit1)
        self.dfs(node2, edges, dist2, visit2)

        min_dist_node = -1
        min_dist_till_now = float("inf")

        for curr_node in range(n):
            max_dist = max(dist1[curr_node], dist2[curr_node])
            if min_dist_till_now > max_dist:
                min_dist_node = curr_node
                min_dist_till_now = max_dist

        return min_dist_node
