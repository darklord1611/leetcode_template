# LeetCode Daily Challenge (2025-03-12)
# Title: Maximum Count of Positive Integer and Negative Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
#
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
# 
# 
# 	In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# 
# 
# Note that 0 is neither positive nor negative.
# 
#  


# Your solution starts here

from typing import List

# Brute force solution

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count = 0
        neg_count = 0

        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                pos_count += 1
            elif nums[i] < 0:
                neg_count += 1
        
        return max(pos_count, neg_count)


# Optimized solution using binary search -> find the first and last zero index
