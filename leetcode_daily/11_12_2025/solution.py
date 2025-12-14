# LeetCode Daily Challenge (2025-12-11)\n# Title: Count Covered Buildings\n# Difficulty: Medium\n# Acceptance Rate: 40.24508278889695\n# Tags: Array, Hash Table, Sorting\n# URL: https://leetcode.com/problems/count-covered-buildings/\n#\n# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
# 
# A building is covered if there is at least one building in all four directions: left, right, above, and below.
# 
# Return the number of covered buildings.
# 
#  


# Your solution starts here


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # what does it mean for a building to be covered in one direction?

        # for a single point (x1, y1), we draw the line of y = y1 and check if there points across the two sides of that line

        # all coordinates are unique and bounded

        # on top? -> exists at least one point where y2 > y1
        # on bottom? -> exists at least one point where y3 < y1
        # left -> exists at least one point where x4 < x1
        # right -> exists at least one point where x5 > x1

        # what about the boundaries? -> suppose we can find the boundaries then we have something to compare to
        # notice that we only need to have at least one building at one direction

        # the buildings must be on the same x and y-axis to count?

        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)

        for p in buildings:
            x, y = p[0], p[1]
            max_row[y] = max(max_row[y], x)
            min_row[y] = min(min_row[y], x)
            max_col[x] = max(max_col[x], y)
            min_col[x] = min(min_col[x], y)

        res = 0
        for p in buildings:
            x, y = p[0], p[1]
            if min_row[y] < x < max_row[y] and min_col[x] < y < max_col[x]:
                res += 1

        return res



