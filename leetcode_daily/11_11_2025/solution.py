# LeetCode Daily Challenge (2025-11-11)\n# Title: Ones and Zeroes\n# Difficulty: Medium\n# Acceptance Rate: 49.58353663122694\n# Tags: Array, String, Dynamic Programming\n# URL: https://leetcode.com/problems/ones-and-zeroes/\n#\n# You are given an array of binary strings strs and two integers m and n.
#
# Return the size of the largest subset of strs such that there are at most m 0&#39;s and n 1&#39;s in the subset.
#
# A set x is a subset of a set y if all elements of x are also elements of y.
#
#


# Your solution starts here

from typing import List
from collections import defaultdict


class TOP_DOWN_SOLUTION:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # think of strings as items, number of 0s and 1s as values

        # DP with memoization

        freq = []
        str_len = len(strs)
        dp = {}
        for i in range(str_len):
            zero_count = 0
            for char in strs[i]:
                if char == "0":
                    zero_count += 1

            freq.append((zero_count, len(strs[i]) - zero_count))

        def dfs(i, m, n):
            if i == str_len:
                return 0

            if (i, m, n) in dp:
                return dp[(i, m, n)]

            zero_count, one_count = freq[i]

            skip_count = dfs(i + 1, m, n)
            if zero_count <= m and one_count <= n:
                take_count = dfs(i + 1, m - zero_count, n - one_count) + 1
            else:
                take_count = 0

            res = max(skip_count, take_count)

            dp[(i, m, n)] = res

            return res

        return dfs(0, m, n)


class BOTTOM_UP_SOLUTION:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # think of strings as items, number of 0s and 1s as values

        # DP with memoization
        dp = defaultdict(int)

        for s in strs:
            z = s.count("0")
            o = s.count("1")
            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    dp[(i, j)] = max(dp[(i, j)], dp[(i - z, j - o)] + 1)

        return dp[(m, n)]
