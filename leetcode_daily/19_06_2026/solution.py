# LeetCode Daily Challenge (2026-06-19)\n# Title: Find the Highest Altitude\n# Difficulty: Easy\n# Acceptance Rate: 83.92550442989496\n# Tags: Array, Prefix Sum\n# URL: https://leetcode.com/problems/find-the-highest-altitude/\n#\n# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# 
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 &lt;= i &lt; n). Return the highest altitude of a point.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0

        cur_net = gain[0]

        for i in range(1, len(gain)):
            max_alt = max(max_alt, cur_net)

            cur_net += gain[i]
        

        return max(max_alt, cur_net)
