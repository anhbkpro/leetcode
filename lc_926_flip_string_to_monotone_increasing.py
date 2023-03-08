def minFlipsMonoIncr(s: str) -> int:
    dp = {(len(s), True): 0, (len(s), False): 0}

    def dfs(i, is_one):
        if (i, is_one) in dp:
            return dp[(i, is_one)]
        if i == len(s):  # base case
            return 0
        # if we are at a 1, we can either flip it to 0 or keep it as 1
        if is_one:
            # All zeros and s[i] == '1'
            if s[i] == '1':
                dp[(i, is_one)] = min(dfs(i + 1, is_one=False), 1 + dfs(i + 1, is_one))
            # All zeros and s[i] == '0'
            else:
                dp[(i, is_one)] = min(dfs(i + 1, is_one), 1 + dfs(i + 1, is_one=False))
        # if we are at a 0, we can either flip it to 1 or keep it as 0
        else:
            # Not all zeros and s[i] == '1'
            if s[i] == '1':
                dp[(i, is_one)] = dfs(i + 1, is_one)
            # Not all zeros and s[i] == '0'
            else:
                dp[(i, is_one)] = 1 + dfs(i + 1, is_one)
        return dp[(i, is_one)]

    return min(dfs(0, True), dfs(0, False))


class Solution:
    pass
