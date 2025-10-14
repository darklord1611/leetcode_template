# LeetCode Daily Challenge (2025-05-27)
# Title: Divisible and Non-divisible Sums Difference
# Difficulty: Easy
# URL: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
#
# You are given positive integers n and m.
#
# Define two integers as follows:
#
#
# 	num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# 	num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
#
#
# Return the integer num1 - num2.
#
#


# Your solution starts here


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # num1 + num2 = n * (n + 1) // 2

        div_sum = 0
        for i in range(1, n + 1):
            if i % m == 0:
                div_sum += i

        return n * (n + 1) // 2 - 2 * div_sum
