# LeetCode Daily Challenge (2025-05-17)
# Title: Sort Colors
# Difficulty: Medium
# URL: https://leetcode.com/problems/sort-colors/
#
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# 
# You must solve this problem without using the library&#39;s sort function.
# 
#  


# Your solution starts here]
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count sort?

        freqs = [0, 0, 0]
        
        for num in nums:
            freqs[num] += 1

        # calculate the indices where we would change color
        freqs[1] = freqs[0] + freqs[1]
        freqs[2] = freqs[1] + freqs[2]

        for i in range(len(nums)):
            if i < freqs[0]:
                nums[i] = 0
            elif i < freqs[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        
        return