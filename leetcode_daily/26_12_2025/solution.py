# LeetCode Daily Challenge (2025-12-26)\n# Title: Minimum Penalty for a Shop\n# Difficulty: Medium\n# Acceptance Rate: 67.98831177881983\n# Tags: String, Prefix Sum\n# URL: https://leetcode.com/problems/minimum-penalty-for-a-shop/\n#\n# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters &#39;N&#39; and &#39;Y&#39;:
#
#
# 	if the ith character is &#39;Y&#39;, it means that customers come at the ith hour
# 	whereas &#39;N&#39; indicates that no customers come at the ith hour.
#
#
# If the shop closes at the jth hour (0 &lt;= j &lt;= n), the penalty is calculated as follows:
#
#
# 	For every hour when the shop is open and no customers come, the penalty increases by 1.
# 	For every hour when the shop is closed and customers come, the penalty increases by 1.
#
#
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
#
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
#
#


# Your solution starts here


class Solution:
	def bestClosingTime(self, customers: str) -> int:
		# shop is open -> X
		# customers come -> Y
		# X and not Y -> penalized by 1
		# Not X and Y -> penalized by 1

		# close at time i -> how do we calculate the penalty? -> would be the sum of Ns from 0 to i + Ys from i to n - 1
		n = len(customers)
		max_Y = customers.count("Y", 0)
		max_N = customers.count("N", 0)
		cur_Y = 0
		cur_N = 0

		min_index = n
		min_penalty = max_N  # close after the latest possible hour

		for i in range(n):
			# calculate the penalties
			open_and_no_customers = max(cur_N, 0)
			closed_and_have_customers = max_Y - cur_Y

			cur_penalty = open_and_no_customers + closed_and_have_customers
			if min_penalty > cur_penalty:
				min_penalty = cur_penalty
				min_index = i
			elif min_penalty == cur_penalty:
				min_penalty = cur_penalty
				min_index = min(min_index, i)  # tiebreaker

			if customers[i] == "Y":
				cur_Y += 1
			else:
				cur_N += 1

		return min_index
