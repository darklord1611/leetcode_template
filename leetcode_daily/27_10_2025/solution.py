# LeetCode Daily Challenge (2025-10-27)\n# Title: Number of Laser Beams in a Bank\n# Difficulty: Medium\n# Acceptance Rate: 85.88678881786718\n# Tags: Array, Math, String, Matrix\n# URL: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/\n#\n# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of &#39;0&#39;s and &#39;1&#39;s. &#39;0&#39; means the cell is empty, while&#39;1&#39; means the cell has a security device.
#
# There is one laser beam between any two security devices if both conditions are met:
#
#
# 	The two devices are located on two different rows: r1 and r2, where r1 &lt; r2.
# 	For each row i where r1 &lt; i &lt; r2, there are no security devices in the ith row.
#
#
# Laser beams are independent, i.e., one beam does not interfere nor join with another.
#
# Return the total number of laser beams in the bank.
#
#


# Your solution starts here
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # count the number of laser beams at each floor -> multiply

        n = len(bank)
        floors = []

        for i in range(n):
            count = 0
            for char in bank[i]:
                if char == "1":
                    count += 1

            if count != 0:
                floors.append(count)

        if len(floors) == 1:
            return 0

        num_beams = 0
        for i in range(1, len(floors)):
            num_beams += floors[i - 1] * floors[i]

        return num_beams
