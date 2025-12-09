# LeetCode Daily Challenge (2025-12-09)\n# Title: Count Special Triplets\n# Difficulty: Medium\n# Acceptance Rate: 37.784902203782536\n# Tags: Array, Hash Table, Counting\n# URL: https://leetcode.com/problems/count-special-triplets/\n#\n# You are given an integer array nums.
#
# A special triplet is defined as a triplet of indices (i, j, k) such that:
#
#
# 	0 &lt;= i &lt; j &lt; k &lt; n, where n = nums.length
# 	nums[i] == nums[j] * 2
# 	nums[k] == nums[j] * 2
#
#
# Return the total number of special triplets in the array.
#
# Since the answer may be large, return it modulo 109 + 7.
#
#


# Your solution starts here
from typing import List


class Solution:
	def specialTriplets(self, nums: List[int]) -> int:
		# suppose we fix the middle number -> the question becomes how to calculate valid side numbers?

		# if we store the freq up until that index and the total freq -> ok

		partial_freq = {}
		MOD = 10**9 + 7
		total_freq = {}
		n = len(nums)
		ans = 0

		for i in range(n):
			total_freq[nums[i]] = total_freq.get(nums[i], 0) + 1

		for i in range(n):
			num_to_find = nums[i] * 2
			left_count = partial_freq.get(num_to_find, 0)
			right_count = total_freq.get(num_to_find, 0) - left_count
			if num_to_find == 0:  # edge case of zero
				right_count -= 1
			ans = (ans + left_count * right_count) % MOD

			partial_freq[nums[i]] = partial_freq.get(nums[i], 0) + 1

		# Time: O(n)
		# Space: O(n)
		return ans
