# LeetCode Daily Challenge (2026-01-21)\n# Title: Construct the Minimum Bitwise Array II\n# Difficulty: Medium\n# Acceptance Rate: 52.509709585948315\n# Tags: Array, Bit Manipulation\n# URL: https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/\n#\n# You are given an array nums consisting of n prime integers.
# 
# You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
# 
# Additionally, you must minimize each value of ans[i] in the resulting array.
# 
# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # think about the binary representations of x and x + 1, how are they different?

        # notice that x + 1 will shift the left-most 0 bit to 1, suppose we call this position i
        # then every single bit 1 in the left-most to i would be flipped to 0

        # think about the properties of x | (x + 1), think about the left and right side of the first zero bit

        n = len(nums)
        res = []

        for num in nums:
            if num != 2:
                res.append(num - ((num + 1) & (-num - 1)) // 2)
            else:
                res.append(-1)
    
        return res
