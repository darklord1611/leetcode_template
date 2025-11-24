# LeetCode Daily Challenge (2025-11-04)\n# Title: Find X-Sum of All K-Long Subarrays I\n# Difficulty: Easy\n# Acceptance Rate: 65.81501063898382\n# Tags: Array, Hash Table, Sliding Window, Heap (Priority Queue)\n# URL: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/\n#\n# You are given an array nums of n integers and two integers k and x.
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
from typing import List


class Solution_1:
	def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
		ans = []
		n = len(nums)
		for i in range(n - k + 1):
			cur_ans = 0
			freq = {}
			for j in range(i, i + k):
				freq[nums[j]] = freq.get(nums[j], 0) + 1

			sorted_freq = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)[:x]  # sort by freq and then by value

			for val, key in sorted_freq:  # only take x element
				cur_ans += key * val

			ans.append(cur_ans)

		# Time complexity: O(n * (k + klogk))
		# Space complexity: O(k)

		# there should be another more optimal approach using sliding window
		return ans
