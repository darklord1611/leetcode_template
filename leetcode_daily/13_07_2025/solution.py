# LeetCode Daily Challenge (2025-07-13)
# Title: Maximum Matching of Players With Trainers
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
#
# You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.
#
# The ith player can match with the jth trainer if the player&#39;s ability is less than or equal to the trainer&#39;s training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.
#
# Return the maximum number of matchings between players and trainers that satisfy these conditions.
#
#


# Your solution starts here
from typing import List


class Solution:
	def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
		# greedy -> sort both the players and trainers ascendingly, then just pick accordingly
		m = len(players)
		n = len(trainers)

		players.sort()
		trainers.sort()

		i = 0
		j = 0
		matches = 0
		while i < m and j < n:
			if players[i] <= trainers[j]:
				matches += 1
				i += 1
				j += 1
			else:
				j += 1

		return matches
