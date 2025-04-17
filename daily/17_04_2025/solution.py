# LeetCode Daily Challenge (2025-04-17)
# Title: Count Equal and Divisible Pairs in an Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
#
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 &lt;= i &lt; j &lt; n, such that nums[i] == nums[j] and (i * j) is divisible by k.
#  


# Your solution starts here
from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    total_pairs += 1
        
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        return total_pairs
