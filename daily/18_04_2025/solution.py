# LeetCode Daily Challenge (2025-04-18)
# Title: Count and Say
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-and-say/
#
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# 
# 
# 	countAndSay(1) = &quot;1&quot;
# 	countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# 
# 
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string &quot;3322251&quot; we replace &quot;33&quot; with &quot;23&quot;, replace &quot;222&quot; with &quot;32&quot;, replace &quot;5&quot; with &quot;15&quot; and replace &quot;1&quot; with &quot;11&quot;. Thus the compressed string becomes &quot;23321511&quot;.
# 
# Given a positive integer n, return the nth element of the count-and-say sequence.
# 
#  


# Your solution starts here

# TOP-DOWN APPROACH

class Solution:
    def countAndSay(self, n: int) -> str:
        # 1 -> 11 -> 21 -> 1211 -> 111221 -> 312211

        def dfs(cur_len : int) -> str:
            if cur_len == 1:
                return "1"
            
            res_str = dfs(cur_len - 1)
            count = 1
            cur_char = res_str[0]
            encoded_str = ""

            for i in range(1, len(res_str)):
                if res_str[i] == cur_char:
                    count += 1
                else:
                    encoded_str += f"{count}{cur_char}"
                    cur_char = res_str[i]
                    count = 1
            
            encoded_str += f"{count}{cur_char}"
            return encoded_str

        res = dfs(n)

        # Time complexity: O(2^n)
        # Space complexity: O(n)
        return res

# BOTTOM-UP APPROACH
class Solution2:
    def countAndSay(self, n: int) -> str:
        # 1 -> 11 -> 21 -> 1211 -> 111221 -> 312211
        res = "1"

        for _ in range(1, n):
            temp_str = res
            encoded_str = ""
            cur_char = temp_str[0]
            count = 1
            for i in range(1, len(temp_str)):
                if temp_str[i] == cur_char:
                    count += 1
                else:
                    encoded_str += f"{count}{cur_char}"
                    cur_char = temp_str[i]
                    count = 1
            
            encoded_str += f"{count}{cur_char}"

            res = encoded_str

        return res
        
