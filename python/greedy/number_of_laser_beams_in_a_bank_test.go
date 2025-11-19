package main

import "testing"

func TestNumberOfBeams(t *testing.T) {
	tests := []struct {
		name     string
		bank     []string
		expected int
	}{
		{
			name:     "example 1",
			bank:     []string{"011001", "000000", "010100", "001000"},
			expected: 8,
		},
		{
			name:     "example 2",
			bank:     []string{"000", "111", "000"},
			expected: 0,
		},
		{
			name:     "single row",
			bank:     []string{"111"},
			expected: 0,
		},
		{
			name:     "two rows with devices",
			bank:     []string{"11", "11"},
			expected: 4,
		},
		{
			name:     "multiple rows with zeros in between",
			bank:     []string{"101", "000", "000", "111"},
			expected: 6,
		},
		{
			name:     "all zeros except first",
			bank:     []string{"111", "000", "000"},
			expected: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numberOfBeams(tt.bank)
			if result != tt.expected {
				t.Errorf("numberOfBeams(%v) = %d; expected %d", tt.bank, result, tt.expected)
			}
		})
	}
}
