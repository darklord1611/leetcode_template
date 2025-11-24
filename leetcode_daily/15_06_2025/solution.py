# LeetCode Daily Challenge (2025-06-15)
# Title: Max Difference You Can Get From Changing an Integer
# Difficulty: Medium
# URL: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
#
# You are given an integer num. You will apply the following steps to num two separate times:
#
#
# 	Pick a digit x (0 &lt;= x &lt;= 9).
# 	Pick another digit y (0 &lt;= y &lt;= 9). Note y can be equal to x.
# 	Replace all the occurrences of x in the decimal representation of num by y.
#
#
# Let a and b be the two results from applying the operation to num independently.
#
# Return the max difference between a and b.
#
# Note that neither a nor b may have any leading zeros, and must not be 0.
#
#


# Your solution starts here


class Solution:
	def maxDiff(self, num: int) -> int:
		# just pick the rightmost integer that not 9 -> transform to a 9 -> get the maximum number
		# just pick the rightmost integer that not 1 -> transform to a 1 -> get the minimum number

		digit_str = str(num)
		n = len(digit_str)
		max_digit_char_to_trans = ""
		min_digit_char_to_trans = ""
		max_num = []
		min_num = []

		# edge cases when the first digit is equal to 1
		nums_to_exclude = ["0", "1"] if digit_str[0] == "1" else ["0"]

		for i in range(n):
			if max_digit_char_to_trans != "" and min_digit_char_to_trans != "":
				break

			# find the rightmost digit that not equal to 9 for max transform
			if digit_str[i] != "9" and max_digit_char_to_trans == "":
				max_digit_char_to_trans = digit_str[i]

			# find the rightmost digit that not equal to 1 for min transform
			if digit_str[i] not in nums_to_exclude and min_digit_char_to_trans == "":
				min_digit_char_to_trans = digit_str[i]

		min_digit = "1" if (min_digit_char_to_trans == digit_str[0]) else "0"

		for i in range(n):
			temp = digit_str[i]
			if digit_str[i] == max_digit_char_to_trans:
				temp = "9"
			max_num.append(temp)

			temp = digit_str[i]
			if digit_str[i] == min_digit_char_to_trans:
				temp = min_digit
			min_num.append(temp)

		num1 = int("".join(max_num))
		num2 = int("".join(min_num))

		return num1 - num2
