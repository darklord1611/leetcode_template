# LeetCode Daily Challenge (2025-06-16)
# Title: Maximum Difference Between Increasing Elements
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
#
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 &lt;= i &lt; j &lt; n and nums[i] &lt; nums[j].
# 
# Return the maximum difference. If no such i and j exists, return -1.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # keep track of the minimum number when we traverse through the array

        max_diff = -1
        min_num = nums[0]
        n = len(nums)
        for i in range(1, n):
            if min_num < nums[i]:
                max_diff = max(max_diff, nums[i] - min_num)
            min_num = min(min_num, nums[i])

        return max_diff
