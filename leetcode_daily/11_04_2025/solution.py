# LeetCode Daily Challenge (2025-04-11)
# Title:   Count Symmetric Integers
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-symmetric-integers/
#
# You are given two positive integers low and high.
#
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
#
# Return the number of symmetric integers in the range [low, high].
#
#


# Your solution starts here
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # numbers between [low, high] = numbers between [0, high] - numbers between [0, low - 1]

        def count(num: int):
            res = 0
            for i in range(1, num + 1):
                num_digits = 0
                temp = i
                prefix_sum = []
                while temp != 0:
                    num_digits += 1
                    if len(prefix_sum) == 0:
                        prefix_sum.append(temp % 10)
                    else:
                        prefix_sum.append(prefix_sum[len(prefix_sum) - 1] + temp % 10)
                    temp = temp // 10
                if (
                    num_digits % 2 != 0
                    or 2 * prefix_sum[(num_digits - 1) // 2]
                    != prefix_sum[num_digits - 1]
                ):
                    continue
                else:
                    res += 1

            return res

        return count(high) - count(low - 1)
