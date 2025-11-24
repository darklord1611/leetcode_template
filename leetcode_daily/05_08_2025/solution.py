# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from typing import List


class Solution:
	def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
		# brute force, create a mask of used baskets

		n = len(fruits)

		used = [0 for _ in range(n)]

		for i in range(n):
			for j in range(n):
				if not used[j] and fruits[i] <= baskets[j]:
					used[j] = 1
					break

		# unallocated baskets -> number of fruits remain unplaced
		# Time Complexity: O(n^2) -> nested loops
		# Space Complexity: O(n) -> used array to track used baskets

		# We could optimize using segment tree, but too complicate with small inputs
		return n - sum(used)
