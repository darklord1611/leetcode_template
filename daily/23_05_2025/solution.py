# LeetCode Daily Challenge (2025-05-23)
# Title: Find the Maximum Sum of Node Values
# Difficulty: Hard
# URL: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
#
# There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.
# 
# Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:
# 
# 
# 	Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
# 
# 	
# 		nums[u] = nums[u] XOR k
# 		nums[v] = nums[v] XOR k
# 	
# 	
# 
# 
# Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
# 
#  


# Your solution starts here
from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # we got a bunch of edges, each time we can choose an edge, update the values to be nums[i] xor k
        # we want maximum of values of each node -> each node must be the maximum value that we can obtain
        # for a particular node, how many operations can we do? <= number of edges involving that node
        # [0, 1], [0, 2] -> node 0 can be transform at most 2 times
        # The transformation only includes the current number and k, -> if we perform 2 * n transformation, we would get back the original number
        
        # think about how XOR affects two arbitrary nodes, since all nodes are connected, are there any side-effect to other nodes in the progress?
        # we can XOR two arbitrary nodes and all the in-between nodes stay the same -> greedy approach, pick the pairs with largest value change to the sum

        n = len(nums)

        net_change = [(nums[i] ^ k) - nums[i] for i in range(n)]
        net_change.sort(reverse=True) # sort according the largest change
        max_sum = sum(nums) # base sum


        for i in range(0, n, 2):
            
            if i + 1 == n:
                break
            
            cur_sum = net_change[i] + net_change[i + 1]
            if cur_sum > 0:
                max_sum += cur_sum
        
        # Time Complexity: O(n * log(n))
        # Space Complexity: O(n)
        return max_sum
