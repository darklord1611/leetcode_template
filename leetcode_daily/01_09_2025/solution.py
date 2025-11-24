# LeetCode Daily Challenge (2025-09-01)
# Title: Maximum Average Pass Ratio
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-average-pass-ratio/
#
# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
#
# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
#
# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
#
# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.
#
#


# Your solution starts here
import heapq
from typing import List


class Solution:
	def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
		# pass ratio = number of students pass / total students in that class
		# notice that the larger the ratio, the less we will gain if we put an extra student in that class
		# Example: original ratio 1: 3/5 -> 4/6 gain more than 4/5 -> 5/6
		# -> prioritize classes with small pass ratio -> gain more
		# key info: whenever we "add" an extra student -> the ratio changes -> the order of ratio magnitude also changes

		# we need a data structure to keep track of the smallest ratio at a specific time -> heap

		# the above approach is wrong since the smallest ratio may not yield the most gain, instead keep track of how much we would gain if we were to increment a class

		heap = []
		n = len(classes)
		ans = 0.0

		for i in range(n):
			num_pass, total_pass = classes[i]
			gain = (num_pass + 1) / (total_pass + 1) - num_pass / total_pass
			heapq.heappush(heap, (-gain, num_pass, total_pass))

		while extraStudents != 0:
			_, num_pass, total_pass = heapq.heappop(heap)

			num_pass += 1
			total_pass += 1

			gain = (num_pass + 1) / (total_pass + 1) - num_pass / total_pass
			heapq.heappush(heap, (-gain, num_pass, total_pass))  # num_pass and total_pass here are the updated after add an extra student
			extraStudents -= 1

		for i in range(n):
			_, num_pass, total_pass = heapq.heappop(heap)
			ans += num_pass / total_pass
		# Time Complexity: O(nlogn)
		# Space Complexity: O(n)

		return ans / n
