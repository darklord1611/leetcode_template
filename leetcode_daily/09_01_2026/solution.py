# LeetCode Daily Challenge (2026-01-09)\n# Title: Smallest Subtree with all the Deepest Nodes\n# Difficulty: Medium\n# Acceptance Rate: 73.51778656126481\n# Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree\n# URL: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/\n#\n# Given the root of a binary tree, the depth of each node is the shortest distance to the root.
#
# Return the smallest subtree such that it contains all the deepest nodes in the original tree.
#
# A node is called the deepest if it has the largest depth possible among any node in the entire tree.
#
# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
#
#


# Your solution starts here

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		def dfs(cur_node) -> tuple:
			if not cur_node:
				return None, 0

			left_node, left_height = dfs(cur_node.left)
			right_node, right_height = dfs(cur_node.right)

			if left_height == right_height:  #
				return cur_node, 1 + left_height
			elif left_height < right_height:  #
				return right_node, right_height + 1
			else:
				return left_node, left_height + 1

		cur_node, height = dfs(root)

		return cur_node
