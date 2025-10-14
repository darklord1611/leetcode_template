# LeetCode Daily Challenge (2025-03-09)
# Title: Alternating Groups II
# Difficulty: Medium
# URL: https://leetcode.com/problems/alternating-groups-ii/
#
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
#
#
# 	colors[i] == 0 means that tile i is red.
# 	colors[i] == 1 means that tile i is blue.
#
#
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
#
# Return the number of alternating groups.
#
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
#
#

from typing import List


# Your solution starts here
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        group_count = 0

        # loop from -(k - 1) to n - 1 -> cover the entire circle
        start_index = -(k - 1)
        expected_num = 1 - colors[start_index]
        left = start_index
        for right in range(start_index + 1, n):
            if colors[right] != expected_num:
                left = right
                expected_num = 1 - colors[right]
                continue

            if right - left + 1 == k:
                group_count += 1
                left += 1

            expected_num = 1 - colors[right]

        return group_count
