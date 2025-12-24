# LeetCode Daily Challenge (2025-12-24)\n# Title: Apple Redistribution into Boxes\n# Difficulty: Easy\n# Acceptance Rate: 76.15867530405428\n# Tags: Array, Greedy, Sorting\n# URL: https://leetcode.com/problems/apple-redistribution-into-boxes/\n#\n# You are given an array apple of size n and an array capacity of size m.
#
# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
#
# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
#
# Note that, apples from the same pack can be distributed into different boxes.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
		# just be greedy
		total_apples = sum(apple)

		capacity.sort()
		m = len(capacity)
		cur_total_cap = 0
		box_count = 0
		for i in range(m - 1, -1, -1):
			cur_total_cap += capacity[i]
			box_count += 1

			if cur_total_cap >= total_apples:
				break

		return box_count
