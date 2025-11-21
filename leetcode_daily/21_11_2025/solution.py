# LeetCode Daily Challenge (2025-11-21)\n# Title: Unique Length-3 Palindromic Subsequences\n# Difficulty: Medium\n# Acceptance Rate: 71.5137291343821\n# Tags: Hash Table, String, Bit Manipulation, Prefix Sum\n# URL: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/\n#\n# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
#
# 	For example, &quot;ace&quot; is a subsequence of &quot;abcde&quot;.
#
#
#


# Your solution starts here


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # abcdedeabc

        # the subsequence would be in the form of XxX, we need a way to keep track of the frequencies of possible characters on the left and on the right of a particular index

        # food for thought: what about counting in-between letters between two identical characters aka reverse the way we define the problem?
        # What happened if the length of palindrome is not fixed to 3 and is arbitrary?

        prefix_freqs = []
        n = len(s)
        unique_subseq = set()
        count = 0
        total_freq = [0 for _ in range(26)]

        for i in range(n):
            total_freq[ord(s[i]) - ord("a")] += 1

            prefix_freqs.append(list(total_freq))

        for i in range(1, n - 1):
            # the count arr of left of this index would be i - 1
            for j in range(26):  # loop through every single X character
                cur_subseq = chr(97 + j) + s[i] + chr(97 + j)
                if cur_subseq in unique_subseq:
                    continue

                left_count = prefix_freqs[i - 1][j]
                right_count = total_freq[j] - prefix_freqs[i][j]
                if left_count > 0 and right_count > 0:
                    count += 1
                    unique_subseq.add(cur_subseq)

        # Time complexity: O(n)
        # Space complexity: O(n)
        return count
