# LeetCode Daily Challenge (2025-05-04)
# Title: Number of Equivalent Domino Pairs
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
# 
# Return the number of pairs (i, j) for which 0 &lt;= i &lt; j &lt; dominoes.length, and dominoes[i] is equivalent to dominoes[j].
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # orders within the dominoes doesn't matter, [a, b] is the same as [b, a]
        # suppose we got n equivalent "index" -> how many pairs in total? -> combinatorics

        n = len(dominoes)
        freq = {}
        total_pairs = 0

        for i in range(n):
            min_side = min(dominoes[i][0], dominoes[i][1])
            max_side = max(dominoes[i][0], dominoes[i][1])
            if (min_side, max_side) not in freq:
                freq[(min_side, max_side)] = 1
            else:
                freq[(min_side, max_side)] += 1
        
        for key in freq:
            if freq[key] >= 2:
                total_pairs += freq[key] * (freq[key] - 1) // 2

        return total_pairs
