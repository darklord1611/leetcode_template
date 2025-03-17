# LeetCode Daily Challenge (2025-03-17)
# Title: Divide Array Into Equal Pairs
# Difficulty: Easy
# URL: https://leetcode.com/problems/divide-array-into-equal-pairs/
#
# You are given an integer array nums consisting of 2 * n integers.
# 
# You need to divide nums into n pairs such that:
# 
# 
# 	Each element belongs to exactly one pair.
# 	The elements present in a pair are equal.
# 
# 
# Return true if nums can be divided into n pairs, otherwise return false.
# 
#  


# Your solution starts here

from typing import List
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        n = len(nums)
        freq = defaultdict(int)

        for i in range(n):
            freq[nums[i]] += 1
        
        for key in freq:
            if freq[key] % 2 != 0:
                return False

        # Time complexity: O(n)
        # Space complexity: O(n)
        return True
