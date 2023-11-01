class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # The idea is to use BFS to find the shortest path from (0, 0) to (x, y).
        # We can use a set to store the visited positions, and a queue to store
        # the positions to be visited.
        visited = set()
        queue = [(0, 0)]
        steps = 0

        while queue:
            # For each position in the queue, we check if it is the target position.
            # If it is, we return the current step.
            # Otherwise, we add its neighbors to the queue.
            for _ in range(len(queue)):  # iterate through the current level
                pos = queue.pop(0)
                if pos == (x, y):
                    return steps

                for neighbor in self.get_neighbors(pos):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            # move on to the next level
            steps += 1

    @staticmethod
    def get_neighbors(pos):
        # There are 8 possible neighbors for each position.
        # We can use a list of offsets to get the neighbors.
        offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        neighbors = []
        for offset in offsets:
            neighbors.append((pos[0] + offset[0], pos[1] + offset[1]))
        return neighbors
