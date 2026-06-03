# 3635. Earliest Finish Time for Land and Water Rides II

[LeetCode problem](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/) · Medium

## Problem

A tourist must complete exactly one land ride and one water ride, in either order. Each ride has an earliest boarding time and a duration. A ride started at time `t` finishes at `t + duration`. The tourist may wait if the second ride hasn't opened yet.

Return the **earliest possible finish time** across all choices of rides and orderings.

## Approach

### Brute force — O(n × m)

Try every `(land_i, water_j)` pair in both orderings. Too slow when `n` and `m` are large.

### Optimized — O(n + m)

**Key observation:** for fixed water ride `j`, doing land-first gives:

```
finish = max(land_end[i], water_start[j]) + water_dur[j]
```

Because `max(x, c)` is non-decreasing in `x`, this is minimized by taking the **globally smallest `land_end[i]`** — no need to pair every `i` with every `j`.

The same argument applies symmetrically for water-first order.

**Algorithm:**

```
min_land_end  = min(land_start[i]  + land_dur[i])   for all i
min_water_end = min(water_start[j] + water_dur[j])  for all j

land_first  = min over j: max(min_land_end,  water_start[j]) + water_dur[j]
water_first = min over i: max(min_water_end, land_start[i])  + land_dur[i]

answer = min(land_first, water_first)
```

### Complexity

| | Time | Space |
|---|---|---|
| Brute force | O(n × m) | O(1) |
| Optimized | **O(n + m)** | **O(1)** |

## Visualization

The widget below renders every plan on a timeline — blue bars are land rides, green bars are water rides, gray gaps are wait time. The best plan is highlighted.

```
landStartTime = [2, 8]   landDuration = [4, 1]
waterStartTime = [6]     waterDuration = [3]

t:  0    2    4    6    8    10   12
         [L0──────]
                   [W0──]           ← L0→W0: finish = 9  ✓ best
                        [L1]
                   [W0──]
                             [L1]   ← W0→L1: finish = 10
         [L0──────]
              [···][W0──]           ← W0→L0: finish = 13  (wait before W0)
    [W0──────][···][L0──────]
         [L1][W0──]                 ← L1→W0: finish = 12
```

## Solution

```python
def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
    min_land_end  = min(s + d for s, d in zip(landStartTime,  landDuration))
    min_water_end = min(s + d for s, d in zip(waterStartTime, waterDuration))

    # Land first, then water
    land_first  = min(max(min_land_end,  ws) + wd for ws, wd in zip(waterStartTime, waterDuration))

    # Water first, then land
    water_first = min(max(min_water_end, ls) + ld for ls, ld in zip(landStartTime,  landDuration))

    return min(land_first, water_first)
```

## Worked Examples

### Example 1

```
landStartTime = [2, 8]   landDuration = [4, 1]   → land_end = [6, 9]   min_land_end  = 6
waterStartTime = [6]     waterDuration = [3]      → water_end = [9]     min_water_end = 9
```

| Order | Calculation | Finish |
|---|---|---|
| land → water (j=0) | max(6, 6) + 3 | **9** |
| water → land (i=0) | max(9, 2) + 4 | 13 |
| water → land (i=1) | max(9, 8) + 1 | 10 |

**Answer: 9**

### Example 2

```
landStartTime = [5]   landDuration = [3]    → land_end = [8]    min_land_end  = 8
waterStartTime = [1]  waterDuration = [10]  → water_end = [11]  min_water_end = 11
```

| Order | Calculation | Finish |
|---|---|---|
| land → water (j=0) | max(8, 1) + 10 | 18 |
| water → land (i=0) | max(11, 5) + 3 | **14** |

**Answer: 14**
