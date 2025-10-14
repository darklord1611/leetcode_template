# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from typing import List
from collections import defaultdict


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # our job is to find subarrays of length k that are strictly increasing, with k = 3, example -> 5,6,7
        # we must check if there exist 2 such subarrays and they are adjacent
        # maintain a sliding window of k -> record each subarray satisfied
        valid_start_idx = defaultdict(int)
        left = 0
        n = len(nums)
        for right in range(n):
            if nums[right] - nums[right - 1] <= 0:
                left = right  # if we encounter a not strictly increase scenario -> immediately jump ahead
            if right - left + 1 == k:
                # we have a subarray of length k
                if (
                    left - k >= 0 and valid_start_idx[left - k] == 1
                ):  # check for the first adjacent subarray
                    return True
                valid_start_idx[left] = 1
                left += 1

        # Time Complexity: O(n)
        # Space Complexity: O(m) -> m is number of valid subarrays
        return False
