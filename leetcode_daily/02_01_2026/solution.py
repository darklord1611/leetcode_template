# LeetCode Daily Challenge (2026-01-02)\n# Title: N-Repeated Element in Size 2N Array\n# Difficulty: Easy\n# Acceptance Rate: 77.92272801853237\n# Tags: Array, Hash Table\n# URL: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/\n#\n# You are given an integer array nums with the following properties:
#
#
# 	nums.length == 2 * n.
# 	nums contains n + 1 unique elements.
# 	Exactly one element of nums is repeated n times.
#
#
# Return the element that is repeated n times.
#
#


# Your solution starts here
from typing import List


class Solution:
	def repeatedNTimes(self, nums: List[int]) -> int:
		freq = {}
		for num in nums:
			freq[num] = freq.get(num, 0) + 1

			if freq[num] > 1:
				return num

		return -1
