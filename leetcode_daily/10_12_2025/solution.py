# LeetCode Daily Challenge (2025-12-10)\n# Title: Count the Number of Computer Unlocking Permutations\n# Difficulty: Medium\n# Acceptance Rate: 55.47335316295019\n# Tags: Array, Math, Brainteaser, Combinatorics\n# URL: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/\n#\n# You are given an array complexity of length n.
# 
# There are n locked computers in a room with labels from 0 to n - 1, each with its own unique password. The password of the computer i has a complexity complexity[i].
# 
# The password for the computer labeled 0 is already decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:
# 
# 
# 	You can decrypt the password for the computer i using the password for computer j, where j is any integer less than i with a lower complexity. (i.e. j &lt; i and complexity[j] &lt; complexity[i])
# 	To decrypt the password for computer i, you must have already unlocked a computer j such that j &lt; i and complexity[j] &lt; complexity[i].
# 
# 
# Find the number of permutations of [0, 1, 2, ..., (n - 1)] that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.
# 
# Since the answer may be large, return it modulo 109 + 7.
# 
# Note that the password for the computer with label 0 is decrypted, and not the computer with the first position in the permutation.
# 
#  


# Your solution starts here
from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        # ok we have a list of locked computers naming from computer 0 -> computer n - 1
        # each computer has a value called complexity (int) like 0, 1,2, 3 ....

        # we have to count number of permutations to unlock all computers 

        # some conditions
        # we can unlock a computer i when we have already cracked the password for a computer j (j < i) and computer j has less complex password

        # j could be an arbitrary index as long as it satisfies (j < i) and (comp[j] < comp[i])

        # computer 0 is already unlocked -> what does this tell us? if computer 0 complexity is the highest -> then we can't crack the rest of the computers

        # think of this example [3,3,3,4,4,4] -> why 0?
        # the first computer always gonna be computer 0 right? so it should be the unique smallest element in order to generate a valid sequence

        # ok get that out of the way, then what for the rest of the elements? effectively when we unlock computer 0 with the above constraints then all other computers are unlocked -> why? think of the another wordings for the constraints -> just (n - 1) factorials

        n = len(complexity)
        min_count = 0
        cur_min = 10 ** 9 + 1
        MOD = 10 ** 9 + 7
        for i in range(n):
            if complexity[i] < cur_min:
                cur_min = complexity[i]
                min_count = 1
            elif complexity[i] == cur_min:
                min_count += 1
        if min(complexity) != complexity[0] or min_count > 1:
            return 0
        
        ans = 1
        for i in range(1, n):
            ans = (ans * i) % MOD

        # Time : O(n)
        # Space: O(1)
        return ans

