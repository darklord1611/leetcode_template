# LeetCode Daily Challenge (2025-05-11)
# Title: Three Consecutive Odds
# Difficulty: Easy
# URL: https://leetcode.com/problems/three-consecutive-odds/
#
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
#


# Your solution starts here
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True

        return False
