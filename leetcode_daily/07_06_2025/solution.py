# LeetCode Daily Challenge (2025-06-07)
# Title: Lexicographically Minimum String After Removing Stars
# Difficulty: Medium
# URL: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
#
# You are given a string s. It may contain any number of &#39;*&#39; characters. Your task is to remove all &#39;*&#39; characters.
#
# While there is a &#39;*&#39;, do the following operation:
#
#
# 	Delete the leftmost &#39;*&#39; and the smallest non-&#39;*&#39; character to its left. If there are several smallest characters, you can delete any of them.
#
#
# Return the lexicographically smallest resulting string after removing all &#39;*&#39; characters.
#
#


# Your solution starts here

import heapq


class Solution:
	def clearStars(self, s: str) -> str:
		# whenever we encounter a star * -> we must delete a character on the left, the character should be the smallest since we need lexicographically smallest result str
		# the characters after the last star are kept intact
		# we prioritize smaller characters and if they equal, pick the largest one -> save the smaller indices for later stars if possible
		n = len(s)
		heap = []
		res = ""
		used_indices = set()
		for i in range(n):
			if s[i] != "*":
				heapq.heappush(heap, (s[i], -i))
			else:
				cur_char, index = heapq.heappop(heap)
				used_indices.add(-index)

		for i in range(n):
			if i not in used_indices and s[i] != "*":
				res += s[i]

		return res
