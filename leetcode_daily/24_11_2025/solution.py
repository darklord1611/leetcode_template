# LeetCode Daily Challenge (2025-11-24)\n# Title: Binary Prefix Divisible By 5\n# Difficulty: Easy\n# Acceptance Rate: 48.629856088285734\n# Tags: Array, Bit Manipulation\n# URL: https://leetcode.com/problems/binary-prefix-divisible-by-5/\n#\n# You are given a binary array nums (0-indexed).
#
# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
#
#
# 	For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
#
#
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
#
#


# Your solution starts here
from typing import List


class Solution:
	def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
		# remember bitwise operators, <<, >>
		n = len(nums)
		ans = [False for _ in range(n)]
		cur_num = 0
		for i, num in enumerate(nums):
			if num == 0:
				cur_num = cur_num << 1  # shift left 1 unit, ex: 01 -> 010
			else:
				cur_num = (cur_num << 1) | 1  # shift left 1 unit, ex: 01 -> 011

			if cur_num % 5 == 0:
				ans[i] = True

		# Time: O(n)
		# Space: O(n)
		return ans


from typing import Dict


def temp(abc: Dict):
	pass
