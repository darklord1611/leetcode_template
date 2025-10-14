# LeetCode Daily Challenge (2025-05-03)
# Title: Minimum Domino Rotations For Equal Row
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
#
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
#
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
#
# If it cannot be done, return -1.
#
#


# Your solution starts here
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # top and bottom can swap values
        # top or bottom values should be the same value(we call it k) 1 <= k <= 6 -> for each index, value k should be either at the tops[index] or bottoms[index] or BOTH
        # find the valid k first -> then we need to find minimum number of swaps
        # ideas? store the frequency of each possible k at both arrays -> any k that count(k) >= len(tops) will be valid
        # examine the k with largest count -> why largest? larger count == less rotations
        # do another pass to find the minimum rotations

        # beware of the duplicate situtaions, rembember set union

        n = len(tops)
        max_num = -1
        max_count = 0
        counts = [[0, 0, 0] for _ in range(7)]

        for i in range(n):
            counts[tops[i]][0] += 1
            counts[bottoms[i]][1] += 1
            if tops[i] == bottoms[i]:  # record the duplicate count
                counts[tops[i]][2] += 1

        for i in range(1, 7):
            freq = counts[i][0] + counts[i][1] - counts[i][2]
            if freq >= n and freq > max_count:
                max_count = counts[i][0] + counts[i][1]
                max_num = i

        if max_count == 0:
            return -1

        return min(n - counts[max_num][0], n - counts[max_num][1])
