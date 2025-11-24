# LeetCode Daily Challenge (2025-08-30)
# Title: Valid Sudoku
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#
# 	Each row must contain the digits 1-9 without repetition.
# 	Each column must contain the digits 1-9 without repetition.
# 	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#
# Note:
#
#
# 	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# 	Only the filled cells need to be validated according to the mentioned rules.
#
#
#


# Your solution starts here
from typing import List


class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		# check the rows first then column
		rows = len(board)
		cols = len(board[0])

		# check the rows
		for i in range(rows):
			checks = [0 for _ in range(rows + 1)]
			for j in range(cols):
				if board[i][j] == ".":
					continue
				if checks[int(board[i][j])] == 1:
					return False
				else:
					checks[int(board[i][j])] = 1

		# check the columns
		for i in range(cols):
			checks = [0 for _ in range(cols + 1)]
			for j in range(rows):
				if board[j][i] == ".":
					continue
				if checks[int(board[j][i])] == 1:
					return False
				else:
					checks[int(board[j][i])] = 1

		# check the sub-boxes, remember we only need the coordinates of the top-left to figure the rest of the box

		for i in range(0, rows, 3):
			for j in range(0, cols, 3):
				checks = [0 for _ in range(cols + 1)]
				for k in range(i, i + 3):
					for l in range(j, j + 3):
						if board[k][l] == ".":
							continue
						if checks[int(board[k][l])] == 1:
							return False
						else:
							checks[int(board[k][l])] = 1

		# Time complexity is O(n^2)
		# Space complexity is O(n)

		return True
