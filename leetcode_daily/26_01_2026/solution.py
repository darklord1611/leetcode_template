# LeetCode Daily Challenge (2026-01-26)\n# Title: Minimum Absolute Difference\n# Difficulty: Easy\n# Acceptance Rate: 73.92022676988871\n# Tags: Array, Sorting\n# URL: https://leetcode.com/problems/minimum-absolute-difference/\n#\n# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# 
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# 
# 
# 	a, b are from arr
# 	a &lt; b
# 	b - a equals to the minimum absolute difference of any two elements in arr
# 
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        n = len(arr)

        arr.sort()
        ans = []

        min_diff = 2 * (10 ** 6) + 1

        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                ans.append([arr[i - 1], arr[i]])
        
        # Time Complexity: O(n log n)
        # Space Complexity: O(logn)
        return ans
