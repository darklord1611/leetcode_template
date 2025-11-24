# LeetCode Daily Challenge (2025-09-26)
# Title: Valid Triangle Number
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-triangle-number/
#
# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#
#


# Your solution starts here
from typing import List


class Solution:
	def triangleNumber(self, nums: List[int]) -> int:
		# 1 1 2 3 4 5 6 7 8 8 8

		# sort the number ascendingly
		# then loop through, fix the first 2 numbers, let's call them A and B, binary search on the rest to find the breaking point

		# find the first index of number C where A + B <= C aka we no longer have valid triangle -> then calculate # of valid triplets for a pair of (A, B)

		# iterate to find the rest -> time complexity: O(n^2 x logn)

		def check_valid_triangle(a, b, c):
			return (a + b > c) and (a + c > b) and (b + c > a)

		nums.sort()
		n = len(nums)
		triplet_count = 0
		for i in range(n - 2):
			for j in range(i + 1, n - 1):
				low = j + 1
				high = n - 1

				while low <= high:
					mid = (low + high) // 2

					if check_valid_triangle(nums[i], nums[j], nums[mid]):
						low = mid + 1
					else:
						high = mid - 1

				triplet_count += low - (j + 1)

		# Time complexity: O(n^2 x logn)
		# Space complexity: O(1)
		return triplet_count
