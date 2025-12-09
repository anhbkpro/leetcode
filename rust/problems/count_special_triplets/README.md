# Summary: Count Special Triplets

This solution counts triplets `(i, j, k)` where `i < j < k` and `nums[i] == nums[k] == 2 * nums[j]`.

## Approach: Two Hash Maps (One Pass)

The algorithm uses a clever counting technique with two hash maps:

1. **`num_cnt`** — Pre-counts the total occurrences of each number in the array
2. **`num_partial_cnt`** — Tracks occurrences seen so far (elements to the left)

## Key Logic

For each element `v` at index `j`:

- **Target** = `v * 2` (the value that `nums[i]` and `nums[k]` must equal)
- **`l_cnt`** = count of `target` to the **left** of `j` (from `num_partial_cnt`)
- **`r_cnt`** = count of `target` to the **right** of `j` (calculated as `total - partial`)
- **Add** `l_cnt × r_cnt` to the answer (all valid combinations)

### Example Walkthrough

For `[6, 3, 6]`:

- At `j=1` (value 3): target = 6, left has one 6, right has one 6 → **1 triplet**

## Complexity

- **Time:** O(n) — single pass after preprocessing
- **Space:** O(n) — for the hash maps


# Example Walkthrough: `[8, 4, 2, 8, 4]`

## Initial Setup

- **`num_cnt`** = `{8: 2, 4: 2, 2: 1}` (pre-computed total counts)
- **`num_partial_cnt`** = `{}` (empty)
- **`ans`** = 0

---

## Iteration-by-Iteration

| Step | `v` (j) | target | `l_cnt` | `r_cnt` | Contribution | `ans` |
|------|---------|--------|---------|---------|--------------|-------|
| 1 | 8 (idx 0) | 16 | 0 | 0 | 0 × 0 = 0 | 0 |
| 2 | 4 (idx 1) | 8 | 1 | 1 | 1 × 1 = **1** | 1 |
| 3 | 2 (idx 2) | 4 | 1 | 1 | 1 × 1 = **1** | 2 |
| 4 | 8 (idx 3) | 16 | 0 | 0 | 0 × 0 = 0 | 2 |
| 5 | 4 (idx 4) | 8 | 2 | 0 | 2 × 0 = 0 | 2 |

---

## Detailed Breakdown

**Step 2** (`v = 4` at index 1):

- target = 8
- Left 8s: 1 (index 0)
- Right 8s: total(2) - seen(1) = 1 (index 3)
- **Triplet found:** `(0, 1, 3)` → `[8, 4, 8]` ✓

**Step 3** (`v = 2` at index 2):

- target = 4
- Left 4s: 1 (index 1)
- Right 4s: total(2) - seen(1) = 1 (index 4)
- **Triplet found:** `(1, 2, 4)` → `[4, 2, 4]` ✓

---

## Valid Triplets

1. **(0, 1, 3):** `nums[0]=8`, `nums[1]=4`, `nums[3]=8` → `8 == 4×2 == 8` ✓
2. **(1, 2, 4):** `nums[1]=4`, `nums[2]=2`, `nums[4]=4` → `4 == 2×2 == 4` ✓

**Final Answer: 2**

