from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last_serve_time = 0
        total_wait_time = 0
        for arrival, time in customers:
            start_serve = max(arrival, last_serve_time)
            last_serve_time = start_serve + time
            wait_time = last_serve_time - arrival
            total_wait_time += wait_time
        return total_wait_time/len(customers)
