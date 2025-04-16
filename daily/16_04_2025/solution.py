# LeetCode Daily Challenge (2025-04-16)
# Title: Count the Number of Good Subarrays
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-the-number-of-good-subarrays/
#
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# 
# A subarray arr is good if there are at least k pairs of indices (i, j) such that i &lt; j and arr[i] == arr[j].
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
#  


# Your solution starts here
from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # subarrays -> sliding windows
        # n identical elements -> how many pairs -> nC2
        # adding an element will create k more pairs with k -> current count of element
        # two pointers, moving the right ptr until we have a valid subarray, then adding any numbers will eventually create more valid arrays

        freq = defaultdict(int)
        n = len(nums)

        num_pairs = 0
        ans = 0
        
        left = 0

        for right in range(n):

            num_pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while num_pairs >= k:
                ans += n - right

                freq[nums[left]] -= 1
                num_pairs -= freq[nums[left]]
                left += 1
        
        return ans
