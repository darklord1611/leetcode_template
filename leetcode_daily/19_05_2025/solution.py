# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
	def triangleType(self, nums: List[int]) -> str:
		freq = defaultdict(int)

		def check_triangle(a, b, c):
			return (a + b) > c and (b + c) > a and (c + a) > b

		if not check_triangle(nums[0], nums[1], nums[2]):
			return "none"

		for num in nums:
			freq[num] += 1

		if len(freq) == 1:
			return "equilateral"
		elif len(freq) == 2:
			return "isosceles"

		return "scalene"
