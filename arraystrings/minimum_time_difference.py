from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minute(timePoint: str):
            hour, minute = timePoint.split(":")
            return int(hour) * 60 + int(minute)

        minutes = []
        for time in timePoints:
            minutes.append(convert_to_minute(time))
        minutes.sort()
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])
