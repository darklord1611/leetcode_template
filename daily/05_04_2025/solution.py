# LeetCode Daily Challenge (2025-04-05)
# Title: Sum of All Subset XOR Totals
# Difficulty: Easy
# URL: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
#
# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
# 
# 
# 	For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# 
# 
# Given an array nums, return the sum of all XOR totals for every subset of nums. 
# 
# Note: Subsets with the same elements should be counted multiple times.
# 
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
# 
#  


# Your solution starts here

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets_xor_sums = []
        n = len(nums)
        cur_subsets = []    

        def dfs(cur_index):
            if cur_index >= n:
                cur_xor = cur_subsets[0] if len(cur_subsets) > 0 else 0
                for i in range(1, len(cur_subsets)):
                    cur_xor = cur_xor ^ cur_subsets[i]
                subsets_xor_sums.append(cur_xor)
                return
            
            # include the current element
            cur_subsets.append(nums[cur_index])
            dfs(cur_index + 1)

            # exclude the current element
            cur_subsets.pop()
            dfs(cur_index + 1)
        
        dfs(0)
        return sum(subsets_xor_sums)
