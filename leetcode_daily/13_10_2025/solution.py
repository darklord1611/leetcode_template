# LeetCode Daily Challenge (2025-10-13)
# Title: Find Resultant Array After Removing Anagrams
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
#
# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
#
# In one operation, select any index i such that 0 &lt; i &lt; words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
#
# Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, &quot;dacb&quot; is an anagram of &quot;abdc&quot;.
#
#


# Your solution starts here
from typing import List


class Solution:
	def removeAnagrams(self, words: List[str]) -> List[str]:
		# anagrams when sorted would result in the same string
		# loop through

		n = len(words)
		mask = [1 for _ in range(n)]
		prev_idx = 0

		for i in range(1, n):
			if "".join(sorted(words[i])) == "".join(sorted(words[prev_idx])):
				mask[i] = 0
			else:
				prev_idx = i

		return [words[i] for i in range(n) if mask[i] == 1]
