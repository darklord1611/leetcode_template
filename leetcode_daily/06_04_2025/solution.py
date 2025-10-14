# LeetCode Daily Challenge (2025-04-06)
# Title: Largest Divisible Subset
# Difficulty: Medium
# URL: https://leetcode.com/problems/largest-divisible-subset/
#
# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
#
#
# 	answer[i] % answer[j] == 0, or
# 	answer[j] % answer[i] == 0
#
#
# If there are multiple solutions, return any of them.
#
#


# Your solution starts here
from typing import List


# TOP DOWN DP


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # given 4 numbers: a b c d -> how to check if valid?
        # check if a % b == 0 or b % a == 0 -> simplify: max(a, b) % min(a, b) == 0 -> sort first
        # what happen when we add another sorted number to the result? check with all numbers? -> only check with the largest number
        # we can either include the number if satisfied or skip -> overlapped problems -> DP
        nums.sort()
        n = len(nums)
        cache = {}

        def dfs(index) -> List[int]:
            if index >= n:
                return []

            if index in cache:
                return cache[index]

            cur_subset = [nums[index]]

            tmp_subset = []

            for i in range(index + 1, n):
                if nums[i] % nums[index] == 0:
                    tmp_subset = [nums[index]] + dfs(
                        i
                    )  # continue exploring the ith index
                    if len(tmp_subset) > len(cur_subset):
                        cur_subset = tmp_subset

            cache[index] = cur_subset
            return cur_subset

        res = []
        for i in range(n):  # check all subsets starting at any possible indexes
            tmp_subset = dfs(i)
            if len(tmp_subset) > len(res):
                res = tmp_subset

        # Time Complexity: O(n^2)
        # Space Complexity: O(n)

        return res


# BOTTOM UP DP

# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         n = len(nums)
#         res = []
#         cache = [[] for _ in range(n)]
#         for i in range(n - 1, -1, -1):
#             cur = []
#             for j in range(i + 1, n):
#                 if nums[j] % nums[i] == 0:
#                     if len(cache[j]) > len(cur):
#                         cur = cache[j]
#             cur = [nums[i]] + cur
#             cache[i] = cur
#             if len(cache[i]) > len(res):
#                 res = cache[i]
#         return res
