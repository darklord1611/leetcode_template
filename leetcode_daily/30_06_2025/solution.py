# LeetCode Daily Challenge (2025-06-30)
# Title: Longest Harmonious Subsequence
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-harmonious-subsequence/
#
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
#
#


# Your solution starts here
class Solution:
	def possibleStringCount(self, word: str) -> int:
		cur_char = ""
		cur_count = 1
		res = 0
		for char in word:
			if char == cur_char:
				cur_count += 1
			else:
				res += cur_count - 1  # the character appears at most once
				cur_char = char
				cur_count = 1

		res += cur_count - 1  # account for the last possible sequence of identical characters

		res += 1  # account for the original string where there are no typos

		return res
