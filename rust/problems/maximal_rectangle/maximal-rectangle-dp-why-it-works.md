# Why the DP + Upward Scan Approach Works

**LeetCode 85 – Maximal Rectangle**

---

## Problem Summary

Given a binary matrix, find the **largest rectangle consisting entirely of `'1'`s** and return its area.

A rectangle is defined by:

* a **bottom-right corner**
* a **width**
* a **height**

---

## High-Level Idea

> **Every maximal rectangle has a unique bottom-right corner.**

This solution:

1. Fixes each cell as a potential **bottom-right corner**
2. Computes how wide a rectangle can be at that cell
3. Expands **upward** to try all possible heights
4. Tracks the maximum valid area

---

## Step 1: Meaning of `dp[r][c]`

We define:

```
dp[r][c] = number of consecutive '1's ending at (r, c) in the same row
```

Example:

```
Matrix row:  1 1 0 1 1 1
dp values:   1 2 0 1 2 3
```

This means:

* Any rectangle ending at `(r, c)` **cannot be wider than `dp[r][c]`**
* Width is constrained by horizontal continuity

---

## Step 2: Fix the Bottom-Right Corner

For every cell `(r, c)` where `matrix[r][c] == '1'`, assume:

```
(r, c) is the bottom-right corner of a rectangle
```

Now we try to find the **largest rectangle that ends exactly here**.

---

## Step 3: Expand Upward (Key Insight)

We move upward row by row:

```
k = r, r-1, r-2, ..., 0
```

At each row `k`:

* **Height** = `r - k + 1`
* **Width** = minimum of `dp[k][c]` over rows `k..r`

Why the minimum?

> All rows must support the rectangle width.
> One narrow row limits the entire rectangle.

So we compute:

```
width = min(width, dp[k][c])
area = width × height
```

---

## Visual Example

Matrix:

```
1 0 1 1
1 1 1 1
1 1 1 0
```

Computed `dp`:

```
1 0 1 2
1 2 3 4
1 2 3 0
```

Consider bottom-right corner `(r=1, c=3)`:

| Top Row (k) | Width      | Height | Area |
| ----------- | ---------- | ------ | ---- |
| 1           | 4          | 1      | 4    |
| 0           | min(4,2)=2 | 2      | 4    |

Best rectangle ending at `(1,3)` has area `4`.

---

## Why This Finds All Valid Rectangles

For a fixed `(r, c)`:

* Any rectangle ending here must have:

  * a top boundary `k`
  * a width supported by **all rows `k..r`**
* The algorithm tries **every possible `k`**
* Therefore, **no rectangle ending at `(r,c)` is missed**

Repeating this for all `(r,c)` ensures:

> **Every rectangle in the matrix is considered exactly once**

---

## Why Invalid Rectangles Are Automatically Excluded

If any row has a `'0'`:

* `dp[k][c] = 0`
* width becomes `0`
* area becomes `0`

Invalid rectangles are naturally discarded.

---

## Why This Algorithm Is Correct

**Formal reasoning:**

1. Every maximal rectangle has a unique bottom-right corner
2. For each bottom-right corner, all possible heights are explored
3. For each height, the maximum valid width is used
4. The maximum area across all candidates is tracked

Therefore, the algorithm examines **all possible valid rectangles**.

---

## Time and Space Complexity

* **Time:** `O(rows² × cols)`
* **Space:** `O(rows × cols)` for the DP table

This is correct but **not optimal** for very large matrices.

---

## Key Takeaway

> This approach converts a 2D rectangle problem into:
> “For each cell, what is the largest rectangle that ends here?”

It works because:

* `dp` enforces horizontal continuity
* upward scanning enforces vertical continuity
* `min(width)` guarantees rectangle validity

---

## Note on Optimization

For better performance, use:

* **Histogram + Monotonic Stack**
* Time complexity: `O(rows × cols)`

This DP approach is excellent for:

* Understanding the problem
* Interviews
* Step-by-step reasoning

---
