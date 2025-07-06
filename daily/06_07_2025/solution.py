# LeetCode Daily Challenge (2025-07-06)
# Title: Finding Pairs With a Certain Sum
# Difficulty: Medium
# URL: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
#
# You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:
# 
# 
# 	Add a positive integer to an element of a given index in the array nums2.
# 	Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 &lt;= i &lt; nums1.length and 0 &lt;= j &lt; nums2.length).
# 
# 
# Implement the FindSumPairs class:
# 
# 
# 	FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
# 	void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
# 	int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
# 
# 
#  


# Your solution starts here
from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # initialize two arrays
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(self.nums2)
        # tot = num1 + num2 -> num2 = tot - num1
        # so we keep track of the frequency of nums2, then for each num1 in nums1 we check the key tot - num1 and return


    def add(self, index: int, val: int) -> None:
        # increase the value of an index of array2
        # also we need to update the freq array to reflect the change
        self.freq[self.nums2[index]] -= 1

        self.nums2[index] += val

        self.freq[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        total_count = 0
        for num in self.nums1:
            total_count += self.freq[tot - num]
        
        return total_count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
