# LeetCode Daily Challenge (2025-07-14)
# Title: Convert Binary Number in a Linked List to Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
#
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# 
# Return the decimal value of the number in the linked list.
# 
# The most significant bit is at the head of the linked list.
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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bin_list = []
        ans = 0
        cur_node = head

        while cur_node != None:
            bin_list.append(cur_node.val)
            cur_node = cur_node.next
        
        n = len(bin_list)
        for i in range(n - 1, -1, -1):
            ans += 2 ** (n - 1 - i) * bin_list[i]
        
        return ans
