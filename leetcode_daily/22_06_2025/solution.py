# LeetCode Daily Challenge (2025-06-22)
# Title: Divide a String Into Groups of Size k
# Difficulty: Easy
# URL: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
#
# A string s can be partitioned into groups of size k using the following procedure:
#
#
# 	The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group.
# 	For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
#
#
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.
#
# Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.
#
#


# Your solution starts here
from typing import List


class Solution:
	def divideString(self, s: str, k: int, fill: str) -> List[str]:
		res = []
		n = len(s)
		cur = n

		while cur % k != 0:
			cur += 1
			s = s + fill

		n = cur
		cur = 0

		while cur < n:
			res.append(s[cur : cur + k])
			cur += k

		return res
