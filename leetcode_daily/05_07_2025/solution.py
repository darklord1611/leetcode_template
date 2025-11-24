# LeetCode Daily Challenge (2025-07-05)
# Title: Find Lucky Integer in an Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-lucky-integer-in-an-array/
#
# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
#
# Return the largest lucky integer in the array. If there is no lucky integer return -1.
#
#


# Your solution starts here
from collections import Counter
from typing import List


class Solution:
	def findLucky(self, arr: List[int]) -> int:
		count = Counter(arr)
		max_val = -1

		for num in count:
			if count[num] == num:
				max_val = max(num, max_val)

		return max_val
