package hashing

import (
	"reflect"
	"testing"
)

func TestTransfer(t *testing.T) {
	tests := []struct {
		name        string
		initial     []int64
		account1    int
		account2    int
		money       int64
		wantOK      bool
		wantBalance []int64
	}{
		{"success", []int64{10, 20, 30}, 1, 2, 5, true, []int64{5, 25, 30}},
		{"insufficient", []int64{10, 0}, 2, 1, 5, false, []int64{10, 0}},
		{"invalid_to_account", []int64{100}, 1, 2, 10, false, []int64{100}},
		{"edge_upper_bound", []int64{5, 5}, 2, 1, 5, true, []int64{10, 0}},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			b := Constructor(append([]int64(nil), tc.initial...))
			ok := b.Transfer(tc.account1, tc.account2, tc.money)
			if ok != tc.wantOK {
				t.Fatalf("Transfer returned ok=%v, want %v", ok, tc.wantOK)
			}
			if !reflect.DeepEqual([]int64(b), tc.wantBalance) {
				t.Fatalf("balances = %v, want %v", []int64(b), tc.wantBalance)
			}
		})
	}
}

func TestDeposit(t *testing.T) {
	tests := []struct {
		name        string
		initial     []int64
		account     int
		money       int64
		wantOK      bool
		wantBalance []int64
	}{
		{"success", []int64{1, 2}, 1, 3, true, []int64{4, 2}},
		{"invalid_account", []int64{10, 20}, 3, 5, false, []int64{10, 20}},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			b := Constructor(append([]int64(nil), tc.initial...))
			ok := b.Deposit(tc.account, tc.money)
			if ok != tc.wantOK {
				t.Fatalf("Deposit returned ok=%v, want %v", ok, tc.wantOK)
			}
			if !reflect.DeepEqual([]int64(b), tc.wantBalance) {
				t.Fatalf("balances = %v, want %v", []int64(b), tc.wantBalance)
			}
		})
	}
}

func TestWithdraw(t *testing.T) {
	tests := []struct {
		name        string
		initial     []int64
		account     int
		money       int64
		wantOK      bool
		wantBalance []int64
	}{
		{"exact_balance", []int64{10}, 1, 10, true, []int64{0}},
		{"insufficient", []int64{5}, 1, 6, false, []int64{5}},
		{"invalid_account", []int64{10, 20}, 3, 1, false, []int64{10, 20}},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			b := Constructor(append([]int64(nil), tc.initial...))
			ok := b.Withdraw(tc.account, tc.money)
			if ok != tc.wantOK {
				t.Fatalf("Withdraw returned ok=%v, want %v", ok, tc.wantOK)
			}
			if !reflect.DeepEqual([]int64(b), tc.wantBalance) {
				t.Fatalf("balances = %v, want %v", []int64(b), tc.wantBalance)
			}
		})
	}
}
