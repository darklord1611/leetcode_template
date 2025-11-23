# LeetCode Daily Challenge (2025-11-23)\n# Title: Greatest Sum Divisible by Three\n# Difficulty: Medium\n# Acceptance Rate: 51.489134126863675\n# Tags: Array, Dynamic Programming, Greedy, Sorting\n# URL: https://leetcode.com/problems/greatest-sum-divisible-by-three/\n#\n# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.
#
#


# Your solution starts here

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # record each type of numbers a % 3 == 0, a % 3 == 1, a % 3 == 2
        # we can add in 4 seperate ways, numbers that are naturally divisible by 3 -> ex: 3, 6, 9
        # numbers that % 3 == 1 but we have frequency to be a multiple of 3
        # numbers that % 3 == 2 but we have frequency to be a multiple of 3
        # we can combine numbers % 3 == 1 and % 3 == 2 in greedy ways

        a = [num for num in nums if num % 3 == 0]
        b = sorted([num for num in nums if num % 3 == 1], reverse=True)
        c = sorted([num for num in nums if num % 3 == 2], reverse=True)
        total_sum = 0

        len_b = len(b)
        len_c = len(c)

        for cnt_b in [len_b - 2, len_b - 1, len_b]:
            if cnt_b >= 0:
                for cnt_c in [len_c - 2, len_c - 1, len_c]:
                    if cnt_c >= 0 and (cnt_b - cnt_c) % 3 == 0:
                        cur_sum = sum(b[:cnt_b]) + sum(c[:cnt_c])
                        total_sum = max(total_sum, cur_sum)

        return total_sum + sum(a)
