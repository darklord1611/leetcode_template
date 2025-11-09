# LeetCode Daily Challenge (2025-11-06)\n# Title: Power Grid Maintenance\n# Difficulty: Medium\n# Acceptance Rate: 46.647230320699705\n# Tags: Array, Hash Table, Depth-First Search, Breadth-First Search, Union Find, Graph, Heap (Priority Queue), Ordered Set\n# URL: https://leetcode.com/problems/power-grid-maintenance/\n#\n# You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).
#
# These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.
#
# Initially, all stations are online (operational).
#
# You are also given a 2D array queries, where each query is one of the following two types:
#
#
#
# 	[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.
#
#
# 	[2, x]: Station x goes offline (i.e., it becomes non-operational).
#
#
#
# Return an array of integers representing the results of each query of type [1, x] in the order they appear.
#
# Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.
#
#


# Your solution starts here
from typing import List
import heapq


class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]  # 1 -> still operational
        self.is_operational = [True for i in range(n + 1)]
        self.groups = {}

    def find(self, idx):
        # find the operational station within the power grid
        if self.parents[idx] == idx:  # still active
            return idx
        else:
            self.parents[idx] = self.find(self.parents[idx])
            return self.parents[idx]

    def deactivate_station(self, idx):
        self.is_operational[idx] = False

    def build(self, n):
        for i in range(1, n + 1):
            cur_root = self.find(i)
            if cur_root not in self.groups.keys():
                self.groups[cur_root] = [i]
            else:
                heapq.heappush(self.groups[cur_root], i)

    def find_station(self, idx):
        if self.is_operational[idx]:
            return idx

        root_idx = self.find(idx)
        while len(self.groups[root_idx]) != 0:
            cur_station_id = heapq.heappop(self.groups[root_idx])
            if self.is_operational[cur_station_id]:
                heapq.heappush(self.groups[root_idx], cur_station_id)
                return cur_station_id

        return -1

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parents[max(root_x, root_y)] = self.parents[min(root_x, root_y)]

        return None


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # disjoint set union
        # each power station starts as an independent set -> then union

        dsu = DSU(c)

        n = len(connections)
        m = len(queries)
        ans = []

        for i in range(n):
            dsu.union(connections[i][0], connections[i][1])

        dsu.build(c)  # build the min-heap of each connected components

        for i in range(m):
            query_type, station_id = queries[i]
            if query_type == 2:
                dsu.deactivate_station(station_id)
            else:
                cur_station = dsu.find_station(station_id)

                ans.append(cur_station)

        return ans
