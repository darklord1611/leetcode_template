# LeetCode Daily Challenge (2026-06-15)\n# Title: Delete the Middle Node of a Linked List\n# Difficulty: Medium\n# Acceptance Rate: 59.71351672134454\n# Tags: Linked List, Two Pointers\n# URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/\n#\n# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# 
# The middle node of a linked list of size n is the &lfloor;n / 2&rfloor;th node from the start using 0-based indexing, where &lfloor;x&rfloor; denotes the largest integer less than or equal to x.
# 
# 
# 	For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# 
# 
#  


# Your solution starts here

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow fast pointers

        slow = head
        fast = head
        prev = None

        if head.next is None:
            return None

        while True:
            # 2 cases, odd vs even number of nodes

            # case 1, odd number of nodes
            if fast.next is None:
                temp = prev.next
                prev.next = prev.next.next
                temp.next = None
                break
            
            # case 2, even number of nodes
            if fast.next.next is None:
                temp = slow.next
                slow.next = slow.next.next
                temp.next = None
                break
            
            prev = slow
            slow = slow.next
            fast = fast.next.next
    
        # Time Complexity: O(n) where n is the number of nodes in the linked list
        # Space Complexity: O(1) since we are not using any additional data structures that grow with the input size
        return head
        

