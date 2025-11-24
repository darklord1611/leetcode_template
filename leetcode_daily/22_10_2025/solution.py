# LeetCode Daily Challenge (2025-10-22)\n# Title: Maximum Frequency of an Element After Performing Operations II\n# Difficulty: Hard\n# Acceptance Rate: 39.64408605887873\n# Tags: Array, Binary Search, Sliding Window, Sorting, Prefix Sum\n# URL: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/\n#\n# You are given an integer array nums and two integers k and numOperations.
#
# You must perform an operation numOperations times on nums, where in each operation you:
#
#
# 	Select an index i that was not selected in any previous operations.
# 	Add an integer in the range [-k, k] to nums[i].
#
#
# Return the maximum possible frequency of any element in nums after performing the operations.
#
#


# Your solution starts here
from typing import List


class Solution:
	def maxIncreasingSubarrays(self, nums: List[int]) -> int:
		# so we maintain a sliding window of size 2 * k -> we check for valid subarrays when the indices are even

		# even simpler, so we either get our subarrays from one giant increasing array, or from 2 different consecutive increasing subarrays
		# so we can effectively record the current length of increasing subarray -> then compare two options, take from the current or from the 2 last subarrays

		n = len(nums)
		prev_count = 0  # length of the previous increasing subarray
		cur_count = 1  # length of the current increasing subarray
		max_k = 0

		nums.append(-(10**10))  # append a small number to avoid extra checks at the end of the array

		for i in range(n):
			if nums[i] < nums[i + 1]:
				cur_count += 1
			else:
				max_k = max(max_k, cur_count // 2, min(cur_count, prev_count))  # consider 2 options
				prev_count = cur_count
				cur_count = 1

		return max_k
