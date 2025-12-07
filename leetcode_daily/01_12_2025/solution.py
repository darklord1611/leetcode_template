# LeetCode Daily Challenge (2025-12-01)\n# Title: Maximum Running Time of N Computers\n# Difficulty: Hard\n# Acceptance Rate: 53.85990830639402\n# Tags: Array, Binary Search, Greedy, Sorting\n# URL: https://leetcode.com/problems/maximum-running-time-of-n-computers/\n#\n# You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.
#
# Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.
#
# Note that the batteries cannot be recharged.
#
# Return the maximum number of minutes you can run all the n computers simultaneously.
#
#


# Your solution starts here


class Solution:
	def maxRunTime(self, n: int, batteries: List[int]) -> int:
		# we always have >= n batteries for n computers

		# for n computers to run simultaneously -> we must always have n valid batteries at the time

		# the real question is how do we divide up the resource, 1 battery can only be in 1 computer at a time

		# we can use the battery up until a point and then place it back(if it's not used up yet)

		# in a natural way, we want to use the batteries with larger capacity first

		# so we maintain a max heap of n elements, whenever the smallest element is 0 -> we reached the limit

		# hold on, this type of problem seems very familiar

		# if we can run all n computers for the maximum of x minutes, then we wouldn't be able to run it for x + 1 minutes, we would be able to run it for x - 1 minutes -> monotonic nature

		# binary search? then how would we verify that we able to run it for x minutes in O(n)?

		left = 1
		right = sum(batteries) // n

		while left < right:
			mid = left + (right - left) // 2 + 1

			total = 0
			for battery in batteries:
				total += min(battery, mid)

			if total // n >= mid:
				left = mid
			else:
				right = mid - 1

		return left
