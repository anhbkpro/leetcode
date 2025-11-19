package main

import (
	"strings"
)

func numberOfBeams(bank []string) int {
	ans := 0
	prevDevices := strings.Count(bank[0], "1")

	for i := 1; i < len(bank); i++ {
		curDevices := strings.Count(bank[i], "1")
		if curDevices == 0 {
			continue
		}
		ans += prevDevices * curDevices
		prevDevices = curDevices
	}

	return ans
}
