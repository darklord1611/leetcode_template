# LeetCode Daily Challenge (2025-08-11)
# Title: Range Product Queries of Powers
# Difficulty: Medium
# URL: https://leetcode.com/problems/range-product-queries-of-powers/
#
# Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.
#
# You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti &lt;= j &lt;= righti.
#
# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.
#
#


# Your solution starts here
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # represent the number in binary -> ex: 1011010 -> powers array would consist of 1-value indices
        # now we have range queries -> utilize prefix arrays

        powers = []
        cur_power = 1
        temp = n
        MOD = 10**9 + 7
        ans = []

        while temp != 0:
            if temp % 2 != 0:
                powers.append(cur_power)

            cur_power = cur_power << 1
            temp = temp >> 1

        m = len(powers)

        # a query [a, b], we must multiply all powers[i] with a <= i <= b
        # [a, b] = [0, b + 1] - [0, a - 1] -> use prefix multiply

        prefix_mul = [0 for _ in range(m)]
        prefix_mul[0] = powers[0]

        for j in range(1, m):
            prefix_mul[j] = prefix_mul[j - 1] * powers[j]

        for query in queries:
            left, right = query
            if left == 0:
                ans.append(prefix_mul[right] % MOD)
            else:
                ans.append((prefix_mul[right] // prefix_mul[left - 1]) % MOD)

        # Time Complexity: O(m + q), where m is the number of powers and q is the number of queries
        # Space Complexity: O(m + q), where m is the number of powers and q is the number of queries
        return ans
