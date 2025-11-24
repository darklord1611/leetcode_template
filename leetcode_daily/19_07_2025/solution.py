# LeetCode Daily Challenge ()
# Title:
# Difficulty:
# URL: https://leetcode.com/problems//
#
#


# Your solution starts here
from typing import List


class Solution:
	def removeSubfolders(self, folders: List[str]) -> List[str]:
		# sort according to the length?

		# child folders will appear directly after the parent folder, just keep track of the parent folder and check
		folders.sort()
		valid_folders = [folders[0]]

		for i in range(1, len(folders)):
			last_folder = valid_folders[-1]
			last_folder += "/"

			if not folders[i].startswith(last_folder):
				valid_folders.append(folders[i])

		return valid_folders
