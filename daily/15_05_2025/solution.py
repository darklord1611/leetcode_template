# LeetCode Daily Challenge ()
# Title: 
# Difficulty: 
# URL: https://leetcode.com/problems//
#
# 


# Your solution starts here
from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # invalid sequence would be [0, 0] or [1, 1]
        # longest subsequence? two possible scenarios -> either we have a subsequence starts from group 0 or group 1
        # try both, loop through other elements, keep track of the indices and the next group for both sequence
        # take the max length -> take the indices

        n = len(words)
        
        sub_seqs = [[], []]
        res = []
        next_groups = [0, 1]

        for i in range(n):
            if groups[i] == next_groups[0]:
                sub_seqs[0].append(i)
                next_groups[0] = 1 - next_groups[0]
            
            if groups[i] == next_groups[1]:
                sub_seqs[1].append(i)
                next_groups[1] = 1 - next_groups[1]

        res = sub_seqs[1] if len(sub_seqs[1]) >= len(sub_seqs[0]) else sub_seqs[0]

        return [words[idx] for idx in res]
