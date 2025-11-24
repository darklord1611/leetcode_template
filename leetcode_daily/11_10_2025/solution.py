# LeetCode Daily Challenge (2025-10-11)
# Title: Maximum Total Damage With Spell Casting
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
#
# A magician has various spells.
#
# You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
#
# It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
#
# Each spell can be cast only once.
#
# Return the maximum possible total damage that a magician can cast.
#
#


# Your solution starts here
from collections import Counter
from typing import List


class Solution:
	def maximumTotalDamage(self, power: List[int]) -> int:
		count = Counter(power)
		vec = [(-(10**9), 0)]  # default element to smooth transition

		for k in sorted(count.keys()):  # we sort the count to simplify the range condition
			vec.append((k, count[k]))
		n = len(vec)
		f = [0] * n
		mx = 0
		j = 1
		for i in range(1, n):
			while j < i and vec[j][0] < vec[i][0] - 2:  # keep advancing j until we found the best previous values just before the current index i
				mx = max(mx, f[j])
				j += 1
			f[i] = mx + vec[i][0] * vec[i][1]

		# Time Complexity: O(n log n) due to sorting the unique elements
		# Space Complexity: O(n)
		return max(f)
