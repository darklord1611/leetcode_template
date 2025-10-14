# LeetCode Daily Challenge (2025-04-20)
# Title: Rabbits in Forest
# Difficulty: Medium
# URL: https://leetcode.com/problems/rabbits-in-forest/
#
# There is a forest with an unknown number of rabbits. We asked n rabbits &quot;How many rabbits have the same color as you?&quot; and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
#
# Given the array answers, return the minimum number of rabbits that could be in the forest.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # rabbits that answer the same number ->potentially the same color as well

        n = len(answers)
        freq = defaultdict(int)
        total_rabbits = 0

        for i in range(n):
            if answers[i] == 0:
                total_rabbits += 1
                continue
            if (
                freq[answers[i]] % (answers[i] + 1) == 0
            ):  # already form a group -> add the total rabbits to the result
                total_rabbits += (
                    answers[i] + 1
                )  # plus one to account for the rabbit that answer
            freq[answers[i]] += 1

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        return total_rabbits
