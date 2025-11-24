# LeetCode Daily Challenge (2025-05-13)
# Title: Total Characters in String After Transformations I
# Difficulty: Medium
# URL: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
#
# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:
#
#
# 	If the character is &#39;z&#39;, replace it with the string &quot;ab&quot;.
# 	Otherwise, replace it with the next character in the alphabet. For example, &#39;a&#39; is replaced with &#39;b&#39;, &#39;b&#39; is replaced with &#39;c&#39;, and so on.
#
#
# Return the length of the resulting string after exactly t transformations.
#
# Since the answer may be very large, return it modulo 109 + 7.
#
#


# Your solution starts here


class Solution:
	def lengthAfterTransformations(self, s: str, t: int) -> int:
		# just simulate the whole process, think about recursive formula, how can we update the frequencies of each index?
		# are there any special characters that would require special counting?

		# for any characters, the count after a transformation would be the count of the previous character, count(d) after transform = count(c) before transform
		# what about b? a? z?

		mod = 10**9 + 7

		count = [0] * 26

		for ch in s:
			count[ord(ch) - ord("a")] += 1

		for _ in range(t):
			next_count = [0] * 26

			next_count[0] = count[25]
			next_count[1] = (count[25] + count[0]) % mod

			for i in range(2, 26):
				next_count[i] = count[i - 1]

			count = next_count

		ans = sum(count) % mod

		return ans
