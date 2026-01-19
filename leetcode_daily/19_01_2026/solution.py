# LeetCode Daily Challenge (2026-01-19)\n# Title: Maximum Side Length of a Square with Sum Less than or Equal to Threshold\n# Difficulty: Medium\n# Acceptance Rate: 60.0552679386253\n# Tags: Array, Binary Search, Matrix, Prefix Sum\n# URL: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/\n#\n# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # monotonic nature, suppose we are given a solution which has side length of x -> what do we know about x - 1? x + 1?

        # binary search? 2D prefix sum?

        m = len(mat)
        n = len(mat[0])
        prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]

        # 1 2
        # 3 4

        # prefix sums would be
        # 1 3
        # 4 10

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sums[i][j] = prefix_sums[i - 1][j] + prefix_sums[i][j - 1] - prefix_sums[i - 1][j - 1] + mat[i - 1][j - 1]
        
        def check(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    r2, c2 = i + k, j + k
                    area = (
                        prefix_sums[r2][c2]
                        - prefix_sums[i][c2]
                        - prefix_sums[r2][j]
                        + prefix_sums[i][j]
                    )
                    if area <= threshold:
                        return True
            return False

        low, high = 1, min(m, n)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans