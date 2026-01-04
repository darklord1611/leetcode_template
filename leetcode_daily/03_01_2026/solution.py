# LeetCode Daily Challenge (2026-01-03)\n# Title: Number of Ways to Paint N × 3 Grid\n# Difficulty: Hard\n# Acceptance Rate: 67.16102614558767\n# Tags: Dynamic Programming\n# URL: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/\n#\n# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
#
# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
#
#


# Your solution starts here


class Solution:
	def numOfWays(self, n: int) -> int:
		# n x 3 -> n rows, 3 cols
		# at a single row, we must use at least 2 colors, ie RGR or RGY and other orderings
		# think about subproblem, number of ways to paint using 3 colors per row/using only 2 colors per row? is this complementing?

		# how many rows are painted with 2 colors? how many rows are painted with 3 colors?

		MOD = 10**9 + 7
		pattern_ABA = 6  # initial number of choices for coloring a single row using 2 colors
		pattern_ABC = 6  # initial number of choices for coloring a single row using 3 colors

		for _ in range(1, n):  # start color from second row
			new_pattern_ABA = (pattern_ABA * 3 + pattern_ABC * 2) % MOD
			new_pattern_ABC = (pattern_ABA * 2 + pattern_ABC * 2) % MOD

			pattern_ABA = new_pattern_ABA
			pattern_ABC = new_pattern_ABC

		# Time complexity: O(n)
		# Space complexity: O(1)
		return (pattern_ABA + pattern_ABC) % MOD
