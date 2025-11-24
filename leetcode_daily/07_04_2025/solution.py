# LeetCode Daily Challenge (2025-04-07)
# Title: Partition Equal Subset Sum
# Difficulty: Medium
# URL: https://leetcode.com/problems/partition-equal-subset-sum/
#
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
#
#


# Your solution starts here
from typing import List


class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		# two subsets MUST use all elements and have equal sums
		# two subsets with equal sums? -> the total sum must be divisible by 2
		# problem can be formulated as finding one subset which have sum = total sum / 2

		# subsets -> take it or leave it kind of problem -> 0-1 knapsack? -> DP
		# recursive + memoization

		n = len(nums)
		total_sum = sum(nums)
		if total_sum % 2 != 0:
			return False

		memo = {}

		def dfs(index, target):
			if index >= n:
				return target == 0

			if (index, target) in memo:
				return memo[(index, target)]

			if target < 0:
				return False

			take_cur_element = dfs(index + 1, target - nums[index])

			memo[(index + 1, target - nums[index])] = take_cur_element

			if take_cur_element:
				return True

			skip_cur_element = dfs(index + 1, target)

			memo[(index + 1, target)] = take_cur_element

			return skip_cur_element

		res = dfs(0, total_sum // 2)

		# Time
		return res
