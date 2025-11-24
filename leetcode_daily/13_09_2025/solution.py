# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from collections import defaultdict


class Solution:
	def maxFreqSum(self, s: str) -> int:
		vowels = ["a", "e", "i", "o", "u"]

		freq = defaultdict(int)
		max_vowel = 0
		max_consonant = 0

		for char in s:
			freq[char] += 1
			if char in vowels:
				max_vowel = max(max_vowel, freq[char])
			else:
				max_consonant = max(max_consonant, freq[char])

		return max_vowel + max_consonant
