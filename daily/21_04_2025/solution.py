# LeetCode Daily Challenge (2025-04-21)
# Title: Count the Hidden Sequences
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-the-hidden-sequences/
#
# You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].
#
# You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.
#
#
# 	For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
#
#
# 		[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
# 		[5, 6, 3, 7] is not possible since it contains an element greater than 6.
# 		[1, 2, 3, 4] is not possible since the differences are not correct.
#
#
#
#
# Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.
#
#


# Your solution starts here
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # diff array of length n -> generate hidden sequence of length n + 1
        # choices are deterministic -> if we choose the first number to be a -> there is only 1 hidden sequence constructed by following the diff array
        # valid choices? -> satisfy the diff array + each number in [lower, upper]
        # Generate all choices recursively, keep track of the min and max -> check?

        n = len(differences)
        prefix_sum_diffs = [-1 for _ in range(n)]
        prefix_sum_diffs[0] = differences[0]
        min_diff = prefix_sum_diffs[0]
        max_diff = prefix_sum_diffs[0]
        total_count = 0

        for i in range(1, n):
            prefix_sum_diffs[i] = prefix_sum_diffs[i - 1] + differences[i]
            min_diff = min(prefix_sum_diffs[i], min_diff)
            max_diff = max(prefix_sum_diffs[i], max_diff)

        for i in range(lower, upper + 1):
            if i + min_diff < lower or i + max_diff > upper:
                continue

            total_count += 1

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        return total_count
