# LeetCode Daily Challenge (2025-11-05)\n# Title: Find X-Sum of All K-Long Subarrays II\n# Difficulty: Hard\n# Acceptance Rate: 23.262888248479026\n# Tags: Array, Hash Table, Sliding Window, Heap (Priority Queue)\n# URL: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/\n#\n# You are given an array nums of n integers and two integers k and x.
#
# The x-sum of an array is calculated by the following procedure:
#
#
# 	Count the occurrences of all elements in the array.
# 	Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# 	Calculate the sum of the resulting array.
#
#
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
#
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
#
#


# Your solution starts here
from collections import defaultdict

from sortedcontainers import SortedList


class Helper:
	def __init__(self, x):
		self.x = x
		self.result = 0
		self.large = SortedList()
		self.small = SortedList()
		self.occ = defaultdict(int)

	def insert(self, num):
		if self.occ[num] > 0:
			self.internal_remove((self.occ[num], num))
		self.occ[num] += 1
		self.internal_insert((self.occ[num], num))

	def remove(self, num):
		self.internal_remove((self.occ[num], num))
		self.occ[num] -= 1
		if self.occ[num] > 0:
			self.internal_insert((self.occ[num], num))

	def get(self):
		return self.result

	def internal_insert(self, p):
		if len(self.large) < self.x or p > self.large[0]:
			self.result += p[0] * p[1]
			self.large.add(p)
			if len(self.large) > self.x:
				to_remove = self.large[0]
				self.result -= to_remove[0] * to_remove[1]
				self.large.remove(to_remove)
				self.small.add(to_remove)
		else:
			self.small.add(p)

	def internal_remove(self, p):
		if p >= self.large[0]:
			self.result -= p[0] * p[1]
			self.large.remove(p)
			if self.small:
				to_add = self.small[-1]
				self.result += to_add[0] * to_add[1]
				self.small.remove(to_add)
				self.large.add(to_add)
		else:
			self.small.remove(p)


class Solution:
	# large array holds the top x elements, whereas small array holds the rest, updates follow the principle of first removing the old copy (occ, num) -> refill temporarily by bringing in the largest tuple from small and then insert the new copy after either increase/decrease the element
	def findXSum(self, nums, k, x):
		helper = Helper(x)
		ans = []

		for i in range(len(nums)):
			helper.insert(nums[i])
			if i >= k:
				helper.remove(nums[i - k])
			if i >= k - 1:
				ans.append(helper.get())

		# Time complexity: O(nlogn)
		# Space complexity: O(n)
		return ans
