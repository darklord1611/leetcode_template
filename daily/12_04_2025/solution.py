# LeetCode Daily Challenge (2025-04-12)
# Title: Find the Count of Good Integers
# Difficulty: Hard
# URL: https://leetcode.com/problems/find-the-count-of-good-integers/
#
# You are given two positive integers n and k.
# 
# An integer x is called k-palindromic if:
# 
# 
# 	x is a palindrome.
# 	x is divisible by k.
# 
# 
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.
# 
# Return the count of good integers containing n digits.
# 
# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.
# 
#  


# Your solution starts here
from collections import Counter, defaultdict
import math

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # digits can be rearranged -> we just need to generate the valid numbers and then count the permutations of those numbers
        # valid numbers -> palindrome and divisible by k -> generate palindromes first then check for divisible by k
        # permutation with repetitions?
        

        computed_numbers = {}

        def count_valid_permu_without_lead_zero(freq: dict) -> int:
            denominator = 1
            numerator = math.factorial(n)
            
            for key, val in freq.items():
                denominator = denominator * math.factorial(val) if val != 0 else denominator
            
            total_permu = numerator // denominator
            
            if freq["0"] >= 1: # possibility of leading zero
                numerator = numerator // n
                denominator = denominator // freq["0"]
                
                permu_with_lead_zero = numerator // denominator
                
                return total_permu - permu_with_lead_zero
            
            return total_permu

        def generate_palindrome(cur_len: int, cur_num: str) -> None:
            if cur_len >= (n + 1) // 2:
                if n % 2 == 0:
                    cur_num += cur_num[::-1]
                else:
                    cur_num += cur_num[:len(cur_num)-1][::-1]
                if int(cur_num) % k == 0:
                    counts = Counter(cur_num)
                    key = tuple(sorted(counts.items()))
                    if key not in computed_numbers:
                        valid_number_count = count_valid_permu_without_lead_zero(counts)
                        computed_numbers[key] = valid_number_count
                return
            
            for i in range(10):
                if cur_len == 0 and i == 0:
                    continue
                generate_palindrome(cur_len + 1, cur_num + str(i))
            
            return
        
        
        generate_palindrome(0, "")

        # Time complexity: O(10^(n/2))
        # Space complexity: O(10^(n/2))
        
        return sum(computed_numbers.values())
