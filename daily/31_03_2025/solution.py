# LeetCode Daily Challenge (2025-03-31)
# Title: Put Marbles in Bags
# Difficulty: Hard
# URL: https://leetcode.com/problems/put-marbles-in-bags/
#
# You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.
#
# Divide the marbles into the k bags according to the following rules:
#
#
# 	No bag is empty.
# 	If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
# 	If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
#
#
# The score after distributing the marbles is the sum of the costs of all the k bags.
#
# Return the difference between the maximum and minimum scores among marble distributions.
#
#


# Your solution starts here
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # k bags -> k intervals
        # we need to distribute ALL marbles -> not mentioned explicitly but implied through examples
        # try to formulate the score -> what special? we always have first and last index in our weight sum
        # Example: 1 4 7 2 3 9 5 3, k = 3
        # split at an arbitrary index -> 1 4 7 | 2 3 9 5 3
        # what happens when we split a single index between 7 and 2 like above? -> we form a bag(subarray) and also choose the first index of the 2nd bag
        # score = weight[0] + weight[n - 1] + sum(split_point_1 + .... + split_point_k) -> finding both top k min and max -> solved

        n = len(weights)
        ans = 0

        split_point_weights = []

        for i in range(n - 1):
            split_point_weights.append(weights[i] + weights[i + 1])

        split_point_weights.sort()

        for i in range(k - 1):  # k intervals -> k - 1 split points
            ans += split_point_weights[n - 2 - i] - split_point_weights[i]

        return ans
