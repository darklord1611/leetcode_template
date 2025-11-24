from typing import List


class Solution:
	def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
		# find all smaller numbers and then put them into a list
		# find all larger numbers and then put them into another list
		# count all occurences of pivot numbers

		n = len(nums)
		less_than_pivot = []
		greater_than_pivot = []
		pivot_count = 0

		for i in range(n):
			if nums[i] < pivot:
				less_than_pivot.append(nums[i])
			elif nums[i] > pivot:
				greater_than_pivot.append(nums[i])
			else:
				pivot_count += 1

		less_than_pivot.extend([pivot for _ in range(pivot_count)])
		less_than_pivot.extend(greater_than_pivot)

		return less_than_pivot
