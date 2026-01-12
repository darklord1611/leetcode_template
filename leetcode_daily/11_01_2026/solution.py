# LeetCode Daily Challenge (2026-01-11)\n# Title: Maximal Rectangle\n# Difficulty: Hard\n# Acceptance Rate: 55.79469402296957\n# Tags: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack\n# URL: https://leetcode.com/problems/maximal-rectangle/\n#\n# Given a rows x cols binary matrix filled with 0&#39;s and 1&#39;s, find the largest rectangle containing only 1&#39;s and return its area.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
		# so we need to pass them according to the orders in the array
		# effectively we can find a greedy way of traversing between two arbitrary points -> then done

		# two points -> A(x1, y1), B(x2, y2) -> how can we travel from A to B with min ops? utilize diagonal moves if possible?

		total_time = 0
		n = len(points)

		for i in range(1, n):
			total_time += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))

		return total_time
