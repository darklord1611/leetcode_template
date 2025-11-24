# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here

from collections import Counter


class Solution:
	def reorderedPowerOf2(self, n: int) -> bool:
		# power of 2 -> binary representation would only have one index with value 1 -> ex: 1000, 100, 001

		# create a hashmap of each possible power of two, ranging from 2^0 to 2^32
		# for each power of two, we create a freq count of the number in decimal
		# then check the original freq count vs count of each power of two -> return if match

		# we can also convert to string and sort -> better approach

		num_freq = Counter(str(n))

		freq = {}

		for i in range(31):
			freq[i] = Counter(str(2**i))

			is_valid = True

			if set(freq[i].keys()) == set(num_freq.keys()):
				for key in freq[i]:
					if freq[i][key] != num_freq[key]:
						is_valid = False
						break
			else:
				is_valid = False

			if is_valid:
				return True

		return False
