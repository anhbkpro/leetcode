# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(mid):
    pass


def guessNumber(n: int) -> int:
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi)//2
        if not guess(mid):  # same as guess(mid) == 0
            return mid
        elif guess(mid) < 0:
            hi = mid-1
        else:
            lo = mid+1
    return -1


class Solution:
    pass
    