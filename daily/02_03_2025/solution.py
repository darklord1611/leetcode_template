from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        ans = []

        m = len(nums1)
        n = len(nums2)
        while ptr1 < m and ptr2 < n:

            if nums1[ptr1][0] < nums2[ptr2][0]:
                ans.append([nums1[ptr1][0], nums1[ptr1][1]])
                ptr1 += 1
            elif nums1[ptr1][0] > nums2[ptr2][0]:
                ans.append([nums2[ptr2][0], nums2[ptr2][1]])
                ptr2 += 1
            else:
                ans.append([nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
        
        while ptr1 < m:
            ans.append([nums1[ptr1][0], nums1[ptr1][1]])
            ptr1 += 1
        
        while ptr2 < n:
            ans.append([nums2[ptr2][0], nums2[ptr2][1]])
            ptr2 += 1

        return ans