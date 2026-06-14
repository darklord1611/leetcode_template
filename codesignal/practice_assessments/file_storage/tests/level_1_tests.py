import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from file_storage_impl import FileStorageImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for File Storage - Basic Storage

	Tests cover: FILE_UPLOAD, FILE_GET, FILE_COPY
	"""

	failureException = Exception

	def setUp(self):
		self.storage = FileStorageImpl()

	@timeout(0.4)
	def test_level_1_case_01_upload(self):
		self.assertEqual(self.storage.file_upload(1, "a.txt", 100), "true")

	@timeout(0.4)
	def test_level_1_case_02_upload_duplicate(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.assertEqual(self.storage.file_upload(2, "a.txt", 200), "")

	@timeout(0.4)
	def test_level_1_case_03_get(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.assertEqual(self.storage.file_get(2, "a.txt"), "100")

	@timeout(0.4)
	def test_level_1_case_04_get_missing(self):
		self.assertEqual(self.storage.file_get(1, "missing.txt"), "")

	@timeout(0.4)
	def test_level_1_case_05_duplicate_does_not_overwrite(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_upload(2, "a.txt", 999)
		self.assertEqual(self.storage.file_get(3, "a.txt"), "100")

	@timeout(0.4)
	def test_level_1_case_06_copy(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.assertEqual(self.storage.file_copy(2, "a.txt", "b.txt"), "true")
		self.assertEqual(self.storage.file_get(3, "b.txt"), "100")

	@timeout(0.4)
	def test_level_1_case_07_copy_missing_source(self):
		self.assertEqual(self.storage.file_copy(1, "missing.txt", "b.txt"), "")

	@timeout(0.4)
	def test_level_1_case_08_copy_overwrites_dest(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_upload(2, "b.txt", 50)
		self.assertEqual(self.storage.file_copy(3, "a.txt", "b.txt"), "true")
		self.assertEqual(self.storage.file_get(4, "b.txt"), "100")

	@timeout(0.4)
	def test_level_1_case_09_copy_source_unchanged(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_copy(2, "a.txt", "b.txt")
		self.assertEqual(self.storage.file_get(3, "a.txt"), "100")

	@timeout(0.4)
	def test_level_1_case_10_copy_missing_dest_not_created(self):
		self.storage.file_copy(1, "missing.txt", "b.txt")
		self.assertEqual(self.storage.file_get(2, "b.txt"), "")


if __name__ == "__main__":
	unittest.main()
