package twopointers

import "testing"

func TestMinCost(t *testing.T) {
	tests := []struct {
		name       string
		colors     string
		neededTime []int
		want       int
	}{
		{
			name:       "example 1 - multiple groups",
			colors:     "abaac",
			neededTime: []int{1, 2, 3, 4, 5},
			want:       3,
		},
		{
			name:       "example 2 - all same color",
			colors:     "abc",
			neededTime: []int{1, 2, 3},
			want:       0,
		},
		{
			name:       "example 3 - all consecutive same",
			colors:     "aabaa",
			neededTime: []int{1, 2, 3, 4, 1},
			want:       2,
		},
		{
			name:       "single balloon",
			colors:     "a",
			neededTime: []int{1},
			want:       0,
		},
		{
			name:       "two same color balloons",
			colors:     "aa",
			neededTime: []int{1, 2},
			want:       1,
		},
		{
			name:       "two different color balloons",
			colors:     "ab",
			neededTime: []int{1, 2},
			want:       0,
		},
		{
			name:       "all same color - keep max",
			colors:     "aaaa",
			neededTime: []int{3, 5, 1, 4},
			want:       8,
		},
		{
			name:       "alternating colors",
			colors:     "ababab",
			neededTime: []int{1, 2, 3, 4, 5, 6},
			want:       0,
		},
		{
			name:       "group at start",
			colors:     "aaabcd",
			neededTime: []int{1, 2, 3, 4, 5, 6},
			want:       3,
		},
		{
			name:       "group at end",
			colors:     "abcaaa",
			neededTime: []int{1, 2, 3, 4, 5, 6},
			want:       9,
		},
		{
			name:       "multiple groups of same color",
			colors:     "aabbaa",
			neededTime: []int{1, 2, 3, 4, 5, 6},
			want:       8,
		},
		{
			name:       "large consecutive group",
			colors:     "aaaaa",
			neededTime: []int{10, 1, 1, 1, 1},
			want:       4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := minCost(tt.colors, tt.neededTime)
			if got != tt.want {
				t.Errorf("minCost() = %v, want %v", got, tt.want)
			}
		})
	}
}
