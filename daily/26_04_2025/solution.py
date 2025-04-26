# LeetCode Daily Challenge (2025-04-26)
# Title: Count Subarrays With Fixed Bounds
# Difficulty: Hard
# URL: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
#
# You are given an integer array nums and two integers minK and maxK.
# 
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
# 
# 
# 	The minimum value in the subarray is equal to minK.
# 	The maximum value in the subarray is equal to maxK.
# 
# 
# Return the number of fixed-bound subarrays.
# 
# A subarray is a contiguous part of an array.
# 
#  


# Your solution starts here
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # sliding window for the best
        # the number of valid subarrays would be the sum of valid subarrays that end at every possible index i
        # keep track of the last maxK and minK and also last invalid index
        # Example: [1,3,5,2,7,5] -> min_index = 0, max_index = 5, invalid_index = 4
        # What are the possbilities at a single index i?
        # count the possible starting points for valid subarrays that end at current index -> valid choices would be from [last_invalid_index + 1, min(last_min_index, last_max_index)]

        n = len(nums)
        last_min_index = -1
        last_max_index = -1
        last_invalid_index = -1
        res = 0

        for i in range(n):
            if nums[i] == minK:
                last_min_index = i
            if nums[i] == maxK:
                last_max_index = i
            if nums[i] < minK or nums[i] > maxK:
                last_invalid_index = i

            if last_invalid_index > min(last_min_index, last_max_index): # why min? because we need both min and max values to be in the array to be valid
                continue
            res += min(last_min_index, last_max_index) - last_invalid_index

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        return res

