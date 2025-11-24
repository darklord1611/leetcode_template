# LeetCode Daily Challenge (2025-07-30)
# Title: Longest Subarray With Maximum Bitwise AND
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
#
# You are given an integer array nums of size n.
#
# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
#
#
# 	In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
#
#
# Return the length of the longest such subarray.
#
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
#
# A subarray is a contiguous sequence of elements within an array.
#
#


# Your solution starts here
from typing import List


class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		# bitwise AND only decrease the value, -> the value# will be maximum when we have the maximum number in the arrays
		# just count the consecutive occurrences of the maximum number in the array
		n = len(nums)
		max_num = max(nums)

		cur_count = 0
		max_count = 0

		for i in range(n):
			if nums[i] == max_num:
				cur_count += 1
				max_count = max(max_count, cur_count)
			else:
				cur_count = 0

		# Time Complexity: O(n) -> single pass through the array
		# Space Complexity: O(1) -> no extra space used

		return max_count
