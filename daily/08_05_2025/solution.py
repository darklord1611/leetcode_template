# LeetCode Daily Challenge (2025-05-08)
# Title: Find Minimum Time to Reach Last Room II
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
#
# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
#
# Return the minimum time to reach the room (n - 1, m - 1).
#
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.
#
#


# Your solution starts here

from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # SFT problem, non-negative weights -> Dijkstra
        # Single-Source Single-Target Shortest Path
        n = len(moveTime)
        m = len(moveTime[0])

        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = [(0, 0, 0, 1)]
        visited = set((0, 0))
        min_time = 0

        while len(queue) != 0:
            time, x, y, adjacent_move_time = heapq.heappop(queue)
            min_time = max(time, min_time)

            if x == n - 1 and y == m - 1:
                break

            # check adjacent future cells
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in visited:
                    continue

                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                    continue
                # minimum time to reach the cell, either the time we can start moving to current cell OR the maximum start time of other cells we have already traversed, which ever is greater
                min_time_reach_current_cell = (
                    max(min_time, moveTime[new_x][new_y]) + adjacent_move_time
                )
                heapq.heappush(
                    queue,
                    (min_time_reach_current_cell, new_x, new_y, 3 - adjacent_move_time),
                )
                visited.add((new_x, new_y))

        return min_time
