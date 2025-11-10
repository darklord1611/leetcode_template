# LeetCode Daily Challenge (2025-11-10)\n# Title: Minimum Operations to Convert All Elements to Zero\n# Difficulty: Medium\n# Acceptance Rate: 47.05014462930248\n# Tags: Array, Hash Table, Stack, Greedy, Monotonic Stack\n# URL: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/\n#\n# You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.
#
# In one operation, you can select a subarray [i, j] (where 0 &lt;= i &lt;= j &lt; n) and set all occurrences of the minimum non-negative integer in that subarray to 0.
#
# Return the minimum number of operations required to make all elements in the array 0.
#
#


# Your solution starts here
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # so obviously we want to transform the most frequent non-zero elements first
        # notice that if there is 0 in the subarray -> then we can't do the transform -> why?

        # if we able to do the transformation to the non-zero elements -> then we should find the largest subarray to do all of them at once -> less operations

        # think about what happened to other non-zero elements after we transformed the first one? How does 0s affects them?

        # example: 3 4 2 1 2 1 4 1

        # think of counting the number of segments of the same non-zero elements instead (monotonic stack)
        # 1 1 1 -> is a valid segment where we could apply 1 ops
        # 1 0 1 -> this is invalid and we have to break down into two smaller segments -> 2 ops

        stack = []
        res = 0
        for num in nums:
            while (
                len(stack) > 0 and stack[-1] > num
            ):  # we encountered a smaller number -> the current segment would end right here -> pop very single bigger elements, example: stack = [3, 4], num = 2
                stack.pop()

            if num == 0:
                continue

            if (
                not stack or stack[-1] < num
            ):  # num is bigger -> current segment could still extends and collect more elements, example: stack = [3], num = 4
                res += 1
                stack.append(num)

        # Time complexity: O(n)
        # Space complexity: O(n)

        return res
