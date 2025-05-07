# LeetCode Daily Challenge (2025-05-07)
# Title: Find Minimum Time to Reach Last Room I
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
#
# There is a dungeon with n x m rooms arranged as a grid.
# 
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
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
        
        # Shortest-path algo -> Dijkstra, Bellman-Ford, etc....

        n = len(moveTime)
        m = len(moveTime[0])
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = [(0, 0, 0)] # x, y, time to reach this coordinate
        visited = set((0, 0))
        min_time = 0

        while len(queue) != 0:
            x, y, time = heapq.heappop(queue)
            min_time = max(min_time, time) # update the current minimum time to reach the current cell

            if x == n - 1 and y == m - 1:
                break
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if (new_x, new_y) in visited:
                    continue
                
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                    continue
                
                max_dist = max(min_time, moveTime[new_x][new_y]) + 1 # calculate the minimum time to reach adjacent cells
                heapq.heappush(queue, (new_x, new_y, max_dist))
                visited.add((new_x, new_y))
            
        return min_time
