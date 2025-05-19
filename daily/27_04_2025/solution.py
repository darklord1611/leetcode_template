# LeetCode Daily Challenge (2025-04-27)
# Title: Count Subarrays of Length Three With a Condition
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
#
# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # sliding window

        n = len(nums)
        left = 0
        count = 0
        for right in range(n):
            if right - left + 1 == 3:
                if nums[right] + nums[left] == nums[left + 1] / 2:
                    count += 1
                left += 1
            
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        return count
