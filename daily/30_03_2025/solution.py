# LeetCode Daily Challenge ()
# Title: 
# Difficulty: 
# URL: https://leetcode.com/problems//
#
# 


# Your solution starts here
from typing import List

class Solution:
    def partitionLabels(self, temp: str) -> List[int]:
        # all occurences of a character in the same partition? -> the first and last occurence of a character in the same partition
        # [start, end] -> forms a valid partition for a specific character
        # the partition may overlap with other characters? -> merge? -> merge what? -> merge intervals
        # https://leetcode.com/problems/merge-intervals/ -> same shit with different representation
        n = len(temp)
        first_and_last_indexes = {}

        for i in range(n):
            if temp[i] not in first_and_last_indexes:
                first_and_last_indexes[temp[i]] = [i, i]
            else:
                first_and_last_indexes[temp[i]][1] = i

        intervals = []
        for key in first_and_last_indexes:
            intervals.append(first_and_last_indexes[key])


        ans = self.check_interval(intervals)

        # Time complexity: O(n)
        # Space complexity: O(1) -> only lowercase English characters

        return ans


    def check_interval(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)
        res = []
        intervals.sort()

        min_overlap_num = intervals[0][0]
        max_overlap_num = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] <= max_overlap_num:
                max_overlap_num = max(max_overlap_num, intervals[i][1]) 
            else:
                res.append([min_overlap_num, max_overlap_num])
                min_overlap_num = intervals[i][0]
                max_overlap_num = intervals[i][1]

        res.append([min_overlap_num, max_overlap_num])


        return [part[1] - part[0] + 1 for part in res]

