# LeetCode Daily Challenge (2025-09-15)
# Title: Maximum Number of Words You Can Type
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
#
# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
# 
# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.
# 
#  


# Your solution starts here

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        count = 0
        words = text.split(" ")

        for word in words:
            is_valid = True
            for letter in brokenLetters:
                if letter in word:
                    is_valid = False
                    break
            
            if is_valid:
                count += 1
        
        return count