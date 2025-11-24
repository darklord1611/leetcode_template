# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here

from typing import List


class Solution:
	def countHillValley(self, nums: List[int]) -> int:
		# [2, 4, 4, 4, 4, 1, 5, 3]
		n = len(nums)

		if len(nums) < 3:
			return 0

		left_neighbor_index = 0
		right_neighbor_index = 2
		count = 0
		i = 1
		while left_neighbor_index < n - 2 and i < n - 1 and right_neighbor_index < n:
			# check if the right index is equal to current number, if yes then keep moving forward until we found a valid right index
			while right_neighbor_index < n - 1 and nums[right_neighbor_index] == nums[i]:
				right_neighbor_index += 1

			if nums[left_neighbor_index] < nums[i] and nums[right_neighbor_index] < nums[i]:
				count += 1

			if nums[left_neighbor_index] > nums[i] and nums[right_neighbor_index] > nums[i]:
				count += 1

			left_neighbor_index = right_neighbor_index - 1
			i = right_neighbor_index
			right_neighbor_index += 1

		# Time Complexity: O(n)
		# Space Complexity: O(1)
		# We could have just removed the adjacent duplicate values for a more standard solution instead of keeping track of indices.

		return count
