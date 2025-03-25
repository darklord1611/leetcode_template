# LeetCode Daily Challenge (2025-03-25)
# Title: Check if Grid can be Cut into Sections
# Difficulty: Medium
# URL: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
#
# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:
# 
# 
# 	(startx, starty): The bottom-left corner of the rectangle.
# 	(endx, endy): The top-right corner of the rectangle.
# 
# 
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:
# 
# 
# 	Each of the three resulting sections formed by the cuts contains at least one rectangle.
# 	Every rectangle belongs to exactly one section.
# 
# 
# Return true if such cuts can be made; otherwise, return false.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # we can either slice horizontally or vertically -> try both
        # Example 1
        # x-axis: [1, 5], [0, 2], [3, 5], [0, 4]
        # y-axis: [0, 2], [2, 4], [2, 3], [4, 5]
        # if slicing is possible then we would find a way to combine these above intervals into 3 separate intervals
        # y-axis -> [0, 2], [2, 4], [4, 5] -> 3 -> valid
        # x-axis -> [0, 4], [1, 5] -> 2 -> invalid

        # Example 2
        # x-axis: [0, 1], [2, 3], [0, 2], [3, 4] -> [0, 2], [2, 3], [3, 4] -> valid
        # y-axis: [0, 1], [0, 4], [2, 3], [0, 3] -> [0, 4] -> invalid

        x_intervals = []
        y_intervals = []

        m = len(rectangles)

        for rec in rectangles:
            x_intervals.append([rec[0], rec[2]])
            y_intervals.append([rec[1], rec[3]])
        
        slicing_vertical_possible = self.check_interval(x_intervals)
        slicing_horizontal_possible = self.check_interval(y_intervals)

        if slicing_vertical_possible or slicing_horizontal_possible:
            return True
        
        return False

    def check_interval(self, intervals: List[List[int]]) -> bool:

        n = len(intervals)
        res = []
        intervals.sort()

        min_overlap_num = intervals[0][0]
        max_overlap_num = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] < max_overlap_num: # why there no equal sign? because we want to maintain the intervals that share the same end and start coordinate
                max_overlap_num = max(max_overlap_num, intervals[i][1]) 
            else:
                res.append([min_overlap_num, max_overlap_num])
                min_overlap_num = intervals[i][0]
                max_overlap_num = intervals[i][1]

        res.append([min_overlap_num, max_overlap_num])


        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        
        # why does it still satisfy if we have more than 3 intervals after merged? draw them out
        return True if len(res) >= 3 else False

