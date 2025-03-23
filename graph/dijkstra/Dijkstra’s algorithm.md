# Dijkstra's Algorithm
- “Dijkstra’s algorithm” solves the “single-source shortest path” problem in a weighted directed graph with non-negative weights.
## The Main Idea
We take the starting point u as the center and gradually expand outward while updating the “shortest path” to reach other vertices.

Dijkstra's Algorithm uses a `greedy approach`. Each step selects the `minimum weight` from the currently reached vertices to find the `shortest path` to other vertices.

## Limitation of the Algorithm
Dijkstra's Algorithm can only be used on graphs that satisfy the following condition:

- Weights of all edges are non-negative.
