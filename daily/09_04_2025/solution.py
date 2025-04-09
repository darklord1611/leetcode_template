# LeetCode Daily Challenge (2025-04-09)
# Title: Minimum Operations to Make Array Values Equal to K
# Difficulty: Easy
# URL: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
#
# You are given an integer array nums and an integer k.
# 
# An integer h is called valid if all values in the array that are strictly greater than h are identical.
# 
# For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] &gt; 9 are equal to 10, but 5 is not a valid integer.
# 
# You are allowed to perform the following operation on nums:
# 
# 
# 	Select an integer h that is valid for the current values in nums.
# 	For each index i where nums[i] &gt; h, set nums[i] to h.
# 
# 
# Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # if there is any number in the array less than k -> impossible
        # keep the count of each elements
        # problem can also be interpreted as returning number of DISTINCT integers GREATER than k 

        unique_nums = set(nums)
        n = len(unique_nums)
        max_ops = 0
        for num in unique_nums:
            if num < k:
                return -1
            elif num > k:
                max_ops += 1

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        return max_ops
