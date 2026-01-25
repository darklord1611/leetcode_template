# LeetCode Daily Challenge (2026-01-25)\n# Title: Minimum Difference Between Highest and Lowest of K Scores\n# Difficulty: Easy\n# Acceptance Rate: 60.09116963419313\n# Tags: Array, Sliding Window, Sorting\n# URL: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/\n#\n# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# 
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# 
# Return the minimum possible difference.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        # maintain a sliding window of size k after we sort
        n = len(nums)

        nums.sort()

        min_diff = 10 ** 5 + 1

        left = 0
        for right in range(n):
            cur_min = nums[right] - nums[left]
            if right - left + 1 == k:
                min_diff = min(min_diff, cur_min)
                if min_diff == 0:
                    return 0
                left += 1
        
        # Time Complexity: O(n log n)
        # Space Complexity: O(logn)
        return min_diff

