# LeetCode Daily Challenge (2025-12-28)\n# Title: Count Negative Numbers in a Sorted Matrix\n# Difficulty: Easy\n# Acceptance Rate: 77.95914543825856\n# Tags: Array, Binary Search, Matrix\n# URL: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/\n#\n# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
#
#


# Your solution starts here
from typing import List


class Solution:
	def countNegatives(self, grid: List[List[int]]) -> int:
		# 4 3 2 -1
		# 3 2 1 -1
		# 1 1 -1 -2
		# -1 -1 -2 -3

		# both rows and cols are sorted in decreasing order, visualize the grids, what should we look for for each row
		# where should we start, think about the sorted nature

		m = len(grid)
		n = len(grid[0])

		cur_row, cur_col = m - 1, 0
		ans = 0

		while cur_row >= 0 and cur_col < n:
			if grid[cur_row][cur_col] >= 0:
				cur_col += 1
			else:
				ans += n - cur_col
				cur_row -= 1

		return ans
