from collections import deque


class Solution:
    def min_swaps_stack(self, s: str) -> int:
        stack = deque()
        unbalanced = 0
        for ch in s:
            # If an opening bracket is encountered, push it in the deque.
            if ch == "[":
                stack.append(ch)
            else:
                # If the deque is not empty, pop it.
                if stack:
                    stack.pop()
                # Otherwise increase the count of unbalanced brackets.
                else:
                    unbalanced += 1
        return (unbalanced + 1) // 2

    def min_swaps_space_optimized_stack(self, s: str) -> int:
        stack_size = 0
        for ch in s:
            # If character is opening bracket, increment the stack size.
            if ch == "[":
                stack_size += 1
            else:
                # If the character is closing bracket, and we have an opening bracket, decrease
                # the stack size.
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2
