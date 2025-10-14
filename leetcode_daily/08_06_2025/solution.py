# LeetCode Daily Challenge (2025-06-08)
# Title: Lexicographical Numbers
# Difficulty: Medium
# URL: https://leetcode.com/problems/lexicographical-numbers/
#
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.
#
#


# Your solution starts here
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # DFS, start from 1, keep adding numbers to it, 1 -> 10, 11, -> ... 100 only if it < n

        res = []

        def dfs(i: str):
            if int(i) > n:
                return

            res.append(int(i))

            for j in range(0, 10):
                dfs(f"{i}{j}")

            return

        for i in range(1, 10):
            dfs(i)

        # Time complexity: O(n)
        return res
