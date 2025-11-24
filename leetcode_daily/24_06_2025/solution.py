# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from typing import List


class Solution:
	def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
		# for a particular index, we need to check in the range of [i - k, i + k] if there any index j where nums[j] == key
		# prefix_sum -> each index would store the number of previous indices where nums[indices] == key

		n = len(nums)
		prefix_counts = [0 for _ in range(n)]
		res = []
		prefix_counts[0] = 1 if nums[0] == key else 0

		for i in range(1, n):
			prefix_counts[i] = (prefix_counts[i - 1] + 1) if nums[i] == key else prefix_counts[i - 1]

		for i in range(n):
			# count(a, b) = count(0, b) - count(0, a - 1)
			left_bound = max(i - k, 0)
			right_bound = min(i + k, n - 1)
			if left_bound == 0:
				keys_within_range = prefix_counts[right_bound]
			else:
				keys_within_range = prefix_counts[right_bound] - prefix_counts[left_bound - 1]
			if keys_within_range > 0:
				res.append(i)

		return res
