# LeetCode Daily Challenge (2025-10-31)\n# Title: The Two Sneaky Numbers of Digitville\n# Difficulty: Easy\n# Acceptance Rate: 89.84906138420611\n# Tags: Array, Hash Table, Math\n# URL: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/\n#\n# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.
#
# As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
	def getSneakyNumbers(self, nums: List[int]) -> List[int]:
		freq = defaultdict(int)
		ans = []
		for num in nums:
			freq[num] += 1
			if freq[num] == 2:
				ans.append(num)

		return ans
