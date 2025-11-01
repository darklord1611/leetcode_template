# LeetCode Daily Challenge (2025-10-29)\n# Title: Smallest Number With All Set Bits\n# Difficulty: Easy\n# Acceptance Rate: 77.49584846181993\n# Tags: Math, Bit Manipulation\n# URL: https://leetcode.com/problems/smallest-number-with-all-set-bits/\n#\n# You are given a positive number n.
#
# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
#
#


# Your solution starts here


class Solution:
    def smallestNumber(self, n: int) -> int:
        max_exp = 11
        ans = -1

        for i in range(max_exp):
            cur = 2**i
            if cur > n:
                ans = cur - 1
                break

        return ans
