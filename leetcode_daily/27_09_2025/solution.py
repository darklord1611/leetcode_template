# LeetCode Daily Challenge (2025-09-27)
# Title: Largest Triangle Area
# Difficulty: Easy
# URL: https://leetcode.com/problems/largest-triangle-area/
#
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
#
#


# Your solution starts here

from itertools import combinations
from typing import List


class Solution:
	def largestTriangleArea(self, points: List[List[int]]) -> float:
		# Shoelace's formula

		def calc_triangle_area(a, b, c):
			return 0.5 * abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))

		max_area = 0
		for a, b, c in combinations(points, 3):
			cur_area = calc_triangle_area(a, b, c)
			max_area = max(max_area, cur_area)

		# Time complexity: O(n^3)
		# Space complexity: O(1)
		return max_area
