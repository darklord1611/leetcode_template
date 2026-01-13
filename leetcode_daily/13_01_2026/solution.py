# LeetCode Daily Challenge (2026-01-13)\n# Title: Separate Squares I\n# Difficulty: Medium\n# Acceptance Rate: 52.81273949183517\n# Tags: Array, Binary Search\n# URL: https://leetcode.com/problems/separate-squares-i/\n#\n# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
# 
# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.
# 
# Answers within 10-5 of the actual answer will be accepted.
# 
# Note: Squares may overlap. Overlapping areas should be counted multiple times.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # problem ask for the min y, notice a monotonic nature here, suppose we given a line already, we can calculate the top and bottom area
        # based on the differences, we can then adjust for a better line

        # binary search? 

        # given a horizontal line, how to calculate the top and the bottom area of ONE square? what if they don't intersect/ do intersect?

        # cautious with BS for float numbers

        n = len(squares)
        areas = [square[2] ** 2 for square in squares]
        low = 0
        high = 0
        eps = 1e-5

        for square in squares:
            high = max(high, square[1] + square[2]) # max y coordinate
        
        while abs(high - low) > eps:
            top_area = 0
            btm_area = 0
            mid = (low + high) / 2
            for i in range(n):
                x, y, length = squares[i]

                # case 1: the square on top of the line
                if y > mid:
                    top_area += areas[i]
                elif y + length < mid: # case 2: the square below the line
                    btm_area += areas[i]
                else: # intersection
                    top_area += (y + length - mid) / length * areas[i]
                    btm_area += (mid - y) / length * areas[i]
                
            if top_area > btm_area:
                low = mid
            else:
                high = mid
        
        return low
                


