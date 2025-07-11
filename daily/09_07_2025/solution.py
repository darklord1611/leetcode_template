# LeetCode Daily Challenge (2025-07-09)
# Title: Reschedule Meetings for Maximum Free Time I
# Difficulty: Medium
# URL: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/
#
# You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
# 
# You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
# 
# You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
# 
# The relative order of all the meetings should stay the same and they should remain non-overlapping.
# 
# Return the maximum amount of free time possible after rearranging the meetings.
# 
# Note that the meetings can not be rescheduled to a time outside the event.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # n meetings produce n + 1 breaks, with one meeting, we have the break before and after that meeting
        # with 2 meetings, we have 3 breaks, and so on -> n meetings have n + 1 breaks
        # the rescheduling operation is almost like pushing every events to the leftmost and effectively merge the breaks -> k events then we merge k + 1 consecutive(because of the relative order) breaks
        # problem boils down to find the maximum sum of k + 1 consecutive breaks

        breaks = []
        last_meeting_end = 0

        for start, end in zip(startTime, endTime):
            break_time = start - last_meeting_end

            breaks.append(break_time)
            
            last_meeting_end = end
        
        last_break_time = eventTime - last_meeting_end
        breaks.append(last_break_time)

        max_break = 0
        cur_break = 0
        left = 0
        n = len(breaks)

        for right in range(n):
            if right - left + 1 > k + 1: # maintain a window of size k + 1
                cur_break -= breaks[left]
                left += 1

            cur_break += breaks[right]
            max_break = max(max_break, cur_break)
        
        return max_break
    



