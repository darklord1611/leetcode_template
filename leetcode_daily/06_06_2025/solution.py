# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
class Solution:
	def robotWithString(self, s: str) -> str:
		# the string t is essentially a stack
		# notice that we could be greedy, just push all characters a into the result string first, ensuring smallest criterion
		# do the same with b, c, .....
		# so essentially we wants to push the current character into the result if it is the smallest, compare to other future characters
		# at each character we need to know whether the top element of the stack is the smallest?
		# if yes then just push to result, else keep add elements to the stack
		# min_suffix[i] represents the minimum character in range(i + 1, n - 1)
		n = len(s)
		min_suffix = [s[i] for i in range(n)]
		min_suffix[n - 1] = chr(ord("z") + 1)  # ensure that the last character is already minimum
		stack = []
		res = ""

		for i in range(n - 2, -1, -1):
			min_suffix[i] = min(s[i + 1], min_suffix[i + 1])

		for i in range(n):
			stack.append(s[i])

			while len(stack) != 0 and stack[-1] <= min_suffix[i]:
				res += stack.pop()

		return res
