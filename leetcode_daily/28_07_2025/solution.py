# LeetCode Daily Challenge (2025-07-28)
# Title: Count Number of Maximum Bitwise-OR Subsets
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
#
# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
#
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
#
#


# Your solution starts here
from typing import List


class Solution:
	def countMaxOrSubsets(self, nums: List[int]) -> int:
		# maximum OR -> just OR every single elements then we would achieve the maximum

		# calc subsets, we either include a number or ignore it -> DFS

		n = len(nums)
		max_or = nums[0]
		for i in range(1, n):
			max_or = max_or | nums[i]

		def dfs(i, cur_or):
			if i == n:
				if cur_or == max_or:
					return 1
				else:
					return 0

			next_or = cur_or | nums[i]
			skip_count = dfs(i + 1, cur_or)
			incl_count = dfs(i + 1, next_or)

			return skip_count + incl_count

		res = dfs(0, 0)

		# Time Complexity: O(2^n) -> all subsets
		# Space Complexity: O(n) -> recursion stack
		return res
