# LeetCode Daily Challenge (2025-05-30)
# Title: Find Closest Node to Given Two Nodes
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
#
# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
# 
# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
# 
# You are also given two integers node1 and node2.
# 
# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.
# 
# Note that edges may contain cycles.
# 
#  


# Your solution starts here
from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # we have two nodes: A and B
        # we need to find another node C (reachable from A and B) so that max(dis(A, C), dis(B, C)) is minimized
        # first step would be finding all the mutual nodes that reachable from both A and B
        # then we check for each satisfied node and find the min dist

        n = len(edges)
        adj_list = [[] for _ in range(n)]s
        min_dist = float("inf")
        min_idx = -1
        for i in range(n):
            if edges[i] != -1:
                adj_list[i].append(edges[i])
        
        def calc_dist(node):
            node_dist = {}
            visited = [0 for _ in range(n)]
            queue = deque()
            queue.append(node)
            cur_dist = 0
            while len(queue) != 0:
                for i in range(len(queue)):
                    cur_node = queue.popleft()
                    node_dist[cur_node] = cur_dist
                    visited[cur_node] = 1
                    # add the neighbor of current node
                    for adj_node in adj_list[cur_node]:
                        if not visited[adj_node]: # account for cycle
                            queue.append(adj_node)
                cur_dist += 1
            
            return node_dist
            
        node1_dist = calc_dist(node1)
        node2_dist = calc_dist(node2)

        for i in range(n):
            if i in node1_dist and i in node2_dist:
                cur_dist = max(node1_dist[i], node2_dist[i])
                if cur_dist < min_dist: 
                    min_dist = cur_dist
                    min_idx = i
        
        return min_idx

            

    