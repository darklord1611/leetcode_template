# LeetCode Daily Challenge (2025-05-26)
# Title: Largest Color Value in a Directed Graph
# Difficulty: Hard
# URL: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
#
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
#
# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
#
# A valid path in the graph is a sequence of nodes x1 -&gt; x2 -&gt; x3 -&gt; ... -&gt; xk such that there is a directed edge from xi to xi+1 for every 1 &lt;= i &lt; k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
#
# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
#
#


# Your solution starts here
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # if there is a cycle -> invalid
        # build the adjacency list first

        # dfs? start at each node, we gradually build up the path and check if it is valid(not a cycle) at the same time
        # suppose we start at node 0, how many possible choices for the color? -> 26
        # so we consider all possible colors for the largest value for each node
        # for a node, there are 3 states -> UNVISITED, VISITING, VISITED -> 0, 1, 2 respectively

        # DP, dp[u][c] = the maximum count of vertices with color c of any path starting from vertex u

        n = len(colors)
        INF = float("inf")
        visited = [0 for _ in range(n)]
        adj_list = [[] for _ in range(n)]
        count = [[0] * 26 for _ in range(n)]
        max_color_val = 0

        for edge in edges:
            adj_list[edge[0]].append(edge[1])

        def dfs(i):
            if visited[i] == 1:
                return INF

            if visited[i] == 2:
                return count[i][ord(colors[i]) - ord("a")]

            visited[i] = 1
            for node in adj_list[i]:
                # visit the neighbor
                res = dfs(node)
                if res == INF:  # cycle detected
                    return INF
                for color in range(26):  # consider all possible colors
                    count[i][color] = max(count[i][color], count[node][color])

            # base case -> no neighbors or all neighbors are visited
            cur_color = ord(colors[i]) - ord("a")
            count[i][cur_color] += 1
            visited[i] = 2

            return count[i][cur_color]

        for i in range(n):
            cur_color_val = dfs(
                i
            )  # the largest color path must start somewhere, we just consider all possible starting points
            if cur_color_val == INF:
                return -1
            max_color_val = max(max_color_val, cur_color_val)

        # Time Complexity: O(n + m) where n is the number of nodes and m is the number of edges
        # Space Complexity: O(m + n)
        return max_color_val
