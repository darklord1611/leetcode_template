# LeetCode Daily Challenge (2025-04-24)
# Title: Count Complete Subarrays in an Array
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
#
# You are given an array nums consisting of positive integers.
#
# We call a subarray of an array complete if the following condition is satisfied:
#
#
# 	The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
#
#
# Return the number of complete subarrays.
#
# A subarray is a contiguous non-empty part of an array.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # count the distinct numbers in the entire array
        # sliding window -> notice that if the current window is satisfied then if we keep expanding, we would always have a satisfied subarray
        # Example: [1, 2, 3, 3, 2, 2, 1]
        # Suppose current window is [1, 2, 3] -> this subarray already satisfied, expanding to [1, 2, 3, 3] -> we only increase the count
        # When the array is satisfied -> move the left boundary till we no longer have valid subrray

        n = len(nums)
        distinct_num_count = len(set(nums))
        cur_distinct_count = 0
        freq = defaultdict(int)
        left = 0
        res = 0

        for right in range(n):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                cur_distinct_count += 1

            while cur_distinct_count >= distinct_num_count:
                res += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    cur_distinct_count -= 1
                left += 1

        return res
