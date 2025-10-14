# LeetCode Daily Challenge (2025-04-13)
# Title: Count Good Numbers
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-good-numbers/
#
# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
#
#
# 	For example, &quot;2582&quot; is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, &quot;3245&quot; is not good because 3 is at an even index but is not even.
#
#
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
#
# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
#
#


# Your solution starts here
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        if n % 2 == 0:
            even_count = n // 2
            odd_count = n // 2
        else:
            even_count = n // 2 + 1
            odd_count = n // 2

        def fast_expo(base: int, exp: int, mod: int) -> int:
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = res * base % mod
                base = base * base % mod
                exp = exp // 2

            return res

        return fast_expo(5, even_count, mod) * fast_expo(4, odd_count, mod) % mod
