# LeetCode Daily Challenge (2025-11-13)\n# Title: Maximum Number of Operations to Move Ones to the End\n# Difficulty: Medium\n# Acceptance Rate: 64.43538112675378\n# Tags: String, Greedy, Counting\n# URL: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/\n#\n# You are given a binary string s.
#
# You can perform the following operation on the string any number of times:
#
#
# 	Choose any index i from the string where i + 1 &lt; s.length such that s[i] == &#39;1&#39; and s[i + 1] == &#39;0&#39;.
# 	Move the character s[i] to the right until it reaches the end of the string or another &#39;1&#39;. For example, for s = &quot;010010&quot;, if we choose i = 1, the resulting string will be s = &quot;000110&quot;.
#
#
# Return the maximum number of operations that you can perform.
#
#


# Your solution starts here


# This is a wrong approach since we traverse right to left -> meaning that each "1" would only need at most 1 operation to reach the desired spot, meanwhile we need to calculate the maximum number of operations possible
class WrongSolution:
    def maxOperations(self, s: str) -> int:
        # so essentially we want to move the string to the form of 00000 11111, all 0s to the left and all 1s to the right
        # 10111101 -> 00111111, 5 ops

        chars = list(s)
        n = len(s)
        idx = n - 2
        last_zero_idx = -1
        num_ops = 0

        while idx >= 0:
            # set initial position of the last zero
            if chars[idx] == "0" and last_zero_idx == -1:
                last_zero_idx = idx

            # we encounter one-index -> if there exists a valid switch
            if chars[idx] == "1":  # we replace the two positions
                if chars[idx + 1] == "0":
                    chars[last_zero_idx] = "1"
                    chars[idx] = "0"
                    last_zero_idx -= 1
                    num_ops += 1

            idx -= 1

        return num_ops


class Solution:
    def maxOperations(self, s: str) -> int:
        # so essentially we want to move the string to the form of 00000 11111, all 0s to the left and all 1s to the right
        # 1111101 -> 0111111, 5 ops

        # we traverse right to left or left to right? Why?

        one_count = 0
        num_ops = 0
        n = len(s)

        one_count += 1 if s[0] == "1" else 0

        # think of the string 11101110 -> at first valid index 10, what would we do? how does that affect the previous 1s up until that point?

        for i in range(1, n):
            if s[i] == "1":
                one_count += 1
            elif s[i - 1] == "1":
                num_ops += one_count

        # Time complexity: O(n)
        # Space complexity: O(1)

        return num_ops
