# LeetCode Daily Challenge (2025-11-22)\n# Title: Find Minimum Operations to Make All Elements Divisible by Three\n# Difficulty: Easy\n# Acceptance Rate: 89.38493187442235\n# Tags: Array, Math\n# URL: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/\n#\n# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
#
# Return the minimum number of operations to make all elements of nums divisible by 3.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minimumOperations(self, nums: List[int]) -> int:
		total_ops = 0

		for num in nums:
			r = num % 3

			if r == 0:
				continue
			else:
				total_ops += min(r, 3 - r)

		return total_ops
