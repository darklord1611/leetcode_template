# LeetCode Daily Challenge (2025-10-10)
# Title: Taking Maximum Energy From the Mystic Dungeon
# Difficulty: Medium
# URL: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/
#
# In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.
#
# You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.
#
# In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians&#39; sequence, absorbing all the energy during the journey.
#
# You are given an array energy and an integer k. Return the maximum possible energy you can gain.
#
# Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.
#
#


# Your solution starts here
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        suffix_sum = [-1 for _ in range(n)]
        max_energy = -float("inf")
        # k last elements initilized to be the same values in energy

        for i in range(n - 1, n - 1 - k, -1):
            suffix_sum[i] = energy[i]

        for i in range(n - 1 - k, -1, -1):
            suffix_sum[i] = suffix_sum[i + k] + energy[i]

        for i in range(n):
            max_energy = max(max_energy, suffix_sum[i])

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        return max_energy
