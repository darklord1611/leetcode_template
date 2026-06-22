# LeetCode Daily Challenge (2026-06-22)\n# Title: Maximum Number of Balloons\n# Difficulty: Easy\n# Acceptance Rate: 61.88628494667735\n# Tags: Hash Table, String, Counting\n# URL: https://leetcode.com/problems/maximum-number-of-balloons/\n#\n# Given a string text, you want to use the characters of text to form as many instances of the word &quot;balloon&quot; as possible.
# 
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
# 
#  


# Your solution starts here
from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = ["b", "a", "l", "o", "n"]

        counters = defaultdict(int)
        max_instance = len(text)
        for char in text:
            counters[char] += 1
        
        for char in chars:
            div = 1
            if char == "l" or char == "o":
                div = 2
            max_instance = min(counters[char] // div, max_instance)
        
        return max_instance
