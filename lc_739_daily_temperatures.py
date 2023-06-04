from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    stack = []
    result = [0] * n

    for curr_day, curr_temp in enumerate(temperatures):
        # Pop until the current day's temperature is not
        # warmer than the temperature at the top of the stack
        while stack and temperatures[stack[-1]] < curr_temp:
            prev_day = stack.pop()
            result[prev_day] = curr_day - prev_day
        stack.append(curr_day)

    return result


class Solution:
    pass
