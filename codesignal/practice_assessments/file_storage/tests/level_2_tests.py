import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from file_storage_impl import FileStorageImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for File Storage - Search

	Tests cover: FILE_SEARCH
	"""

	failureException = Exception

	def setUp(self):
		self.storage = FileStorageImpl()

	@timeout(0.4)
	def test_level_2_case_01_search_no_match(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.assertEqual(self.storage.file_search(2, "zzz"), "")

	@timeout(0.4)
	def test_level_2_case_02_search_empty_store(self):
		self.assertEqual(self.storage.file_search(1, "doc"), "")

	@timeout(0.4)
	def test_level_2_case_03_search_single_match(self):
		self.storage.file_upload(1, "doc_a", 100)
		self.assertEqual(self.storage.file_search(2, "doc"), "doc_a")

	@timeout(0.4)
	def test_level_2_case_04_search_size_desc(self):
		self.storage.file_upload(1, "doc_a", 100)
		self.storage.file_upload(1, "doc_b", 300)
		self.storage.file_upload(1, "doc_c", 200)
		self.assertEqual(self.storage.file_search(2, "doc"), "doc_b, doc_c, doc_a")

	@timeout(0.4)
	def test_level_2_case_05_search_tie_name_asc(self):
		self.storage.file_upload(1, "doc_y", 100)
		self.storage.file_upload(1, "doc_x", 100)
		self.assertEqual(self.storage.file_search(2, "doc"), "doc_x, doc_y")

	@timeout(0.4)
	def test_level_2_case_06_search_prefix_filters(self):
		self.storage.file_upload(1, "doc_a", 500)
		self.storage.file_upload(1, "img_a", 900)
		self.assertEqual(self.storage.file_search(2, "doc"), "doc_a")

	@timeout(0.4)
	def test_level_2_case_07_search_empty_prefix_all(self):
		self.storage.file_upload(1, "a", 100)
		self.storage.file_upload(1, "b", 200)
		self.assertEqual(self.storage.file_search(2, ""), "b, a")

	@timeout(0.4)
	def test_level_2_case_08_search_top_10_limit(self):
		for i in range(15):
			self.storage.file_upload(1, "f" + str(i).zfill(2), i + 1)
		# Largest sizes are f14..f05 (10 files), size desc.
		expected = ", ".join("f" + str(i).zfill(2) for i in range(14, 4, -1))
		self.assertEqual(self.storage.file_search(2, "f"), expected)

	@timeout(0.4)
	def test_level_2_case_09_search_after_copy(self):
		self.storage.file_upload(1, "doc_a", 100)
		self.storage.file_copy(2, "doc_a", "doc_b")
		self.assertEqual(self.storage.file_search(3, "doc"), "doc_a, doc_b")

	@timeout(0.4)
	def test_level_2_case_10_search_mixed_ties(self):
		self.storage.file_upload(1, "doc_a", 200)
		self.storage.file_upload(1, "doc_c", 200)
		self.storage.file_upload(1, "doc_b", 300)
		self.assertEqual(self.storage.file_search(2, "doc"), "doc_b, doc_a, doc_c")


if __name__ == "__main__":
	unittest.main()
