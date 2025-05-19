# LeetCode Daily Challenge (2025-04-29)
# Title: Count Subarrays Where Max Element Appears at Least K Times
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
#
# You are given an integer array nums and a positive integer k.
#
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
#
# A subarray is a contiguous sequence of elements within an array.
#
#

# Your solution starts here
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # maximum number of array, NOT current subarray
        # sliding window -> maintain the count of maximum number
        # we want to shrink the window -> at least k times not gonna work since k is not bounded
        # transform to at most k times type of problem
        # remember, total subarrays with at least k = total subarrays - total subarrays with less than k
        # problem -> count total subarrays that have less than k occurences of maximum number

        # total subarrays of an array with n elements? -> a subarrays need a start and end index, for a given starting index i, total number of ending index pairs would be n - i
        # sum(n - i) for i in range(0, n) -> n*(n + 1) // 2
        n = len(nums)
        count = 0
        left = 0
        max_num = 0
        cur_max_freq = 0

        for i in range(n):
            max_num = max(max_num, nums[i])

        for right in range(n):
            if nums[right] == max_num:
                cur_max_freq += 1

            while cur_max_freq >= k:
                if nums[left] == max_num:
                    cur_max_freq -= 1
                left += 1

            count += right - left + 1

        return n * (n + 1) // 2 - count
