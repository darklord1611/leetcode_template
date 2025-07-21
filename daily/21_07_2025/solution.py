# LeetCode Daily Challenge (2025-07-21)
# Title: Delete Characters to Make Fancy String
# Difficulty: Easy
# URL: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
#
# A fancy string is a string where no three consecutive characters are equal.
# 
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# 
# Return the final string after the deletion. It can be shown that the answer will always be unique.
# 
#  


# Your solution starts here

class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        cur_char = s[0]
        count = 1
        res = [cur_char]

        for i in range(1, n):
            if s[i] == cur_char:
                count += 1
            else:
                cur_char = s[i]
                count = 1
            
            if count >= 3:
                continue

            res.append(s[i])
        
        return "".join(res)

