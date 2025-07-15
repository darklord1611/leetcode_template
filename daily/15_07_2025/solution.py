# LeetCode Daily Challenge (2025-07-15)
# Title: Valid Word
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-word/
#
# A word is considered valid if:
# 
# 
# 	It contains a minimum of 3 characters.
# 	It contains only digits (0-9), and English letters (uppercase and lowercase).
# 	It includes at least one vowel.
# 	It includes at least one consonant.
# 
# 
# You are given a string word.
# 
# Return true if word is valid, otherwise, return false.
# 
# Notes:
# 
# 
# 	&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;, and their uppercases are vowels.
# 	A consonant is an English letter that is not a vowel.
# 
# 
#  


# Your solution starts here
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        consonant_count = 0

        for char in word:
            code_point = ord(char.lower())
            if 48 <= code_point <= 57:
                continue
            if 97 <= code_point <= 122:
                if char.lower() in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
            else:
                return False
        
        if vowel_count == 0:
            return False
        
        if consonant_count == 0:
            return False
        
        return True

