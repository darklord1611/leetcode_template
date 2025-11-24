# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here


class Solution:
	def numberOfSubstrings(self, s: str) -> int:
		# consider each index as the ending, calculate number of valid substrings that end at that particular index
		# keep track of the latest index of each character
		# number of valid substrings would be number of total substrings - number of invalid substrings(both ending at that index)
		n = len(s)
		ans = 0
		last_indices = {"a": -1, "b": -1, "c": -1}

		for i in range(n):
			last_indices[s[i]] = i
			min_index = min(last_indices.values())
			if min_index == -1:
				continue
			else:
				ans += min_index + 1

		# Time Complexity: O(n)
		# Space Complexity: O(1)

		return ans
