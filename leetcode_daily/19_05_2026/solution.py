# LeetCode Daily Challenge (2026-05-19)\n# Title: Minimum Common Value\n# Difficulty: Easy\n# Acceptance Rate: 58.66593160393975\n# Tags: Array, Hash Table, Two Pointers, Binary Search\n# URL: https://leetcode.com/problems/minimum-common-value/\n#\n# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# 
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
# 
#  


# Your solution starts here
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(len1):
            freq1[nums1[i]] += 1
        
        for i in range(len2):
            freq2[nums2[i]] += 1

        
        for i in range(len1):
            if freq2[nums1[i]] > 0:
                return nums1[i]
        
        # Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 respectively.
        # Space Complexity: O(n + m) due to the frequency dictionaries.
        return -1
        
