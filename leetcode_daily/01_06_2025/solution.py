# LeetCode Daily Challenge (2025-06-01)
# Title: Distribute Candies Among Children II
# Difficulty: Medium
# URL: https://leetcode.com/problems/distribute-candies-among-children-ii/
#
# You are given two positive integers n and limit.
#
# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.
#
#


# Your solution starts here


class Solution:
	def distributeCandies(self, n: int, limit: int) -> int:
		# n candies for 3 children
		# suppose we assign k1 candies to the first child, then we left with n - k1 candies and 2 children
		# do the same, assign k2 candies to the second child, then we left with the third child with n - k1 - k2 candies
		# problem boils down to find all pairs (k1, k2) satisfied k1 <= limit, k2 <= limit, n - (k1 + k2) <= limit, k1 + k2 <= n

		# suppose we give k1 candies to first child, 0 <= k1 <= min(n, limit)
		# then we left with n - k1 candies for the other two remaining children
		# assign k2 candies -> 0 <= k2 <= limit, k1 + k2 <= n -> 0 <= k2 <= min(n - k1, limit)
		# third child gets n - k1 - k2 candies, 0 <= n - k1 - k2 <= limit -> n - k1 - limit <= k2 <= n - k1
		# so for each k1, the valid choices for k2 would be max(0, n - k1 - limit) <= k2 <= min(n - k1, limit)
		if n > 3 * limit:
			return 0
		total_ways = 0

		for k1 in range(0, min(n, limit) + 1):
			left_bound = max(0, n - k1 - limit)
			right_bound = min(n - k1, limit)

			valid_choices = right_bound - left_bound + 1
			if valid_choices > 0:  # exist valid pairs
				total_ways += valid_choices

		# Time Complexity: O(n)
		# Space Complexity: O(1)
		return total_ways
