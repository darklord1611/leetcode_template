# LeetCode Daily Challenge (2025-11-25)\n# Title: Smallest Integer Divisible by K\n# Difficulty: Medium\n# Acceptance Rate: 47.36255736667194\n# Tags: Hash Table, Math\n# URL: https://leetcode.com/problems/smallest-integer-divisible-by-k/\n#\n# Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
#
# Return the length of n. If there is no such n, return -1.
#
# Note: n may not fit in a 64-bit signed integer.
#
#


# Your solution starts here


class Solution:
	def smallestRepunitDivByK(self, K: int) -> int:
		# think about how can we simulate the numbers 1, 11, 111, 1111 without overflows?

		# think about possible remainders when we divide by k(think of buckets)? What happens if we loop more than k times? -> the remainders are bounded to repeat

		remainder = 0
		for length_N in range(1, K + 1):
			remainder = (remainder * 10 + 1) % K
			if remainder == 0:
				return length_N
		return -1
