# LeetCode Daily Challenge (2026-01-20)\n# Title: Construct the Minimum Bitwise Array I\n# Difficulty: Easy\n# Acceptance Rate: 76.09953072137947\n# Tags: Array, Bit Manipulation\n# URL: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/\n#\n# You are given an array nums consisting of n prime integers.
#
# You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
#
# Additionally, you must minimize each value of ans[i] in the resulting array.
#
# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minBitwiseArray(self, nums: List[int]) -> List[int]:
		n = len(nums)
		ans = []

		for num in nums:
			is_valid = False
			for i in range(num):
				if (i | (i + 1)) == num:
					is_valid = True
					ans.append(i)
					break

			if not is_valid:
				ans.append(-1)

		return ans
