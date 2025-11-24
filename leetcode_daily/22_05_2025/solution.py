# LeetCode Daily Challenge (2025-05-22)
# Title: Zero Array Transformation III
# Difficulty: Medium
# URL: https://leetcode.com/problems/zero-array-transformation-iii/
#
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].
#
# Each queries[i] represents the following action on nums:
#
#
# 	Decrement the value at each index in the range [li, ri] in nums by at most 1.
# 	The amount by which the value is decremented can be chosen independently for each index.
#
#
# A Zero Array is an array with all its elements equal to 0.
#
# Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.
#
#


# Your solution starts here
import heapq
from typing import List


class Solution:
	def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
		# how many queries needed to make the first element satisfied? nums[0] queries with left endpoints be nums[0]
		# notice that we want to process queries to make the first element valid before moving onto to the second element -> sort the queries according to the start index
		# suppose we already have k queries that include current number, which one should we prioritize? the ones with larger ending indices -> cover more numbers -> use max heap to store valid queries for an index

		# how to keep track of the number of operations needed to make the current number and potential future numbers valid? -> difference array

		queries.sort(key=lambda x: x[0])
		heap = []
		deltaArray = [0] * (len(nums) + 1)
		operations = 0
		j = 0
		for i, num in enumerate(nums):
			# reset the number of operations needed to make the current number valid
			# first part would be the number of valid ranges (processed by previous number at index i - 1) that actually include the current number (we resuse this) + the (negative) count of invalid ranges that actually ends at index - 1 and leaves index i untouched
			operations = operations + deltaArray[i]

			# process and store all the queries that do have an effect on the current number
			while j < len(queries) and queries[j][0] <= i:
				heapq.heappush(heap, -queries[j][1])
				j += 1

			# greedily take the queries with larger ending indices
			while operations < num and heap and -heap[0] >= i:
				operations += 1

				# update the index next to the right bound of the query. For example if a query ends at index i, then we know that value at index i + 1 is untouched, therefore the number of operations should be restored to the original
				deltaArray[-heapq.heappop(heap) + 1] -= 1
			if operations < num:
				return -1

		# Time Complexity: O(n + m * log(m))
		# Space Complexity: O(n + m)

		# current elements in the heap are the unused queries
		return len(heap)
