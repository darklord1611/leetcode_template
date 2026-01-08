# LeetCode Daily Challenge (2026-01-08)\n# Title: Max Dot Product of Two Subsequences\n# Difficulty: Hard\n# Acceptance Rate: 63.30082510296569\n# Tags: Array, Dynamic Programming\n# URL: https://leetcode.com/problems/max-dot-product-of-two-subsequences/\n#\n# Given two arrays nums1 and nums2.
#
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
#
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
#
#


# Your solution starts here
from typing import List


class Solution:
	def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
		# solution depends on the prefix dot product sum we built -> DP
		# how are the subproblems relate to our problem?
		# max_sum would be the result when we already exhausted our options aka already traverse through m * n pairs
		# how many choices do we have for a pair (i, j)
		# we can just assign the current product, extends from the previous sequence, or skip either row or col

		n = len(nums1)
		m = len(nums2)

		dp = [[0] * m for _ in range(n)]  # dp[i][j] -> max dot product sum starting from 0 to i, 0 -> j

		for i in range(n):
			for j in range(m):
				cur_product = nums1[i] * nums2[j]

				# first choice, skip all previous sequences(since they could all be negative)
				dp[i][j] = cur_product

				# extend from previous sequence
				if i > 0 and j > 0:
					dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + cur_product)

				# skip the current element of the first array
				if i > 0:
					dp[i][j] = max(dp[i][j], dp[i - 1][j])

				# skip the current element of the second array
				if j > 0:
					dp[i][j] = max(dp[i][j], dp[i][j - 1])

		# Time Complexity: O(n * m)
		# Space Complexity: O(n * m)
		return dp[n - 1][m - 1]
