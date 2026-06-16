# LeetCode Daily Challenge (2026-06-16)\n# Title: Process String with Special Operations I\n# Difficulty: Medium\n# Acceptance Rate: 65.80111798316828\n# Tags: String, Simulation\n# URL: https://leetcode.com/problems/process-string-with-special-operations-i/\n#\n# You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.
# 
# Build a new string result by processing s according to the following rules from left to right:
# 
# 
# 	If the letter is a lowercase English letter append it to result.
# 	A &#39;*&#39; removes the last character from result, if it exists.
# 	A &#39;#&#39; duplicates the current result and appends it to itself.
# 	A &#39;%&#39; reverses the current result.
# 
# 
# Return the final string result after processing all characters in s.
# 
#  


# Your solution starts here

class Solution:
    def processStr(self, s: str) -> str:
        # stacks?
        res = ""

        # so with # or % we always gonna clear out one stack A and put them into the other stack B
        # so if there are any excess characters appear after these operations, well we have to put them into the empty stack
        for char in s:
            if char >= "a" and char <= "z":
                res += char
            elif char == "*":
                res = res[:-1]
            elif char == "#":
                res = res + res
            elif char == "%":
                res = res[::-1]
        
        return res