# LeetCode Daily Challenge (2025-03-19)
# Title: Minimum Operations to Make Binary Array Elements Equal to One I
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
#
# You are given a binary array nums.
#
# You can do the following operation on the array any number of times (possibly zero):
#
#
# 	Choose any 3 consecutive elements from the array and flip all of them.
#
#
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
#
# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minOperations(self, nums: List[int]) -> int:
		# flipping from left to right -> making sure that the preceding indexes are already satisfied
		# first bit of every flip should be a zero aka [0, 1, 1] -> ok, [1, 0, 1] -> flipping now is not ok
		# only flip leftmost bit if needed -> why? need to prove the correctness
		n = len(nums)
		left = 0
		window_size = 3
		flip_count = 0
		for right in range(n):
			if right - left + 1 == window_size:
				if nums[left] == 0:
					flip_count += 1
					for i in range(window_size):
						nums[left + i] = 1 - nums[left + i]

				left += 1

		# check if whether still exists some zeroes in the array -> impossible
		for i in range(n - 1, -1, -1):
			if nums[i] == 0:
				return -1

		# Time complexity: O(n)
		# Space complexity: O(1)
		return flip_count
