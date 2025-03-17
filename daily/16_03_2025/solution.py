# LeetCode Daily Challenge ()
# Title: 
# Difficulty: 
# URL: https://leetcode.com/problems//
#
# 


# Your solution starts here

from typing import List
from collections import defaultdict
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # high-ranked mechanics should fix more cars
        # DP approach? think about the constraints and how would DP fitting in this scenario?
        # can we predefine the range of possible time limits?
        # for a fixed amount of time, can we figure out how many cars can be repaired?
        # we want to find minimum amount of time, we have a predefined time range, we can calculate the number of fixed cars for a certain amount of time? -> what algorithm can make use of all these new constraints?

        n = len(ranks)

        high = max(ranks) * cars * cars
        low = 1

        freq = defaultdict(int)
        for rank in ranks:
            freq[rank] += 1

        while low < high:
            mid = (low + high) // 2
            total_cars_fixed = 0    
            for rank in freq:
                cars_count = math.floor(math.sqrt(mid / rank)) * freq[rank]
                total_cars_fixed += cars_count
            
            if total_cars_fixed >= cars: # we already fixed the required number of cars, can we do faster?
                high = mid
            else: # we are not fixing enough cars in this amount of time -> increase time limit
                low = mid + 1
        
        return low