# LeetCode Daily Challenge (2025-07-16)
# Title: Find the Maximum Length of Valid Subsequence I
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
#
# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:
#
#
# 	(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
#
#
# Return the length of the longest valid subsequence of nums.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#


# Your solution starts here
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # same parity -> all even, all odd or alternating even-odd, odd-even
        # so we just count the length of 4 possible ordering and take the max

        n = len(nums)
        next_parity_even_odd = 0
        next_parity_odd_even = 1
        cur_lens = [
            0 for _ in range(4)
        ]  # [all-even, all-odd, alt-even-odd, alt-odd-even]

        for i in range(n):
            if nums[i] % 2 == 0:
                cur_lens[0] += 1
            else:
                cur_lens[1] += 1

            if nums[i] % 2 == next_parity_even_odd:
                cur_lens[2] += 1
                next_parity_even_odd = 1 - next_parity_even_odd

            if nums[i] % 2 == next_parity_odd_even:
                cur_lens[3] += 1
                next_parity_odd_even = 1 - next_parity_odd_even

        # Time complexity: O(n)
        # Space complexity: O(1)
        return max(cur_lens)
