# LeetCode Daily Challenge (2025-05-21)
# Title: Set Matrix Zeroes
# Difficulty: Medium
# URL: https://leetcode.com/problems/set-matrix-zeroes/
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0&#39;s.
#
# You must do it in place.
#
#


# Your solution starts here
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # store the indices of zero values
        # want to optimize space? think about how we can use the matrix itself to store the indices
        rows_set = set()
        cols_set = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_set.add(i)
                    cols_set.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows_set or j in cols_set:
                    matrix[i][j] = 0

        # Time Complexity: O(m * n)
        # Space Complexity: O(m + n)

        return
