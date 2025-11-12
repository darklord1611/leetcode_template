# LeetCode Daily Challenge (2025-11-12)\n# Title: Minimum Number of Operations to Make All Array Elements Equal to 1\n# Difficulty: Medium\n# Acceptance Rate: 44.31950315317164\n# Tags: Array, Math, Number Theory\n# URL: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/\n#\n# You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:
# 
# 
# 	Select an index i such that 0 &lt;= i &lt; n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
# 
# 
# Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.
# 
# The gcd of two integers is the greatest common divisor of the two integers.
# 
#  


# Your solution starts here
import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # if the overall gcd is > 1 -> invalid

        # if there exist 1 in the array -> then the min ops would be length - total count of 1s

        # else we need to find the minimum length of a subarray with gcd = 1 -> then we need to perform operations on that subarray -> then on the other remaining elements
        n = len(nums)
        cur_gcd = 0
        one_count = 0
        for i in range(n):
            if nums[i] == 1:
                one_count += 1
            
            cur_gcd = math.gcd(cur_gcd, nums[i])
        
        if one_count > 0:
            return n - one_count
        
        if cur_gcd > 1:
            return -1
        
        min_len = n

        for i in range(n):
            cur_gcd = 0
            for j in range(i, n):
                cur_gcd = math.gcd(cur_gcd, nums[j])
                if cur_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        # Time complexity: O(n^2 * logn)
        # Space complexity: O(1)
        return (min_len - 1) + (n - 1) # first part to obtain a 1 from the min length subarray with gcd == 1, then we transform the rest of the array to 1s
