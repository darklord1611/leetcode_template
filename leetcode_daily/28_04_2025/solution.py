# LeetCode Daily Challenge (2025-04-28)
# Title: Count Subarrays With Score Less Than K
# Difficulty: Hard
# URL: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
#
# The score of an array is defined as the product of its sum and its length.
#
#
# 	For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
#
#
# Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.
#
# A subarray is a contiguous sequence of elements within an array.
#
#


# Your solution starts here
from typing import List


class Solution:
	def countSubarrays(self, nums: List[int], k: int) -> int:
		# score = sum * len
		# whenever we expand to a new index, the scores keep increasing -> monotonic -> we can apply sliding window
		# sliding windows, just keep adding the number until satisfy the score, then shrink from the left
		# total valid subrrays = sum(valid subarrays ending at index i for i in range(n))
		# if we have a valid subarray from i to j -> how many valid subarrays ending at index j?

		n = len(nums)
		left = 0
		cur_sum = 0
		count = 0

		for right in range(n):
			cur_sum += nums[right]

			while cur_sum * (right - left + 1) >= k:  # shrink to obtain a valid subarray
				cur_sum -= nums[left]
				left += 1

			count += right - left + 1  # count the available starting choices of a valid subarray ends at index right

		# Time Complexity: O(n)
		# Space Complexity: O(1)
		return count
