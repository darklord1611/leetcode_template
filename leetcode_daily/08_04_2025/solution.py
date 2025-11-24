# LeetCode Daily Challenge (2025-04-08)
# Title: Minimum Number of Operations to Make Elements in Array Distinct
# Difficulty: Easy
# URL: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
#
# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
#
#
# 	Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
#
#
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.
#
#


# Your solution starts here
import math
from typing import List


class Solution:
	def minimumOperations(self, nums: List[int]) -> int:
		# keep track of the count and also the latest index of each number -> find the largest duplicate index
		# the latest index or the near-to-last index should we remove?
		# why not iterate from the end? -> much easier lol :v
		freq = {}
		prev_indexes = {}
		max_duplicate_index = -1
		n = len(nums)
		for i in range(n):
			if nums[i] not in freq:
				freq[nums[i]] = [1, i]
			else:
				freq[nums[i]][0] += 1
				prev_indexes[nums[i]] = freq[nums[i]][1]
				freq[nums[i]][1] = i

		for key in freq:
			if freq[key][0] >= 2:
				max_duplicate_index = max(max_duplicate_index, prev_indexes[key])

		return math.ceil((max_duplicate_index + 1) / 3)  # plus one indicates number of elements that we remove
