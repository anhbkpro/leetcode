from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        total_cost = float("inf")
        current_total_quality = 0
        wage_to_quality_ratio = []

        # Calculate wage-to-quality ratio for each worker
        for i in range(n):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        # Sort workers based on their wage-to-quality ratio
        wage_to_quality_ratio.sort(key=lambda x: x[0])
        print(f"wage_to_quality_ratio = {wage_to_quality_ratio}")

        # Use a heap to keep track of the highest quality workers
        highest_quality_workers = []

        # Iterate through workers
        for i in range(n):
            heapq.heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            print(f"highest_quality_workers = {highest_quality_workers}")
            current_total_quality += wage_to_quality_ratio[i][1]

            # If we have more than k workers,
            # remove the one with the highest quality
            if len(highest_quality_workers) > k:
                top_quality = heapq.heappop(highest_quality_workers)
                print(f"[-] remove worker with quality = {top_quality}")
                current_total_quality += top_quality
                print(f"[total] current_total_quality = {current_total_quality}")

            # If we have exactly k workers,
            # calculate the total cost and update if it's the minimum
            if len(highest_quality_workers) == k:
                total_cost = min(
                    # calculate total_quality * curr_rate
                    total_cost, current_total_quality * wage_to_quality_ratio[i][0]
                )

        return total_cost
