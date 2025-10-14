# LeetCode Daily Challenge (2025-06-04)
# Title: Find the Lexicographically Largest String From the Box I
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
#
# You are given a string word, and an integer numFriends.
#
# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
#
#
# 	word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# 	All the split words are put into a box.
#
#
# Find the lexicographically largest string from the box after all the rounds are finished.
#
#


# Your solution starts here


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:  # one friend so we don't have to divide up
            return word

        # largest substring would be the one with either largest first character or largest size
        # how to achieve largest size for a substring? by break down the string into numFriends parts, with the largest part of length: len(string) - numFriends + 1

        n = len(word)
        res = ""
        for i in range(
            n
        ):  # consider all starting characters to be the first eligible choice for the required string
            right_bound = min(i + n - numFriends + 1, n)
            res = max(res, word[i:right_bound])
        return res
