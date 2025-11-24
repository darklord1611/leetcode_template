# LeetCode Daily Challenge (2025-09-14)
# Title: Vowel Spellchecker
# Difficulty: Medium
# URL: https://leetcode.com/problems/vowel-spellchecker/
#
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
#
# For a given query word, the spell checker handles two categories of spelling mistakes:
#
#
# 	Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
#
#
# 		Example: wordlist = [&quot;yellow&quot;], query = &quot;YellOw&quot;: correct = &quot;yellow&quot;
# 		Example: wordlist = [&quot;Yellow&quot;], query = &quot;yellow&quot;: correct = &quot;Yellow&quot;
# 		Example: wordlist = [&quot;yellow&quot;], query = &quot;yellow&quot;: correct = &quot;yellow&quot;
#
#
# 	Vowel Errors: If after replacing the vowels (&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;) of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
#
# 		Example: wordlist = [&quot;YellOw&quot;], query = &quot;yollow&quot;: correct = &quot;YellOw&quot;
# 		Example: wordlist = [&quot;YellOw&quot;], query = &quot;yeellow&quot;: correct = &quot;&quot; (no match)
# 		Example: wordlist = [&quot;YellOw&quot;], query = &quot;yllw&quot;: correct = &quot;&quot; (no match)
#
#
#
#
# In addition, the spell checker operates under the following precedence rules:
#
#
# 	When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# 	When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# 	When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# 	If the query has no matches in the wordlist, you should return the empty string.
#
#
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
#
#


# Your solution starts here

from typing import List


class Solution:
	def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
		# two kind of errors, capitalization -> YeLLow instead of yellow
		# vowel errors -> Yallow instead of yellow

		# so we loop through the word list for each query, check against two types of errors and return if possible

		# create 3 hashmaps to store 3 version of the same strings

		# priority-based -> 0 -> exact match, 1 -> capitalization error, 2 -> vowel error, 3 -> none match

		def remove_vowel(word):
			return "".join("*" if c in "aeiou" else c for c in word)

		exact_words = set(wordlist)
		words_cap = {}
		words_vow = {}
		ans = []

		for word in wordlist:
			word_low = word.lower()
			word_low_devowel = remove_vowel(word_low)

			if word_low not in words_cap.keys():
				words_cap[word_low] = word

			if word_low_devowel not in words_vow.keys():
				words_vow[word_low_devowel] = word

		for query in queries:
			if query in exact_words:
				ans.append(query)
				continue

			query_low = query.lower()
			if query_low in words_cap:
				ans.append(words_cap[query_low])
				continue

			query_low_devowel = remove_vowel(query_low)
			if query_low_devowel in words_vow:
				ans.append(words_vow[query_low_devowel])
				continue

			ans.append("")

		return ans
