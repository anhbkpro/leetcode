import collections


def maxConsecutiveAnswersSlidingWindow(answerKey: str, k: int) -> int:
    max_size = k
    count = collections.Counter(answerKey[:k])

    left = 0
    for right in range(k, len(answerKey)):
        count[answerKey[right]] += 1

        while min(count['T'], count['F']) > k:
            count[answerKey[left]] -= 1
            left += 1

        max_size = max(max_size, right - left + 1)

    return max_size


class Solution:
    pass
