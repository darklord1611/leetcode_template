# LeetCode Daily Challenge (2025-11-18)\n# Title: 1-bit and 2-bit Characters\n# Difficulty: Easy\n# Acceptance Rate: 46.18478025832108\n# Tags: Array\n# URL: https://leetcode.com/problems/1-bit-and-2-bit-characters/\n#\n# We have two special characters:
#
#
# 	The first character can be represented by one bit 0.
# 	The second character can be represented by two bits (10 or 11).
#
#
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
#
#


# Your solution starts here

from typing import List


class Solution:
	def isOneBitCharacter(self, bits: List[int]) -> bool:
		# 10101011010001110

		# when do we have valid one-bit character at the end -> when we already process m two-bit characters and n one-bit characters before that
		# meaning that if we are able to combine the last and the second-to-last character to be two-bit character, we would have ended up at index k - 1

		n = len(bits)
		idx = 0

		while idx < n:
			if bits[idx] == 0:
				if idx == n - 1:
					return True
				idx += 1
			else:
				idx += 2

		return False
