# LeetCode Daily Challenge (2025-11-17)\n# Title: Check If All 1's Are at Least Length K Places Away\n# Difficulty: Easy\n# Acceptance Rate: 59.093708117506424\n# Tags: Array\n# URL: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/\n#\n# Given an binary array nums and an integer k, return true if all 1&#39;s are at least k places away from each other, otherwise return false.
#
#


# Your solution starts here
from typing import List


class Solution:
	def kLengthApart(self, nums: List[int], k: int) -> bool:
		# two pointers -> one for the previous instance of 1, the other for the current 1

		prev = -1
		cur = -1
		n = len(nums)
		for i in range(n):
			if nums[i] == 1:
				prev = cur
				cur = i

				if prev == -1:  # we haven't reach the second 1s yet
					continue

				if cur - prev <= k:
					return False

		return True
