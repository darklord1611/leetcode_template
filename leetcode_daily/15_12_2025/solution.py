# LeetCode Daily Challenge (2025-12-15)\n# Title: Number of Smooth Descent Periods of a Stock\n# Difficulty: Medium\n# Acceptance Rate: 65.30156580861699\n# Tags: Array, Math, Dynamic Programming\n# URL: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/\n#\n# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.
#
# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.
#
# Return the number of smooth descent periods.
#
#


# Your solution starts here
from typing import List


class Solution:
	def getDescentPeriods(self, prices: List[int]) -> int:
		# ok so every single day is considered a smooth descent

		# we simply keep track of the length of current smooth descent period

		# given a period like 10 ..... 5 -> how many smooth descent periods do we have? think of descent period of size 1, 2, 3 ....

		cur_des_len = 1
		ans = 0
		n = len(prices)

		for i in range(1, n):
			if prices[i] == prices[i - 1] - 1:
				cur_des_len += 1
			else:
				ans += cur_des_len * (cur_des_len + 1) // 2
				cur_des_len = 1

		# account for the final period
		ans += cur_des_len * (cur_des_len + 1) // 2

		# Time Complexity: O(n)
		# Space Complexity: O(1)
		return ans
