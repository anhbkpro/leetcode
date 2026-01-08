# Solution Notes - Python

| Problem # | Problem Name | Note | Tag | Difficulty | Time Complexity | Space Complexity |
|-----------|--------------|------|-----|------------|-----------------|------------------|
| 1161 | Maximum Level Sum of a Binary Tree | BFS approach: traverse tree level by level, calculate sum at each level, track maximum sum and return smallest level with maximum sum | Tree | Medium | O(n) | O(n) |
| 1339 | Maximum Product of Splitted Binary Tree | DFS approach: first compute total tree sum, then traverse tree tocalculate each subtree sum and track maximum product of split | DFS | Medium | O(n) | O(n) |
| 1390 | Four Divisors | Handles two cases: n = p³ (cube of prime) and n = p*q (product of two distinct primes) | Math, Number Theory | Medium | O(n * √max(nums)) | O(1) |
| 1458 | Max Dot Product of Two Subsequences | Dynamic programming with memoization: for each pair (i,j), considertaking both elements, skipping one, or skipping both to maximizedot product of subsequences | DP | Hard |  | O(n²) |
| 1975 | Maximum Matrix Sum | Greedy approach: sum absolute values, if odd negatives remain, subtract 2 * minimum absolute value | Greedy, Matrix | Medium | O(n²) | O(1) |

