# LeetCode Daily Challenge (2025-06-10)
# Title: Maximum Difference Between Even and Odd Frequency I
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
#
# You are given a string s consisting of lowercase English letters.
#
# Your task is to find the maximum difference diff = a1 - a2 between the frequency of characters a1 and a2 in the string such that:
#
#
# 	a1 has an odd frequency in the string.
# 	a2 has an even frequency in the string.
#
#
# Return this maximum difference.
#
#


# Your solution starts here

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        min_odd_freq = float("inf")
        min_even_freq = float("inf")
        max_odd_freq = -1
        max_even_freq = -1

        count = Counter(s)

        for key in count:
            if count[key] % 2 == 0:
                min_even_freq = min(min_even_freq, count[key])
                max_even_freq = max(max_even_freq, count[key])
            else:
                min_odd_freq = min(min_odd_freq, count[key])
                max_odd_freq = max(max_odd_freq, count[key])

        # Time complexity: O(n), where n is the length of the string s
        # Space complexity: O(26), for the Counter dictionary
        return max(max_odd_freq - min_even_freq, min_odd_freq - max_even_freq)
