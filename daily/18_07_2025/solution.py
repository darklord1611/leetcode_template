# LeetCode Daily Challenge (2025-07-18)
# Title: Minimum Difference in Sums After Removal of Elements
# Difficulty: Hard
# URL: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
#
# You are given a 0-indexed integer array nums consisting of 3 * n elements.
# 
# You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
# 
# 
# 	The first n elements belonging to the first part and their sum is sumfirst.
# 	The next n elements belonging to the second part and their sum is sumsecond.
# 
# 
# The difference in sums of the two parts is denoted as sumfirst - sumsecond.
# 
# 
# 	For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
# 	Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
# 
# 
# Return the minimum difference possible between the sums of the two parts after the removal of n elements.
# 
#  


# Your solution starts here
from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # 3n elements
        # remove a subsequence of n elements, then calculate sum of first n elements and the last n elements -> res = sum1 - sum2
        # we want minimum difference aka min(sum1 - sum2) -> equivalent of minimize sum1 and maximize sum2
        # instead of thinking about what elements to remove, think about what elements should we keep?
        # suppose we have a partition index k that would divide the array into two subarrays

        # suppose len(sub1) = k, len(sub2) = 3n - k -> k belongs to [n, 2n] (to ensure that each subarray have at least n elements)

        # so the problem boils down to which elements of the subarray should we keep?
        # we need to minimize first subarray -> choose n smallest elements
        # we need to maximize second subarray -> choose n largest elements
        
        # how to keep track of n min/max elements out of k -> heap

        # for each choice of partition index k, we need to calculate first sum - second sum -> prefix + suffix sums

        m = len(nums)
        n = m // 3

        max_sums = [0] * (m + 1)
        min_sums = [0] * (m + 1)

        # build first left max heap
        min_left_heap = []
        cur_sum = 0

        for i in range(m):
            heapq.heappush(min_left_heap, -nums[i])
            cur_sum += nums[i]

            if len(min_left_heap) > n:
                min_element = -heapq.heappop(min_left_heap)
                cur_sum -= min_element
            
            if len(min_left_heap) == n:
                min_sums[i] = cur_sum
        
        max_right_heap = []
        cur_sum = 0

        for i in range(m - 1, -1, -1):
            heapq.heappush(max_right_heap, nums[i])
            cur_sum += nums[i]

            if len(max_right_heap) > n:
                max_element = heapq.heappop(max_right_heap)
                cur_sum -= max_element
            
            if len(max_right_heap) == n:
                max_sums[i] = cur_sum
        
        # now consider all possible choices for k
        res = float("inf")
        for k in range(n - 1, 2*n):
            res = min(res, min_sums[k] - max_sums[k + 1]) # min_sums[k] is the sum of n smallest elements, max_sums[k] is the sum of n largest elements
        

        # Time Complexity: O(n log n) due to heap operations
        # Space Complexity: O(n) for storing the prefix and suffix sums
        return res
