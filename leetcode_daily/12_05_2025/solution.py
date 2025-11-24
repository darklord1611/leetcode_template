# LeetCode Daily Challenge (2025-05-12)
# Title: Finding 3-Digit Even Numbers
# Difficulty: Easy
# URL: https://leetcode.com/problems/finding-3-digit-even-numbers/
#
# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
#
# 	The integer consists of the concatenation of three elements from digits in any arbitrary order.
# 	The integer does not have leading zeros.
# 	The integer is even.
#
#
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.
#
#


# Your solution starts here

from collections import defaultdict
from typing import List


class Solution:
	def findEvenNumbers(self, digits: List[int]) -> List[int]:
		# no odd integers -> must be an even number at the unit index
		# no leading zeros -> must be a number != 0 at the first index
		# the range of possible numbers is from 100 to 999 -> loop through each number, record the frequency and check with our frequency map
		res = []
		freq = {}

		for digit in digits:
			freq[digit] = freq.get(digit, 0) + 1

		for i in range(100, 1000):
			if i % 2 != 0:
				continue

			cur_freq = {}
			temp = i
			is_valid = True

			while temp != 0:
				cur_digit = temp % 10
				cur_freq[cur_digit] = cur_freq.get(cur_digit, 0) + 1
				temp = temp // 10

			for key in cur_freq:
				if key not in freq or freq[key] < cur_freq[key]:
					is_valid = False
					break

			if is_valid:
				res.append(i)

		# Time Complexity: O(10^n) -> n is number of digits
		# Space Complexity: O(1)

		return res


# Approach 2: Brute Force


class Solution2:
	def findEvenNumbers(self, digits: List[int]) -> List[int]:
		# no odd integers -> must be an even number at the unit index
		# no leading zeros -> must be a number != 0 at the first index

		res = []
		freq = defaultdict(int)
		valid_last_nums = set()
		k = 3
		# store the possible numbers for the last index, start from there

		for digit in digits:
			freq[digit] += 1
			if digit % 2 == 0:
				valid_last_nums.add(digit)

		def backtrack(cur_index: int, cur_num: int, k: int) -> None:
			if cur_index == k:
				for num in valid_last_nums:
					temp = num
					freq[num] -= 1
					backtrack(cur_index - 1, temp, k)
					freq[num] += 1
				return

			if cur_index == 1:
				for key in freq:
					if key != 0 and freq[key] >= 1:
						temp = cur_num
						temp += 10 ** (k - cur_index) * key
						res.append(temp)
				return

			for key in freq:
				if freq[key] >= 1:
					temp = cur_num
					temp += 10 ** (k - cur_index) * key
					freq[key] -= 1
					backtrack(cur_index - 1, temp, k)
					freq[key] += 1

			return

		backtrack(k, 0, k)
		res.sort()
		return res
