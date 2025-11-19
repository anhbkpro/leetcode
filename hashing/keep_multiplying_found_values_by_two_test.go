package hashing

import (
	"testing"
)

func TestFindFinalValue(t *testing.T) {
	t.Run("Test case 1", func(t *testing.T) {
		nums := []int{5, 3, 6, 1, 12}
		original := 3
		expected := 24
		result := FindFinalValue(nums, original)
		if result != expected {
			t.Errorf("Expected %d, but got %d", expected, result)
		}
	})

	t.Run("Test case 2", func(t *testing.T) {
		nums := []int{2, 7, 9}
		original := 4
		expected := 4
		result := FindFinalValue(nums, original)
		if result != expected {
			t.Errorf("Expected %d, but got %d", expected, result)
		}
	})

	t.Run("Test case 3", func(t *testing.T) {
		nums := []int{1, 2, 4, 8, 16, 32, 64, 128, 256, 512}
		original := 1
		expected := 1024
		result := FindFinalValue(nums, original)
		if result != expected {
			t.Errorf("Expected %d, but got %d", expected, result)
		}
	})

	t.Run("Test case 4", func(t *testing.T) {
		nums := []int{1024, 512, 256}
		original := 256
		expected := 2048
		result := FindFinalValue(nums, original)
		if result != expected {
			t.Errorf("Expected %d, but got %d", expected, result)
		}
	})

	t.Run("Test case 5", func(t *testing.T) {
		nums := []int{5, 10, 2}
		original := 5
		expected := 20
		result := FindFinalValue(nums, original)
		if result != expected {
			t.Errorf("Expected %d, but got %d", expected, result)
		}
	})

	t.Run("Test case 6: Empty list", func(t *testing.T) {
		nums := []int{}
		original := 1
		expected := 1
		result := FindFinalValue(nums, original)
		if result != expected {
			t.Errorf("Expected %d, but got %d", expected, result)
		}
	})
}
