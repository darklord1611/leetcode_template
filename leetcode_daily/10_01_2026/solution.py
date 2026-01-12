# LeetCode Daily Challenge (2026-01-10)\n# Title: Minimum ASCII Delete Sum for Two Strings\n# Difficulty: Medium\n# Acceptance Rate: 68.9272332812687\n# Tags: String, Dynamic Programming\n# URL: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/\n#\n# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
#
#


# Your solution starts here


class Solution:
	def minimumDeleteSum(self, s1: str, s2: str) -> int:
		# think in reverse, which character to keep?

		# in 2nd example, suppose we keep the subsequence "lee" -> then everything else must be deleted

		# this boils down to which subsequence we gonna keep to get the maximum ASCII values -> then we would have lowest ASCII values of deleted characters

		# think of a simpler problem, suppose every character has a value of 1 -> LCS problem -> DP

		# dp[i][j] -> maximum ASCII values of common subsequence that use up to ith index in first string and jth index in second string

		# res = total_s1 + total_s2 - 2 * common

		total_s1 = sum([ord(char) for char in s1])
		total_s2 = sum([ord(char) for char in s2])

		n = len(s1)
		m = len(s2)
		dp = [[0] * (m + 1) for _ in range(n + 1)]

		for i in range(n):
			for j in range(m):
				if s1[i] == s2[j]:
					dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
				else:
					dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

		return total_s1 + total_s2 - 2 * dp[n][m]
