from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        up_bound = n**2
        expected_sum = up_bound * (up_bound + 1) // 2
        expected_square_sum = up_bound * (up_bound + 1) * (2 * up_bound + 1) // 6
        actual_sum = 0
        actual_square_sum = 0

        for i in range(n):
            for j in range(n):
                actual_sum += grid[i][j]
                actual_square_sum += grid[i][j] ** 2

        diff = actual_sum - expected_sum
        diff_square = (actual_square_sum - expected_square_sum) // diff

        appear_twice_num = (diff + diff_square) // 2
        missing_num = diff_square - appear_twice_num

        # time complexity: O(n^2)
        # space complexity: O(1)

        return [appear_twice_num, missing_num]
