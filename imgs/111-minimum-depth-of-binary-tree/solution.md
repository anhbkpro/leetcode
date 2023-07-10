# Approach 1: Depth-First Search (DFS)
## Intuition
If you're not familiar with DFS, check out our [Explore Card](https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/).

We are given a binary tree; we must return the minimum number of nodes between the root and any leaf node, 
including both. 
Let's try to break this problem into subproblems; we need to return the answer from the root of the current tree; 
what if we know the answer considering the left and right child of the root node? 
If the minimum depth for the root node's 
left child is `x` and the minimum depth for the root node's right child is `y`, 
then the minimum depth for the whole tree with the root node will be `1 + min(x, y)`. 
The additional `+1` is for the current root node.

This way, we can divide the current problem into subproblems and then solve them using recursion. 
The base condition of this recursion would be when the node is `NULL`, in which case we should return `0`. 
One tricky thing that we need to consider is when one of the children is `NULL` and the other one isn't. 
We shouldn't move forward with recursion on the `NULL` child; if we do, 
we would return `0` due to the base condition and 
the count of nodes from the leaf node on the other side would be discarded as we are taking the minimum of the two. 
In case both children are `NULL`, it's fine to go into recursion as both would return `0`, 
and the minimum of the two won't cause an issue.

If we observe closely, we are first traversing to the deepest node and then backtrack to the parent node 
to find the minimum depth for it; hence, this process is actually Depth-First Search (DFS).

![image.png](./Depth-First%20Search%20(DFS).png)

## Algorithm
1. We will use the `dfs` method with `root` as an argument. 
2. The base condition of the recursion would be for the `NULL` node, in which case we should return `0`. 
3. If the left child of root is `NULL`, then we should return `1` + minimum depth for the right child of the root node, 
which is `1 + dfs(root.right)`. 
4. If the right child of root is `NULL`, then we should return `1` + minimum depth for the left child of the root node, 
which is `1 + dfs(root.left)`. 
5. If both child are non-null, then return `1 + min(dfs(root.left), dfs(root.right))`.

## Complexity Analysis
Here, `N` is the number of nodes in the binary tree.

- Time complexity: `O(N)`

We will traverse each node in the tree only once; hence, the total time complexity would be `O(N)`.

- Space complexity: `O(N)`

The only space required is the stack space; the maximum number of active stack calls would equal 
the maximum depth of the tree, which could equal the total number of nodes in the tree. 
Hence, the space complexity would equal `O(N)`.