# LeetCode Daily Challenge (2025-03-26)
# Title: Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
#
# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
#
# A uni-value grid is a grid where all the elements of it are equal.
#
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
#
#


# Your solution starts here
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # what properties does these numbers have to have in order to be transformable? -> modulo, remainder?
        # what number should we transform into to minimize operations? -> should be a number that closer to all other numbers
        m = len(grid)
        n = len(grid[0])
        arr = []

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        arr.sort()

        cur_remainder = arr[0] % x
        ops_count = 0
        k = m * n

        for i in range(1, k):
            if arr[i] % x != cur_remainder:
                return -1

        pivot = arr[k // 2]

        for i in range(k):
            ops_count += abs(pivot - arr[i]) // x

        # Time complexity: O(m*n*log(m*n))
        # Space complexity: O(m*n)

        # why this still works with even-length arrays where there are two possible medians?

        return ops_count
