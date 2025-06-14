# LeetCode Daily Challenge (2025-06-14)
# Title: Maximum Difference by Remapping a Digit
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
#
# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
# 
# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
# 
# Notes:
# 
# 
# 	When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
# 	Bob can remap a digit to itself, in which case num does not change.
# 	Bob can remap different digits for obtaining minimum and maximum values respectively.
# 	The resulting number after remapping can contain leading zeroes.
# 
# 
#  


# Your solution starts here

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # remap the rightmost digit that not equal 9, for example: 8679 -> remap 8 -> 9
        # remap the rightmost digit to 0


        digit_str = str(num)
        n = len(digit_str)
        max_digit_char_to_trans = ""
        min_digit_char_to_trans = digit_str[0]
        max_num = []
        min_num = []

        for i in range(n):
            if digit_str[i] != "9":
                max_digit_char_to_trans = digit_str[i]
                break

        for i in range(n):
            temp = digit_str[i]
            if digit_str[i] == max_digit_char_to_trans:
                temp = "9"   
            max_num.append(temp)

            temp = digit_str[i]
            if digit_str[i] == min_digit_char_to_trans:
                temp = "0"   
            min_num.append(temp)

        num1 = int("".join(max_num))
        num2 = int("".join(min_num))

        return num1 - num2



