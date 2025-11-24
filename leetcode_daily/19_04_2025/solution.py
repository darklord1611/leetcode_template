# LeetCode Daily Challenge (2025-04-19)
# Title: Count the Number of Fair Pairs
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-the-number-of-fair-pairs/
#
# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
#
# A pair (i, j) is fair if:
#
#
# 	0 &lt;= i &lt; j &lt; n, and
# 	lower &lt;= nums[i] + nums[j] &lt;= upper
#
#
#


# Your solution starts here
from typing import List


class Solution:
	def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
		# does order between numbers matter? what if we switch place of i and j?
		# we want the count and not the exact indexes
		# suppose the number is sorted, what happen if a pair (i, j) is valid with i << j? Think about the pairs in-between
		# lower <= ... <= high -> can we simplify this condition? -> 0 <= ... <= high + 1 would contains everything we need + some extras -> extras? just substract counts from 0 <= ... <= lower -> done
		n = len(nums)
		nums.sort()

		def lower_bound(val):
			left = 0
			right = n - 1
			res = 0
			while left < right:
				target_sum = nums[left] + nums[right]
				if target_sum < val:
					res += right - left
					left += 1
				else:
					right -= 1

			return res

		return lower_bound(upper + 1) - lower_bound(lower)
