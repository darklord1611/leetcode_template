# LeetCode Daily Challenge ()
# Title: 
# Difficulty: 
# URL: https://leetcode.com/problems//
#
# 


# Your solution starts here
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_val = 0

        for operation in operations:
            if "++" in operation:
                final_val += 1
            else:
                final_val -= 1
            
        
        return final_val
