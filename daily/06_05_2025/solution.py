# LeetCode Daily Challenge (2025-05-06)
# Title: Build Array from Permutation
# Difficulty: Easy
# URL: https://leetcode.com/problems/build-array-from-permutation/
#
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 &lt;= i &lt; nums.length and return it.
# 
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
