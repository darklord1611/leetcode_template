from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # subarray -> sliding window? naturally
        # think about the brute force approach, we just count how many odd subarrays that start at an index
        # inverted -> how many odd subarrays that ends at a particular index?
        # prefix sum?
        mod = 10 ** 9 + 7
        even_prefix_sum_count = 0
        odd_prefix_sum_count = 0
        res = 0
        prefix_sum = 0
        n = len(arr)

        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum % 2 == 0:
                # current sum is even, we can substract the earlier odd prefix sums to achieve a valid subarray -> even - odd == odd
                res = (res + odd_prefix_sum_count) % mod
                even_prefix_sum_count += 1
            else:
                res = (res + even_prefix_sum_count + 1) % mod
                odd_prefix_sum_count += 1
        
        # time complexity: O(n)
        # space complexity: O(1)


        # DP solution not implemented yet

        return res
