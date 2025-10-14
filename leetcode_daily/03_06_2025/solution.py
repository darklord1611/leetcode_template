# LeetCode Daily Challenge (2025-06-03)
# Title: Maximum Candies You Can Get from Boxes
# Difficulty: Hard
# URL: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
#
# You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:
#
#
# 	status[i] is 1 if the ith box is open and 0 if the ith box is closed,
# 	candies[i] is the number of candies in the ith box,
# 	keys[i] is a list of the labels of the boxes you can open after opening the ith box.
# 	containedBoxes[i] is a list of the boxes you found inside the ith box.
#
#
# You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
#
# Return the maximum number of candies you can get following the rules above.
#
#


# Your solution starts here

from typing import List
from collections import deque


# DFS
class Solution1:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        # so we have a bunch of boxes
        # boxes could be already opened or closed
        # each box contains some number of candies and potentially contains some number of boxes
        # we given with some initial number of boxes

        # we recursively open all the boxes we could, then just sum up the candies based on status

        total_candies = 0
        n = len(status)
        has_box = [False] * n
        used = [False] * n

        def dfs(box_idx):
            if used[box_idx] is True:
                return 0

            if (
                status[box_idx] == 0
            ):  # if the current box is closed -> then we add to the list of acquired & unused boxes
                has_box[box_idx] = True
                return 0

            used[box_idx] = True
            total = candies[box_idx]

            for next_box_idx in containedBoxes[box_idx]:
                total += dfs(next_box_idx)

            for box_key in keys[box_idx]:
                status[box_key] = 1  # "open" the box
                if (
                    has_box[box_key] is True
                ):  # if we have the box of current key then just collect things within that box
                    total += dfs(box_key)

            return total

        for box in initialBoxes:
            total_candies += dfs(box)

        return total_candies


# BFS
class Solution2:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        # so we have a bunch of boxes
        # boxes could be already opened or closed
        # each box contains some number of candies and potentially contains some number of boxes
        # we given with some initial number of boxes

        # we recursively open all the boxes we could, then just sum up the candies based on status

        # there are two ways we can collect the items inside a box, either by collect an opened box or collect the unopened box and the corresponding key

        total_candies = 0
        n = len(status)
        has_box = [False] * n
        used = [False] * n
        queue = deque()

        # first we add to the queue the initial boxes that we can collect

        for box in initialBoxes:
            has_box[box] = (
                True  # we obtain the box itself, not necessarily the items inside the box, just the box
            )
            if status[box] == 1:  # box is already opened
                queue.append(box)
                used[box] = True
                total_candies += candies[box]

        while len(queue) != 0:
            cur_box = queue.popleft()

            # traverse through the keys, append the box if we have the corresponding key
            for key in keys[cur_box]:
                status[key] = 1
                if not used[key] and has_box[key]:
                    queue.append(key)
                    used[key] = True
                    total_candies += candies[key]

            # traverse through the box, only append the box we could open
            for box in containedBoxes[cur_box]:
                has_box[box] = True
                if not used[box] and status[box] == 1:
                    queue.append(box)
                    used[box] = True
                    total_candies += candies[box]

        return total_candies
