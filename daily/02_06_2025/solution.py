# LeetCode Daily Challenge (2025-06-02)
# Title: Candy
# Difficulty: Hard
# URL: https://leetcode.com/problems/candy/
#
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# 
# You are giving candies to these children subjected to the following requirements:
# 
# 
# 	Each child must have at least one candy.
# 	Children with a higher rating get more candies than their neighbors.
# 
# 
# Return the minimum number of candies you need to have to distribute the candies to the children.
# 
#  


# Your solution starts here
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # each child get at least 1 candy
        # [1, 2, 3] -> examine each number, take into account the number before and after the current number

        n = len(ratings)
        candies = [1 for _ in range(n)]
        # forward pass to satisfy left relations between ratings
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # backward pass to satisfy the right relations, be careful that the current candy count may already larger than the next candy count
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

