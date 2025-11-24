# LeetCode Daily Challenge (2025-05-10)
# Title: Minimum Equal Sum of Two Arrays After Replacing Zeros
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
#
# You are given two arrays nums1 and nums2 consisting of positive integers.
#
# You have to replace all the 0&#39;s in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.
#
# Return the minimum equal sum you can obtain, or -1 if it is impossible.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minSum(self, nums1: List[int], nums2: List[int]) -> int:
		# two arrays, each array has n non-zero elements, m zeroed elements,
		# 3 situations -> both arrays have no zero elements
		# -> one of the arrays has no zero elements while the other have some ( >= 1)
		# -> both arrays have some number of zero elements
		n = len(nums1)
		m = len(nums2)

		total_sums = [0, 0]
		num_zeros = [0, 0]

		for i in range(n):
			total_sums[0] += nums1[i]
			if nums1[i] == 0:
				num_zeros[0] += 1

		for i in range(m):
			total_sums[1] += nums2[i]
			if nums2[i] == 0:
				num_zeros[1] += 1

		if num_zeros[0] == 0 and num_zeros[1] == 0:
			return total_sums[0] if total_sums[0] == total_sums[1] else -1

		if num_zeros[0] > 0 and num_zeros[1] > 0:
			return max(total_sums[0] + num_zeros[0], total_sums[1] + num_zeros[1])  # we need to find the maximum sum after transform all zeroes to minimum positive number(ones)

		no_zero_index = 0 if num_zeros[0] == 0 else 1
		cur_max_sum_index = 0 if total_sums[0] > total_sums[1] else 1
		if no_zero_index != cur_max_sum_index or total_sums[cur_max_sum_index] < total_sums[1 - cur_max_sum_index] + num_zeros[1 - no_zero_index]:
			return -1

		return total_sums[cur_max_sum_index]
