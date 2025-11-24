# LeetCode Daily Challenge (2025-04-04)
# Title: Lowest Common Ancestor of Deepest Leaves
# Difficulty: Medium
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
#
# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
#
# Recall that:
#
#
# 	The node of a binary tree is a leaf if and only if it has no children
# 	The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# 	The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
#
#
#


# Your solution starts here
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		def dfs(cur_node) -> tuple:
			if not cur_node:
				return None, 0

			left_node, left_height = dfs(cur_node.left)
			right_node, right_height = dfs(cur_node.right)

			if left_height == right_height:  #
				return cur_node, 1 + left_height
			elif left_height < right_height:  #
				return right_node, right_height + 1
			else:  #
				return left_node, left_height + 1

		cur_node, height = dfs(root)

		return cur_node
