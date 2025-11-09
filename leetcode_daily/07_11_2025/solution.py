# LeetCode Daily Challenge (2025-11-07)\n# Title: Maximize the Minimum Powered City\n# Difficulty: Hard\n# Acceptance Rate: 53.923154701718914\n# Tags: Array, Binary Search, Greedy, Queue, Sliding Window, Prefix Sum\n# URL: https://leetcode.com/problems/maximize-the-minimum-powered-city/\n#\n# You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.
#
# Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| &lt;= r and 0 &lt;= i, j &lt;= n - 1.
#
#
# 	Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
#
#
# The power of a city is the total number of power stations it is being provided power from.
#
# The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.
#
# Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.
#
# Note that you can build the k power stations in multiple cities.
#
#


# Your solution starts here
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # so first lets find out the maximum power station of each cities first

        # to do that we can use difference arrays

        n = len(stations)
        diff = [0 for i in range(n + 1)]

        for i in range(n):
            left_bound = max(0, i - r)
            right_bound = min(i + r + 1, n)
            diff[left_bound] += stations[i]
            diff[right_bound] -= stations[i]

        # we got the initial powers, now think of the question
        # we need to maximize the possible minimum powers(which is the min power that every cities would have if we build additional k station effectively, suppose this number is x

        # suppose the answer is x -> then we could also build minimum power of any smaller values -> the condition is monotonic if x is satisfied -> then all smaller values of range [min(initial_powers), x] also satisfied, all larger values would not satisfy

        # checking condition
        def check(x):
            powers = diff.copy()
            total = 0
            remaining = k

            for i in range(n):
                total += powers[i]
                if total < x:
                    add = x - total
                    if remaining < add:
                        return False

                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    powers[end] -= add
                    total += add
            return True

        # binary search
        low = min(stations)
        high = sum(stations) + k

        res = 0

        while low <= high:
            mid = (low + high) // 2

            valid = check(mid)
            if valid:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res
