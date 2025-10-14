# LeetCode Daily Challenge (2025-04-14)
# Title: Count Good Triplets
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-good-triplets/
#
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
#
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#
#
# 	0 &lt;= i &lt; j &lt; k &lt; arr.length
# 	|arr[i] - arr[j]| &lt;= a
# 	|arr[j] - arr[k]| &lt;= b
# 	|arr[i] - arr[k]| &lt;= c
#
#
# Where |x| denotes the absolute value of x.
#
# Return the number of good triplets.
#
#


# Your solution starts here
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # -a <= a[i] - a[j] <= a
        # -b <= a[j] - a[k] <= b
        # -c <= a[i] - a[k] <= c

        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] - arr[j] < -a or arr[i] - arr[j] > a:
                    continue
                for k in range(j + 1, n):
                    if arr[j] - arr[k] < -b or arr[j] - arr[k] > b:
                        continue

                    if arr[i] - arr[k] < -c or arr[i] - arr[k] > c:
                        continue

                    count += 1

        return count
