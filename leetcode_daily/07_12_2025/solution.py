# LeetCode Daily Challenge (2025-12-07)\n# Title: Count Odd Numbers in an Interval Range\n# Difficulty: Easy\n# Acceptance Rate: 51.180980213577264\n# Tags: Math\n# URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/\n#\n# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
#
#


# Your solution starts here


class Solution:
	def countOdds(self, low: int, high: int) -> int:
		# check for cases, low -> odd, high -> even, etc

		res = (high - low) // 2

		if low % 2 != 0 or high % 2 != 0:
			res += 1

		return res
