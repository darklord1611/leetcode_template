# LeetCode Daily Challenge (2026-01-04)\n# Title: Four Divisors\n# Difficulty: Medium\n# Acceptance Rate: 47.117646576667404\n# Tags: Array, Math\n# URL: https://leetcode.com/problems/four-divisors/\n#\n# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
#
#


# Your solution starts here
import math
from typing import List


class Solution:
	def sumFourDivisors(self, nums: List[int]) -> int:
		# product of two primes?
		# is it conclusive if we find one pair?

		# think about prime factorization, how do we calculate number of divisors based on that?
		# think about how to deconstruct and potential cases

		def is_prime(num):
			if num <= 1:
				return False

			for i in range(2, int(math.sqrt(num)) + 1):
				if num % i == 0:
					return False

			return True

		def sum_if_four_divisors(n: int) -> int:
			# ----- Case 1: p^3 -----
			p = round(n ** (1 / 3))
			if p**3 == n and is_prime(p):
				return 1 + p + p * p + n

			# ----- Case 2: p * q -----
			for i in range(2, int(math.sqrt(n)) + 1):
				if n % i == 0:
					j = n // i
					if i != j and is_prime(i) and is_prime(j):
						return 1 + i + j + n
					return 0

			return 0

		ans = 0

		for num in nums:
			ans += sum_if_four_divisors(num)

		return ans
