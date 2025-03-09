from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        zero_count = 0
        for i in range(0, n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        for i in range(n):
            if nums[i] == 0:
                zero_count += 1

        res = [num for num in nums if num != 0]
        res.extend([0 for _ in range(zero_count)])

        return res
