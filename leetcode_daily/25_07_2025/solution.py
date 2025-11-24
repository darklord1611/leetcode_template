# LeetCode Daily Challenge (2025-07-25)
# Title: Maximum Unique Subarray Sum After Deletion
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
#
# You are given an integer array nums.
#
# You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:
#
#
# 	All elements in the subarray are unique.
# 	The sum of the elements in the subarray is maximized.
#
#
# Return the maximum sum of such a subarray.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
	def maxSum(self, nums: List[int]) -> int:
		# set negative numbers to zeroes -> effectively remove them from final subarray sum
		# then make every element unique by also set any duplicate values to zeroes
		# becareful, if we perform the above two operations, we would end up with an array of multiple zeroes -> go further and conceptually remove all zeroes, we will be left with only positive values -> sum them up and return
		# need to check for an array of full negative values

		max_val = max(nums)

		if max_val <= 0:
			return max_val

		freq = defaultdict(int)
		n = len(nums)

		for i in range(n):
			if nums[i] <= 0 or freq[nums[i]] >= 1:
				nums[i] = 0
			else:
				freq[nums[i]] += 1

		# Time Complexity: O(n)
		# Space Complexity: O(n)
		return sum(nums)
