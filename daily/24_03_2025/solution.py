# LeetCode Daily Challenge (2025-03-24)
# Title: Count Days Without Meetings
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-days-without-meetings/
#
# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
# 
# Return the count of days when the employee is available for work but no meetings are scheduled.
# 
# Note: The meetings may overlap.
# 
#  


# Your solution starts here
from typing import List
import heapq

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        total_free_days = 0
        cur_max_occupied_day = 0
        
        heapq.heapify(meetings)


        while len(meetings) != 0:

            start_day, end_day = heapq.heappop(meetings)
            if start_day <= cur_max_occupied_day: # overlapped meetings
                cur_max_occupied_day = max(cur_max_occupied_day, end_day)
            else:
                total_free_days += start_day - cur_max_occupied_day - 1
                cur_max_occupied_day = end_day
        
        total_free_days += days - cur_max_occupied_day


        # Time complexity: O(nlogn)
        # Space complexity: O(n)

        return total_free_days
