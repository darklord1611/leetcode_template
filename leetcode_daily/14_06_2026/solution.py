# LeetCode Daily Challenge (2026-06-14)\n# Title: Maximum Twin Sum of a Linked List\n# Difficulty: Medium\n# Acceptance Rate: 81.7791359318901\n# Tags: Linked List, Two Pointers, Stack\n# URL: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/\n#\n# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 &lt;= i &lt;= (n / 2) - 1.
# 
# 
# 	For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# 
# 
# The twin sum is defined as the sum of a node and its twin.
# 
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
# 
#  


# Your solution starts here
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        cur_node = head
        while cur_node is not None:
            nums.append(cur_node.val)
            cur_node = cur_node.next
        
        left = 0
        right = len(nums) - 1
        max_sum = 0

        while left <= right:
            max_sum = max(nums[left] + nums[right], max_sum)
            left += 1
            right -= 1
        
        # Time Complexity: O(n) where n is the number of nodes in the linked list
        # Space Complexity: O(n) where n is the number of nodes in the linked list (for storing the values in an array)
        return max_sum


class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # slow and fast pointers to figure out the middle node
        
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        

        prev = None
        cur = slow_ptr
        nxt = slow_ptr.next

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # prev is the head of second-half reversed list
        head_1 = head
        head_2 = prev
        max_sum = 0
        while head_1 is not None and head_2 is not None:
            max_sum = max(max_sum, head_1.val + head_2.val)
            head_1 = head_1.next
            head_2 = head_2.next
        
        # Time Complexity: O(n) where n is the number of nodes in the linked list
        # Space Complexity: O(1) since we are reversing the second half of the linked list in-places
        return max_sum