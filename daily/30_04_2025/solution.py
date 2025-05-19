# LeetCode Daily Challenge (2025-04-30)
# Title: Find Numbers with Even Number of Digits
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#
# Given an array nums of integers, return how many of them contain an even number of digits.
#
#


# Your solution starts here
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            temp = num
            cur_count = 0
            while temp != 0:
                temp = temp // 10
                cur_count += 1

            if cur_count % 2 == 0:
                count += 1

        return count
