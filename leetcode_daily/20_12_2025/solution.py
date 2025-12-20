# LeetCode Daily Challenge (2025-12-20)\n# Title: Delete Columns to Make Sorted\n# Difficulty: Easy\n# Acceptance Rate: 75.15412688921421\n# Tags: Array, String\n# URL: https://leetcode.com/problems/delete-columns-to-make-sorted/\n#\n# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a grid.
#
#
# 	For example, strs = [&quot;abc&quot;, &quot;bce&quot;, &quot;cae&quot;] can be arranged as follows:
#
#
#
# abc
# bce
# cae
#
#
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 (&#39;a&#39;, &#39;b&#39;, &#39;c&#39;) and 2 (&#39;c&#39;, &#39;e&#39;, &#39;e&#39;) are sorted, while column 1 (&#39;b&#39;, &#39;c&#39;, &#39;a&#39;) is not, so you would delete column 1.
#
# Return the number of columns that you will delete.
#
#


# Your solution starts here
from typing import List


class Solution:
	def minDeletionSize(self, strs: List[str]) -> int:
		# all of same length

		deleted_cols = 0
		num_cols = len(strs[0])
		num_rows = len(strs)
		for col in range(num_cols):
			prev_char = strs[0][col]
			is_valid = True

			for row in range(1, num_rows):
				if ord(strs[row][col]) < ord(prev_char):
					is_valid = False
					break

				prev_char = strs[row][col]

			if not is_valid:
				deleted_cols += 1

		return deleted_cols
