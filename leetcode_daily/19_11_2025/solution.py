# LeetCode Daily Challenge (2025-11-19)\n# Title: Keep Multiplying Found Values by Two\n# Difficulty: Easy\n# Acceptance Rate: 71.5588435852753\n# Tags: Array, Hash Table, Sorting, Simulation\n# URL: https://leetcode.com/problems/keep-multiplying-found-values-by-two/\n#\n# You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.
#
# You then do the following steps:
#
#
# 	If original is found in nums, multiply it by two (i.e., set original = 2 * original).
# 	Otherwise, stop the process.
# 	Repeat this process with the new number as long as you keep finding the number.
#
#
# Return the final value of original.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
	def findFinalValue(self, nums: List[int], original: int) -> int:
		freq = defaultdict(int)
		cur_ans = original
		for num in nums:
			freq[num] += 1

		while freq[cur_ans] != 0:
			cur_ans = cur_ans * 2

		return cur_ans
