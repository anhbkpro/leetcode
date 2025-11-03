package twopointers

func minCost(colors string, neededTime []int) int {
	// Initialize two pointers i, j.
	totalTime := 0
	i, j := 0, 0

	for i < len(neededTime) && j < len(neededTime) {
		currTotal := 0
		currMax := 0

		// Find all the balloons having the same color as the
		// balloon indexed at i, record the total removal time
		// and the maximum removal time.
		for j < len(neededTime) && colors[i] == colors[j] {
			currTotal += neededTime[j]
			if neededTime[j] > currMax {
				currMax = neededTime[j]
			}
			j++
		}

		// Once we reach the end of the current group, add the cost of
		// this group to totalTime, and reset two pointers.
		totalTime += currTotal - currMax
		i = j
	}

	return totalTime
}
