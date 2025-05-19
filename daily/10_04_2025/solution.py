# LeetCode Daily Challenge (2025-04-10)
# Title: Count the Number of Powerful Integers
# Difficulty: Hard
# URL: https://leetcode.com/problems/count-the-number-of-powerful-integers/
#
# You are given three integers start, finish, and limit. You are also given a 0-indexed string s representing a positive integer.
#
# A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.
#
# Return the total number of powerful integers in the range [start..finish].
#
# A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.
#
#


# Your solution starts here
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # start from the string s, append valid numbers within limit
        # Example: start = 1, finish = 6000, limit = 4, s = "24"
        # numbers with 2 digits -> 24
        # number with 3 digits -> 124, 224, 324 -> we have (limit - 1) choices for what number to append
        # number with 4 digits -> 1124, 1224, 1324, 2124, 2224, 2324, 3124, 3224, 3324
        # f(x) == 1 if x == s
        # f(x) == f(x - 1) * (limit - 1) -> precompute the valid numbers of each distinct length
        # start = 6000, suffix = 24, limit = 4

        cnt = [0] * 16

        def count(right_limit: str, suffix: str) -> int:
            i = 0
            valid_size_bound = len(right_limit) - len(suffix)
            res = cnt[len(right_limit) - 1]
            while True:
                if (
                    i == valid_size_bound
                ):  # strings with length == len(right_limit), we need to check whether they exceed right_limit
                    if right_limit[i:] >= suffix:
                        res += 1
                else:
                    res += cnt[len(right_limit) - i - 1] * (
                        min(limit, int(right_limit[i]) - 1) + (i > 0)
                    )  # we can use 0 if the current index not the leftmost
                i += 1
                if i > valid_size_bound or int(right_limit[i - 1]) > limit:
                    break
            return res

        for i in range(len(s), 16):
            cnt[i] = 1 if i == len(s) else cnt[i - 1] * (limit + 1)

        return count(str(finish), s) - count(str(start - 1), s)
