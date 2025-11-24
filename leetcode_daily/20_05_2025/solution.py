# LeetCode Daily Challenge (2025-05-20)
# Title: Zero Array Transformation I
# Difficulty: Medium
# URL: https://leetcode.com/problems/zero-array-transformation-i/
#
# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].
#
# For each queries[i]:
#
#
# 	Select a subset of indices within the range [li, ri] in nums.
# 	Decrement the values at the selected indices by 1.
#
#
# A Zero Array is an array where all elements are equal to 0.
#
# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.
#
#


# Your solution starts here
from typing import List


class Solution:
	def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
		# how many transformations do we need?
		# subsets? we can omit some indices and not update
		# try brute force first, for each query decrease the value of the respective index range -> how to optimize?
		# process the queries, given an index, we could know how many transformations affect that index -> use difference arrays(DA)

		# DA -> efficient way of performing range update (l, r, x) aka add the value x to numbers in the range of (l, r)
		# HOW?
		# Example: [0, 0, 0, 0, 0, 0, 0], query = (3, 5, 4) -> updated array: [0, 0, 0, 4, 4, 4, 0] <- this is the prefix sum
		# breakdown the prefix sum: [0, 0, 0, 4, 0, 0, -4, 0] -> diff[l] += x, diff[r + 1] -= x
		n = len(nums)
		m = len(queries)
		diff = [0] * (n + 1)

		for i in range(m):
			left, right = queries[i]

			diff[left] += 1
			diff[right + 1] -= 1

		for i in range(1, n + 1):
			diff[i] = diff[i - 1] + diff[i]  # calculate the total updates for each index

		for i in range(n):
			if nums[i] - diff[i] > 0:
				return False

		# Time Complexity: O(max(n, m))
		# Space Complexity: O(n)
		return True
