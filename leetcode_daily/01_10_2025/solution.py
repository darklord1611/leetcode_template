# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
class Solution:
	def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
		max_bottle = numBottles

		empty = numBottles

		while empty >= numExchange:
			max_bottle += empty // numExchange

			empty = empty // numExchange + empty % numExchange

		return max_bottle
