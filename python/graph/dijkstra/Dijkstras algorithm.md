# Dijkstra's Algorithm
Dijkstra’s algorithm solves the `single-source shortest path` problem in a weighted directed graph with non-negative weights.

## The Main Idea
We take the starting point u as the center and gradually expand outward while updating the `shortest path` to reach other vertices.

Dijkstra's Algorithm uses a `greedy approach`. Each step selects the `minimum weight` from the currently reached vertices to find the `shortest path` to other vertices.

Dijkstra’s algorithm is a `greedy algorithm` that uses a `min-heap` (priority queue) to process nodes in `increasing` order of their shortest known distance. The algorithm starts from the source node, which is node `0`, and initializes its distance to `0` while setting the distance for all other nodes to infinity. The priority queue ensures that the node with the shortest known distance is always processed first.

## Steps of the Algorithm
1. Build an adjacency list representation of the graph.
2. Initialize the distance of the source node to `0` and all other nodes to `infinity`.
3. Use a priority queue to process nodes in increasing order of their shortest known distance.
4. For each node, explore its neighbors and update their shortest distances if a shorter path is found. We start with the source node as the first node get from the priority queue. If we find a shorter path to a node, we update the distance and add the node to the priority queue.
5. Repeat the process until all nodes have been processed.

## Time Complexity
The time complexity of Dijkstra's algorithm is `O((V + E) log V)`, where `V` is the number of vertices and `E` is the number of edges in the graph.

## Space Complexity
The space complexity of Dijkstra's algorithm is `O(V)` for the distance array and `O(V)` for the priority queue.

## Limitation of the Algorithm
Dijkstra's Algorithm can only be used on graphs that satisfy the following condition:

- Weights of all edges are non-negative.
