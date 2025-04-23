# LeetCode Daily Challenge (2025-04-23)
# Title: Count Largest Group
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-largest-group/
#
# You are given an integer n.
# 
# Each number from 1 to n is grouped according to the sum of its digits.
# 
# Return the number of groups that have the largest size.
# 
#  


# Your solution starts here
from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_sums = defaultdict(int)

        for i in range(1, n + 1):
            temp = i
            cur_sum = 0
            while temp != 0:
                cur_sum += temp % 10
                temp = temp // 10
            
            group_sums[cur_sum] += 1
        
        max_group_size = 0
        max_group_count = 0

        for key in group_sums:
            if max_group_size < group_sums[key]:
                max_group_size = group_sums[key]
                max_group_count = 1
            elif max_group_size == group_sums[key]:
                max_group_count += 1
        
        return max_group_count
            

