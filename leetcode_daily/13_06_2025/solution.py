# LeetCode Daily Challenge (2025-06-13)
# Title: Minimize the Maximum Difference of Pairs
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
#
# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
#
# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
#
# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
#
#


# Your solution starts here

from typing import List


class Solution:
	def minimizeMax(self, nums: List[int], p: int) -> int:
		# simulate all possible pairs, we need to pick out p pairs, each index appears only once in those pairs, aka we need to pick out p * 2 distinct indices from the array
		# we need to pick p pairs, calculate the abs diff for each pair, pick out the maximum, -> we need to minimize that
		# just pick p pairs with minimum abs diff then we would be fine?

		# simulate would take O(n^2), push all pairs into a min heap, pop out the first p pairs -> done but TLE
		# do we need to simulate? notice that the orders of indices doesn't matter -> what comes to mind? -> sorting
		# [10,1,2,7,1,3] -> [1, 1, 2, 3, 7, 10]

		# what if we were given the min max diff K already? How would that affect the problem? It would boils down to how many pairs < K?
		# Yes/No question essentially

		# so do sorting first then just try for K = 0, 1, ...... max(nums[n - 1] - nums[0]) till we find the answer? -> TLE
		# if we already have p pairs with K = 3, what happen when we consider K = 4?
		# how about K = 2, do the above information enough?
		# above two questions would guide us to binary search on the number K

		n = len(nums)
		nums.sort()

		def countValidPairs(k):
			idx = 0
			cnt = 0
			while idx < n - 1:
				if nums[idx + 1] - nums[idx] <= k:
					cnt += 1
					idx += 2
				else:
					idx += 1
			return cnt

		left = 0
		right = nums[n - 1] - nums[0]

		while left < right:
			mid = (left + right) // 2

			# check the current array if we have enough p pairs
			count = countValidPairs(mid)

			if count >= p:
				right = mid
			else:
				left = mid + 1

		return left
