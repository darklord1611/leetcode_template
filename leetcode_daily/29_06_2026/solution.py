# LeetCode Daily Challenge (2026-06-29)\n# Title: Number of Strings That Appear as Substrings in Word\n# Difficulty: Easy\n# Acceptance Rate: 82.98157898618055\n# Tags: Array, String\n# URL: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/\n#\n# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
# 
# A substring is a contiguous sequence of characters within a string.
# 
#  


# Your solution starts here
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        ans = 0

        for pattern in patterns:
            if pattern in word:
                ans += 1
        

        return ans
