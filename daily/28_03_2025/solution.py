# LeetCode Daily Challenge (2025-03-28)
# Title: Maximum Number of Points From Grid Queries
# Difficulty: Hard
# URL: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
#
# You are given an m x n integer matrix grid and an array queries of size k.
# 
# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
# 
# 
# 	If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# 	Otherwise, you do not get any points, and you end this process.
# 
# 
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
# 
# Return the resulting array answer.
# 
#  


# Your solution starts here
from typing import List
from collections import defaultdict, deque

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # process lower values queries first -> reuse the results? -> dp
        # for each queries, store the cells that are explored but not valid -> use those cells as starting points for subsequent queries

        m = len(grid)
        n = len(grid[0])
        k = len(queries)
        res = [0 for _ in range(k)]
        queries_with_index = [(query, i) for i, query in enumerate(queries)]
        queries_with_index.sort()
        sorted_queries_with_index = [(0, 0)]
        sorted_queries_with_index.extend(queries_with_index)
        cache_points = defaultdict(int) # caching the results for identical query values

        visited = [[False for _ in range(n)] for i in range(m)]
        dp = [0 for _ in range(k + 1)]
        starting_cells = deque([(0, 0)])

        def search(row, col, query, visited):
            if row < 0 or row >= m:
                return 0

            if col < 0 or col >= n:
                return 0

            if visited[row][col]:
                return 0

            visited[row][col] = True

            if grid[row][col] < query:
                return (
                    1
                    + search(row + 1, col, query, visited)
                    + search(row - 1, col, query, visited)
                    + search(row, col - 1, query, visited)
                    + search(row, col + 1, query, visited)
                )
            else:
                starting_cells.append((row, col))
                return 0

        for i in range(1, k + 1):
            val, index = sorted_queries_with_index[i]
            
            if cache_points[val] != 0:
                dp[i] = cache_points[val]
                res[index] = cache_points[val]
                continue

            acc_points = dp[i - 1]
            for _ in range(len(starting_cells)):
                row, col = starting_cells.popleft()
                visited[row][col] = False
                acc_points += search(row, col, val, visited)
            dp[i] = acc_points
            res[index] = acc_points
            cache_points[val] = acc_points

        # Time complexity: O(m*n*k)
        # Space complexity: O(max(m*n, k))
        return res