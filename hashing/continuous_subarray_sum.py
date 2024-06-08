class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            # sum = prefix[j] - prefix[i] = n*k
            # it means prefix[j] = Q1*k + R1, prefix[i] = Q2*k + R2 => prefix[j] - prefix[i] = (Q1 - Q2) * k + (R1 - R2)
            # to make sum a multiple of k, (R1 - R2) should be 0
            # so prefix[j] % k = prefix[i] % k
            # if we find same mod value, it means we found a subarray whose sum is multiple of k
            if prefix_mod in mod_seen:
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i

        return False
