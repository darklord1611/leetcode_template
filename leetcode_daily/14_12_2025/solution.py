# LeetCode Daily Challenge (2025-12-14)\n# Title: Number of Ways to Divide a Long Corridor\n# Difficulty: Hard\n# Acceptance Rate: 49.06969041635007\n# Tags: Math, String, Dynamic Programming\n# URL: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/\n#\n# Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters &#39;S&#39; and &#39;P&#39; where each &#39;S&#39; represents a seat and each &#39;P&#39; represents a plant.
#
# One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 &lt;= i &lt;= n - 1), at most one divider can be installed.
#
# Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.
#
# Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.
#
#


# Your solution starts here


class Solution:
	def numberOfWays(self, corridor: str) -> int:
		# stars and bars kind of problems, we can have arbitrary number of plants, possible 0 plants between dividers

		# convert to standard stars and bars, what would it look like? ah we must have exactly two seats per section

		# we can effectively ignore the plants, only count the seats -> wrong intuition -> since number of seats per section are fixed -> only differences are how many plants are there

		# we must be greedy with the seats we choose, the first two seats are the first section and so on

		# it seems like there are two kind of plants, the ones at intersection and the ones within the two seats of same section

		# we can count the ones at intersection -> the answer

		num_seats = corridor.count("S", 0)
		num_plants = corridor.count("P", 0)
		n = len(corridor)

		if num_seats % 2 != 0 or num_seats == 0:
			return 0

		prev_first, prev_second = -1, -1

		cur_first, cur_second = -1, -1

		cur_seat_count = 0
		intersect_plants = 1
		MOD = 10**9 + 7

		for i in range(n):
			if corridor[i] == "S":
				if cur_seat_count % 2 == 0:
					prev_first = cur_first
					cur_first = i
				else:
					prev_second = cur_second
					cur_second = i

				# check if the current intersection has any plants
				if cur_seat_count % 2 == 0:
					if prev_first != -1:
						intersect_plants = intersect_plants * (cur_first - cur_second) % MOD

				cur_seat_count += 1

		# Time Complexity: O(n)
		# Space Complexity: O(1)
		return intersect_plants
