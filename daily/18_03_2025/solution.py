# LeetCode Daily Challenge (2025-03-18)
# Title: Longest Nice Subarray
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-nice-subarray/
#
# You are given an array nums consisting of positive integers.
#
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
#
# Return the length of the longest nice subarray.
#
# A subarray is a contiguous part of an array.
#
# Note that subarrays of length 1 are always considered nice.
#
#


# Your solution starts here
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # sliding window -> how to efficiently compute the condition for all numbers in the current window
        # bit mask maintaining the set bits -> if the current number AND with the mask != 0 -> exist overlapped bits -> the AND result between two number will != 0
        n = len(nums)
        max_len = 1
        bit_mask = 0
        left = 0
        for right in range(n):
            while (
                bit_mask & nums[right] != 0
            ):  # shift the left ptr to appropriate index
                bit_mask = bit_mask ^ nums[left]
                left += 1

            bit_mask = bit_mask | nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len
