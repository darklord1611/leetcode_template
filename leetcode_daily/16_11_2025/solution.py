# LeetCode Daily Challenge (2025-11-16)\n# Title: Number of Substrings With Only 1s\n# Difficulty: Medium\n# Acceptance Rate: 55.296919909695774\n# Tags: Math, String\n# URL: https://leetcode.com/problems/number-of-substrings-with-only-1s/\n#\n# Given a binary string s, return the number of substrings with all characters 1&#39;s. Since the answer may be too large, return it modulo 109 + 7.
#
#


# Your solution starts here


class Solution:
    def numSub(self, s: str) -> int:
        # record the length of each segement with continuous 1s

        MOD = 10**9 + 7
        ans = 0
        cur_len = 0
        for char in s:
            if char == "1":
                cur_len += 1
            else:
                ans += cur_len * (cur_len + 1) // 2 % MOD
                cur_len = 0

        # account for the string ends with 1s
        ans += (cur_len * (cur_len + 1) // 2) % MOD

        # Time complexity: O(n)
        # Space complexity: O(1)
        return ans
