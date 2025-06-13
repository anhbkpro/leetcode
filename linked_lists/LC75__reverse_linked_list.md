# Linked List Reversal Explanation

This document explains how the linked list reversal algorithm works in a simple, easy-to-understand way.

## The ListNode Class

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    # stores the value
        self.next = next  # points to the next node
```

Think of this like a train car:

- Each car (node) has a number (val)
- Each car is connected to the next car (next)

## The Reverse Function

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

This function takes the first car (head) of our train and returns a new train going in the opposite direction.

## The Reversal Process

```python
prev = None
curr = head
```

We start with:

- `prev`: points to nothing (None)
- `curr`: points to our first car (head)

## The Main Loop

```python
while curr:
    next_temp = curr.next  # remember where the next car is
    curr.next = prev       # point current car to previous car
    prev = curr            # move prev to current car
    curr = next_temp       # move current to next car
```

## Step-by-Step Example

Let's see this with a simple example of [1 → 2 → 3]:

### Step 1: [1 → 2 → 3]

- `prev` = None
- `curr` = 1
- `next_temp` = 2
- After: [1 ← 2 → 3]

### Step 2: [1 ← 2 → 3]

- `prev` = 1
- `curr` = 2
- `next_temp` = 3
- After: [1 ← 2 ← 3]

### Step 3: [1 ← 2 ← 3]

- `prev` = 2
- `curr` = 3
- `next_temp` = None
- After: [1 ← 2 ← 3]

### Final Step:

- `prev` = 3 (our new head)
- `curr` = None (we're done)
- Return: [3 → 2 → 1]

## Visual Representation

```
Original:    1 → 2 → 3 → None
Reversed:    None ← 1 ← 2 ← 3
```

## The Return

```python
return prev
```

We return the last car we processed, which is now the first car of our reversed train.

## Real-World Analogy

It's like turning a train around:

1. You start at the first car
2. For each car:
   - Remember where the next car is
   - Point the current car to the previous car
   - Move to the next car
3. When you're done, the last car becomes the first car

## Test Cases

The algorithm handles various cases:

- [1, 2, 3] becomes [3, 2, 1]
- [1, 2] becomes [2, 1]
- [1] stays [1]
- [] stays []

## Time and Space Complexity

- Time Complexity: O(n) - we visit each node exactly once
- Space Complexity: O(1) - we only use a constant amount of extra space

## Common Use Cases

1. Reversing a linked list is a fundamental operation used in many algorithms
2. It's often used in:
   - Palindrome checking
   - Reversing a portion of a linked list
   - Converting between different linked list representations
