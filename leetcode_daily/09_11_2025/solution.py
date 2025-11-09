# LeetCode Daily Challenge (2025-11-09)\n# Title: Count Operations to Obtain Zero\n# Difficulty: Easy\n# Acceptance Rate: 76.03739932558594\n# Tags: Math, Simulation\n# URL: https://leetcode.com/problems/count-operations-to-obtain-zero/\n#\n# You are given two non-negative integers num1 and num2.
#
# In one operation, if num1 &gt;= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.
#
#
# 	For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
#
#
# Return the number of operations required to make either num1 = 0 or num2 = 0.
#
#


# Your solution starts here


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # (8, 6) -> (2, 6) -> (2, 4) -> (2, 2) -> done
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1

            count += 1

        return count
