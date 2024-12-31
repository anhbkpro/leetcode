from typing import List


class SolutionTopDownDP:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # The last day on which we need to travel
        last_day = days[-1]

        # Initialize dp array with zeros
        dp = [0] * (last_day + 1)

        # Index to track current position in days array
        i = 0

        # Iterate through all days up to the last travel day
        for day in range(1, last_day + 1):
            # If we don't need to travel on this day, cost remains same as previous day
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                # Buy a pass on this day and move to next travel day
                i += 1

                # Calculate cost with 1-day pass
                one_day = dp[day - 1] + costs[0]

                # Calculate cost with 7-day pass
                seven_day = dp[max(0, day - 7)] + costs[1]

                # Calculate cost with 30-day pass
                thirty_day = dp[max(0, day - 30)] + costs[2]

                # Store the minimum of all three options
                dp[day] = min(one_day, seven_day, thirty_day)

        return dp[last_day]


class SolutionBottomUpDP:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # The last day on which we need to travel
        last_day = days[-1]

        # Initialize dp array with zeros
        dp = [0] * (last_day + 1)

        # Set of travel days
        travel_days = set(days)

        # Iterate through all days up to the last travel day
        for day in range(1, last_day + 1):
            # If we don't need to travel on this day, cost remains same as previous day
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                # Calculate cost with 1-day pass
                one_day = dp[day - 1] + costs[0]

                # Calculate cost with 7-day pass
                seven_day = dp[max(0, day - 7)] + costs[1]

                # Calculate cost with 30-day pass
                thirty_day = dp[max(0, day - 30)] + costs[2]

                # Store the minimum of all three options
                dp[day] = min(one_day, seven_day, thirty_day)

        return dp[last_day]
