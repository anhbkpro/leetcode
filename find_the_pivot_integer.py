class Solution:
    def pivotInteger(self, n: int) -> int:
        total = sum(list(range(n + 1)))
        prefix_sum = [0] * (n + 1)
        prefix = 0
        for i in range(n + 1):
            prefix += i
            prefix_sum[i] = prefix

        begin, end = 0, n + 1
        while begin < end:
            mid = (begin + end) // 2
            if prefix_sum[mid] == total - prefix_sum[mid - 1]:
                return mid
            elif prefix_sum[mid] < total - prefix_sum[mid - 1]:
                begin = mid + 1
            else:
                end = mid

        return -1
