# LeetCode Daily Challenge (2025-05-25)
# Title: Longest Palindrome by Concatenating Two Letter Words
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
#
# You are given an array of strings words. Each element of words consists of two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
#
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
	def longestPalindrome(self, words: List[str]) -> int:
		# we can divide words into two types: one type with both character is the same aka "gg" -> type 1
		# other one is with different character aka "ab" or "ba",..... -> type 2
		# suppose we keep track of the count of each word. what type of words should we include first?
		# we only include a word if we able to create and maintain a palindrome
		# that means if we were to insert word x, we would also have to insert word x.reverse()

		# keep track of the frequency of both x and x.reverse(), we can include at most min(freq[x], freq[x.reverse()]) for a word x

		n = len(words)
		freq = defaultdict(int)
		is_centered = False
		max_len = 0

		for i in range(n):
			freq[words[i]] += 1

		for key in list(freq.keys()):  # convert keys to a new list to avoid runtime error when add key to used_words
			if freq[key] == 0 or freq[key[::-1]] == 0:
				continue

			if key == key[::-1]:  # type 1 words
				max_len += (freq[key] // 2) * 4
				if not is_centered and freq[key] % 2 == 1:  # there can only be one instance of type 1 word in the center
					max_len += 2
					is_centered = True
			else:
				max_len += min(freq[key], freq[key[::-1]]) * 4  # take the min of x and x.reverse()

			freq[key] = 0  # mark as used

		# Time Complexity: O(n)
		# Space Complexity: O(n)
		return max_len
