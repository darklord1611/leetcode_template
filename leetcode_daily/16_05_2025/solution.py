# LeetCode Daily Challenge (2025-05-16)
# Title: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/
#
# You are given a string array words, and an array groups, both arrays having length n.
#
# The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.
#
# You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:
#
#
# 	For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 &lt; j + 1 &lt; k.
# 	words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 &lt; j + 1 &lt; k, for all indices in the subsequence.
#
#
# Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.
#
# Note: strings in words may be unequal in length.
#
#


# Your solution starts here
from typing import List


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        # hamming_distance -> number of indices that have different characters
        # find the longest sequence, each string pair in the sequence need to be of the same length, with different groups
        # DP? gradually build up the sequence, at each index, consider all possible indices come before

        n = len(words)
        dp = [1] * n
        prev_idx = [-1] * n
        max_idx = 0

        def calcHamDis(str1: str, str2: str) -> int:
            diff_idx_cnt = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff_idx_cnt += 1

            return diff_idx_cnt

        for i in range(n):
            for j in range(i):
                if (
                    len(words[i]) != len(words[j])
                    or groups[i] == groups[j]
                    or calcHamDis(words[i], words[j]) != 1
                ):
                    continue

                # if the string satisfy -> update length
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev_idx[i] = j

                if dp[i] > dp[max_idx]:
                    max_idx = i

        res = []
        last_idx = max_idx
        while last_idx >= 0:
            res.append(words[last_idx])
            last_idx = prev_idx[last_idx]

        res.reverse()

        # Time complexity: O(n^2 * m), where n is the number of words and m is the maximum length of the words
        # Space complexity: O(n), where n is the number of words
        return res


# WRONG ASSUMPTION OF THE PROBLEM, we could potentially drop some words in order to gain a longer sequence


class WrongSolution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        # hamming_distance -> number of indices that have different characters
        # find the longest sequence, each string pair in the sequence need to be of the same length, with different groups
        # possible length from 1 to 10 -> brute force?

        # same approach as before, simulate the possible solutions by building up the sequences

        n = len(words)
        max_str_len = 10

        seqs = [[] for _ in range(max_str_len)]
        cur_groups = [-1 for _ in range(max_str_len)]

        def calcHamDis(str1: str, str2: str) -> int:
            diff_idx_cnt = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff_idx_cnt += 1

            return diff_idx_cnt

        for i in range(n):
            for str_len in range(max_str_len):  # length range from 0 to 10 -> O(1)
                if (
                    len(words[i]) != str_len + 1
                ):  # if the current string of diff length -> skip
                    continue

                if (
                    groups[i] == cur_groups[str_len]
                ):  # if current string belongs to the same previous group -> skip
                    continue

                if (
                    len(seqs[str_len]) == 0
                    or calcHamDis(seqs[str_len][len(seqs[str_len]) - 1], words[i]) == 1
                ):
                    seqs[str_len].append(words[i])
                    cur_groups[str_len] = groups[i]

        # we got longest subsequences of different length -> now compare
        max_len, max_index = -1, -1

        for str_len in range(max_str_len):
            if len(seqs[str_len]) > max_len:
                max_len = len(seqs[str_len])
                max_index = str_len

        return seqs[max_index]
