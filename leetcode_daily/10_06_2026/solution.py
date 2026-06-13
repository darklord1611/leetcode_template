# LeetCode Daily Challenge (2026-06-10)\n# Title: Maximum Total Subarray Value II\n# Difficulty: Hard\n# Acceptance Rate: 30.76931510453783\n# Tags: Array, Greedy, Segment Tree, Heap (Priority Queue)\n# URL: https://leetcode.com/problems/maximum-total-subarray-value-ii/\n#\n# You are given an integer array nums of length n and an integer k.
# 
# You must select exactly k distinct non-empty subarrays nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.
# 
# The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).
# 
# The total value is the sum of the values of all chosen subarrays.
# 
# Return the maximum possible total value you can achieve.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        ans_str = ""
        for word in words:
            cur_weight = 0
            for char in word:
                cur_weight += weights[ord(char) - ord("a")]
            
            ans_str += chr(ord("z") - cur_weight % 26)
        
        return ans_str
