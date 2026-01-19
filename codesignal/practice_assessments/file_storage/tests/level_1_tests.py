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
	Level 1 tests for File Storage - Basic Operations

	Tests cover: FILE_UPLOAD, FILE_GET, FILE_COPY
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh FileStorage instance for each test."""
		self.storage = FileStorageImpl()

	@timeout(0.4)
	def test_level_1_case_01_upload_single_file(self):
		"""Test uploading a single file."""
		result = self.storage.file_upload("Cars.txt", "200kb")
		self.assertEqual(result, "uploaded Cars.txt")

	@timeout(0.4)
	def test_level_1_case_02_get_existing_file(self):
		"""Test getting an existing file."""
		self.storage.file_upload("Cars.txt", "200kb")
		result = self.storage.file_get("Cars.txt")
		self.assertEqual(result, "got Cars.txt")

	@timeout(0.4)
	def test_level_1_case_03_copy_file(self):
		"""Test copying a file."""
		self.storage.file_upload("Cars.txt", "200kb")
		result = self.storage.file_copy("Cars.txt", "Cars2.txt")
		self.assertEqual(result, "copied Cars.txt to Cars2.txt")

	@timeout(0.4)
	def test_level_1_case_04_get_copied_file(self):
		"""Test getting a file that was copied."""
		self.storage.file_upload("Cars.txt", "200kb")
		self.storage.file_copy("Cars.txt", "Cars2.txt")
		result = self.storage.file_get("Cars2.txt")
		self.assertEqual(result, "got Cars2.txt")

	@timeout(0.4)
	def test_level_1_case_05_upload_multiple_files(self):
		"""Test uploading multiple files."""
		result1 = self.storage.file_upload("File1.txt", "100kb")
		result2 = self.storage.file_upload("File2.txt", "200kb")
		result3 = self.storage.file_upload("File3.txt", "300kb")
		self.assertEqual(result1, "uploaded File1.txt")
		self.assertEqual(result2, "uploaded File2.txt")
		self.assertEqual(result3, "uploaded File3.txt")

	@timeout(0.4)
	def test_level_1_case_06_copy_overwrites_destination(self):
		"""Test that copying overwrites existing destination file."""
		self.storage.file_upload("Source.txt", "100kb")
		self.storage.file_upload("Dest.txt", "200kb")
		result = self.storage.file_copy("Source.txt", "Dest.txt")
		self.assertEqual(result, "copied Source.txt to Dest.txt")

	@timeout(0.4)
	def test_level_1_case_07_multiple_operations(self):
		"""Test a sequence of operations."""
		self.storage.file_upload("A.txt", "50kb")
		self.storage.file_upload("B.txt", "75kb")
		self.assertEqual(self.storage.file_get("A.txt"), "got A.txt")
		self.assertEqual(self.storage.file_get("B.txt"), "got B.txt")
		self.assertEqual(self.storage.file_copy("A.txt", "C.txt"), "copied A.txt to C.txt")
		self.assertEqual(self.storage.file_get("C.txt"), "got C.txt")

	@timeout(0.4)
	def test_level_1_case_08_copy_chain(self):
		"""Test copying a file multiple times."""
		self.storage.file_upload("Original.txt", "100kb")
		self.storage.file_copy("Original.txt", "Copy1.txt")
		self.storage.file_copy("Copy1.txt", "Copy2.txt")
		self.assertEqual(self.storage.file_get("Original.txt"), "got Original.txt")
		self.assertEqual(self.storage.file_get("Copy1.txt"), "got Copy1.txt")
		self.assertEqual(self.storage.file_get("Copy2.txt"), "got Copy2.txt")

	@timeout(0.4)
	def test_level_1_case_09_different_file_sizes(self):
		"""Test uploading files with different sizes."""
		self.assertEqual(self.storage.file_upload("Small.txt", "1kb"), "uploaded Small.txt")
		self.assertEqual(self.storage.file_upload("Medium.txt", "100kb"), "uploaded Medium.txt")
		self.assertEqual(self.storage.file_upload("Large.txt", "1000kb"), "uploaded Large.txt")

	@timeout(0.4)
	def test_level_1_case_10_different_file_types(self):
		"""Test uploading files with different extensions."""
		self.assertEqual(self.storage.file_upload("Document.txt", "50kb"), "uploaded Document.txt")
		self.assertEqual(self.storage.file_upload("Spreadsheet.csv", "75kb"), "uploaded Spreadsheet.csv")
		self.assertEqual(self.storage.file_upload("Presentation.pdf", "100kb"), "uploaded Presentation.pdf")
		self.assertEqual(self.storage.file_get("Document.txt"), "got Document.txt")
		self.assertEqual(self.storage.file_get("Spreadsheet.csv"), "got Spreadsheet.csv")
		self.assertEqual(self.storage.file_get("Presentation.pdf"), "got Presentation.pdf")


if __name__ == "__main__":
	unittest.main()
