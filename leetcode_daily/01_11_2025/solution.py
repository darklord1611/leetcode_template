# LeetCode Daily Challenge (2025-11-01)\n# Title: Delete Nodes From Linked List Present in Array\n# Difficulty: Medium\n# Acceptance Rate: 68.79984700790011\n# Tags: Array, Hash Table, Linked List\n# URL: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/\n#\n# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
#
#


# Your solution starts here
from collections import defaultdict
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
		# get the first node which values are not in nums -> gonna be our new head
		# store nums as dict for faster lookup

		lookup = defaultdict(int)
		for num in nums:
			lookup[num] = 1

		# find our new head
		cur = head
		new_head = None

		while lookup[cur.val] != 0:  # meaning we still have to delete the current number
			cur = cur.next

		new_head = cur

		# advance prev and cur ptrs
		prev = cur
		cur = cur.next

		while cur != None:
			if lookup[cur.val] == 1:
				prev.next = cur.next
				cur.next = None
				cur = prev.next
			else:
				prev = cur
				cur = cur.next

		return new_head
