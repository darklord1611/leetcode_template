# LeetCode Daily Challenge (2025-11-03)\n# Title: Minimum Time to Make Rope Colorful\n# Difficulty: Medium\n# Acceptance Rate: 64.04530366264362\n# Tags: Array, String, Dynamic Programming, Greedy\n# URL: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/\n#\n# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
#
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
#
# Return the minimum time Bob needs to make the rope colorful.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minCost(self, colors: str, neededTime: List[int]) -> int:
		# so we need to keep track of consecutive same color balloons if there are any
		# for each consecutive same color segment of size k for example -> we calculate the min amount of time to delete (k - 1) elements

		# or, we could simply keep track of the time of selected indices -> take sum of needed time - total selected -> needed time to remove consecutive balloons
		# follow the above logic, for each segment, we would retain the balloon with the largest needed time -> why? because we want min delete time -> therefore, be greedy and delete the balloon with min and retain the max

		n = len(colors)
		total_time = sum(neededTime)
		max_time = 0  # total time of selected indices
		cur_max_time = neededTime[0]

		for i in range(1, n):
			# check if cur_index is the same color as before
			if colors[i] == colors[i - 1]:
				cur_max_time = max(cur_max_time, neededTime[i])
			else:  # we encounter new color
				max_time += cur_max_time
				cur_max_time = neededTime[i]  # reset to be the current color's time

		max_time += cur_max_time  # account for the last segment

		# Time complexity: O(n)
		# Space complexity: O(1)
		return total_time - max_time
