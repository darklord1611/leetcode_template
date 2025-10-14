# LeetCode Daily Challenge (2025-05-24)
# Title: Find Words Containing Character
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-words-containing-character/
#
# You are given a 0-indexed array of strings words and a character x.
#
# Return an array of indices representing the words that contain the character x.
#
# Note that the returned array may be in any order.
#
#


# Your solution starts here
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        n = len(words)

        for i in range(n):
            if x in words[i]:
                ans.append(i)

        return ans
