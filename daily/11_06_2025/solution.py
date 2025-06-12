# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0

        n = len(nums)

        for i in range(1, n):
            max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))

        max_diff = max(max_diff, abs(nums[-1] - nums[0]))

        return max_diff
