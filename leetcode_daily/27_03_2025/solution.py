# LeetCode Daily Challenge (2025-03-27)
# Title: Minimum Index of a Valid Split
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-index-of-a-valid-split/
#
# An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.
#
# You are given a 0-indexed integer array nums of length n with one dominant element.
#
# You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:
#
#
# 	0 &lt;= i &lt; n - 1
# 	nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
#
#
# Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j &lt; i then nums[i, ..., j] denotes an empty subarray.
#
# Return the minimum index of a valid split. If no valid split exists, return -1.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
	def minimumIndex(self, nums: List[int]) -> int:
		# both arrays after split have the same dominant element -> original array also have a single dominant element

		freq = defaultdict(int)
		n = len(nums)
		max_num = -1
		cur_max_count = 0
		for num in nums:
			freq[num] += 1
			if freq[num] > cur_max_count:
				cur_max_count = freq[num]
				max_num = num

		# got the most frequent number in the array -> now loop through each index and check if the split is valid
		cur_max_count = 0

		for i in range(0, n - 1):
			if nums[i] == max_num:
				cur_max_count += 1

			if cur_max_count >= (i + 1) // 2 + 1:  # first part of array after split
				if freq[max_num] - cur_max_count >= (n - i - 1) // 2 + 1:  # 2nd part
					return i

		return -1
