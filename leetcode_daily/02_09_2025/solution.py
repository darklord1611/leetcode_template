# LeetCode Daily Challenge (2025-09-02)
# Title: Find the Number of Ways to Place People I
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
#
# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].
#
# Count the number of pairs of points (A, B), where
#
#
# 	A is on the upper left side of B, and
# 	there are no other points in the rectangle (or line) they make (including the border).
#
#
# Return the count.
#
#


# Your solution starts here
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # point A -> (x1, y1), point B -> (x2, y2), A is on the upper left side of B -> what does that mean?
        # upper? -> y1 >= y2, left? -> x1 <= x2 -> first condition satisfied
        # so all left is to figure out how to check if there exist some points in the rectangle(or line) formed by two points
        # filter the valid pairs according to condition 1
        # then do a brute force and check for any other points beside the two examined points

        n = len(points)
        valid_pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                first_point = points[i]
                second_point = points[j]
                if (
                    second_point[0] >= first_point[0]
                    and second_point[1] <= first_point[1]
                ):
                    valid_pairs.append((first_point, second_point))

                if (
                    first_point[0] >= second_point[0]
                    and first_point[1] <= second_point[1]
                ):
                    valid_pairs.append((second_point, first_point))

        final_valid_pairs = []

        for i in range(len(valid_pairs)):
            x1, y1 = valid_pairs[i][0]  # point A
            x2, y2 = valid_pairs[i][1]  # point B
            is_valid = True
            for j in range(n):
                if points[j] == valid_pairs[i][0] or points[j] == valid_pairs[i][1]:
                    continue
                else:
                    if x1 <= points[j][0] <= x2 and y2 <= points[j][1] <= y1:
                        is_valid = False
                        break

            if is_valid:
                final_valid_pairs.append(valid_pairs[i])

        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        return len(final_valid_pairs)
