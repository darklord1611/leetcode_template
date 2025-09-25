# LeetCode Daily Challenge (2025-09-25)
# Title: Triangle
# Difficulty: Medium
# URL: https://leetcode.com/problems/triangle/
#
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
#
#


# Your solution starts here
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # loop from the top to the bottom, we keep track of the running sum

        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        previous_path_sums = [float("inf") for _ in range(n)]

        previous_path_sums[0] = triangle[0][0]
        # k-th layer -> k + 1 elements

        for i in range(1, n):
            cur_path_sums = [float("inf") for _ in range(n)]
            for j in range(i + 1):
                # compare two elements of the previous layer
                if j - 1 >= 0:
                    cur_path_sums[j] = min(
                        cur_path_sums[j], triangle[i][j] + previous_path_sums[j - 1]
                    )

                cur_path_sums[j] = min(
                    cur_path_sums[j], triangle[i][j] + previous_path_sums[j]
                )

            # now reassign the sums to previous

            previous_path_sums = cur_path_sums

        min_path_sum = float("inf")
        for i in range(n):
            min_path_sum = min(min_path_sum, previous_path_sums[i])

        # Time complexity: O(n^2), n -> number of rows
        # Space complexity: O(n) +
        return min_path_sum
        # [5, 6]
