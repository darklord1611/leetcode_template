# LeetCode Daily Challenge (2025-12-08)\n# Title: Count Square Sum Triples\n# Difficulty: Easy\n# Acceptance Rate: 75.21654991622408\n# Tags: Math, Enumeration\n# URL: https://leetcode.com/problems/count-square-sum-triples/\n#\n# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 &lt;= a, b, c &lt;= n.
#
#


# Your solution starts here


class Solution:
	def countTriples(self, n: int) -> int:
		# we can safely assume that a < b, then for every (a, b) pair -> the total number of triples would be x2

		# brute-force O(n^3), notice that if we fix two numbers b and c -> then we could use binary search for the last number a -> O(n^2logn)

		total_pairs = 0

		# this make sure that we get the order right, k < j < i
		for i in range(n + 1):
			for j in range(i):
				low = 0
				high = j - 1

				b_2 = j * j
				c_2 = i * i

				while low <= high:
					mid = low + (high - low) // 2
					a_2 = mid * mid
					if a_2 + b_2 == c_2:
						total_pairs += 2
						break
					elif a_2 + b_2 > c_2:
						high = mid - 1
					else:
						low = mid + 1

		# Time: O(n^2 * logn)
		return total_pairs
