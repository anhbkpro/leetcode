class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_stack = []

        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and num_stack and num_stack[-1] > digit:
                num_stack.pop()
                k -= 1

            num_stack.append(digit)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        final_stack = num_stack[:-k] if k else num_stack

        # trip the leading zeros
        return "".join(final_stack).lstrip('0') or "0"
