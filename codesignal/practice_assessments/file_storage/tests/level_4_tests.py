import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from file_storage_impl import FileStorageImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for File Storage - Rollback

	Tests cover: ROLLBACK and rollback-awareness of the read operations.
	"""

	failureException = Exception

	def setUp(self):
		self.storage = FileStorageImpl()

	@timeout(0.4)
	def test_level_4_case_01_rollback_returns_true(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.assertEqual(self.storage.rollback(10, 5), "true")

	@timeout(0.4)
	def test_level_4_case_02_removes_later_uploads(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_upload(8, "b.txt", 200)
		self.storage.rollback(10, 5)
		self.assertEqual(self.storage.file_get(10, "b.txt"), "")

	@timeout(0.4)
	def test_level_4_case_03_keeps_earlier_uploads(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_upload(8, "b.txt", 200)
		self.storage.rollback(10, 5)
		self.assertEqual(self.storage.file_get(10, "a.txt"), "100")

	@timeout(0.4)
	def test_level_4_case_04_restores_overwritten_size(self):
		# a.txt was 100 at time 5; copy overwrote it to 999 at time 8.
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_upload(2, "big", 999)
		self.storage.file_copy(8, "big", "a.txt")
		self.storage.rollback(10, 5)
		self.assertEqual(self.storage.file_get(10, "a.txt"), "100")

	@timeout(0.4)
	def test_level_4_case_05_rollback_to_before_upload(self):
		self.storage.file_upload(5, "a.txt", 100)
		self.storage.rollback(10, 3)
		self.assertEqual(self.storage.file_get(10, "a.txt"), "")

	@timeout(0.4)
	def test_level_4_case_06_ttl_remaining_preserved(self):
		# Alive [10, 30); at rollback_to=20 it has 10 left, expiry stays 30.
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 20)
		self.storage.rollback(25, 20)
		self.assertEqual(self.storage.file_get(29, "a.txt"), "100")
		self.assertEqual(self.storage.file_get(30, "a.txt"), "")

	@timeout(0.4)
	def test_level_4_case_07_expired_by_rollback_point_dropped(self):
		# Alive [10, 15); already expired by rollback_to=20.
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 5)
		self.storage.rollback(25, 20)
		self.assertEqual(self.storage.file_get(20, "a.txt"), "")

	@timeout(0.4)
	def test_level_4_case_08_search_reflects_rollback(self):
		self.storage.file_upload(1, "doc_a", 100)
		self.storage.file_upload(8, "doc_b", 200)
		self.storage.rollback(10, 5)
		self.assertEqual(self.storage.file_search(10, "doc"), "doc_a")

	@timeout(0.4)
	def test_level_4_case_09_upload_after_rollback(self):
		self.storage.file_upload(1, "a.txt", 100)
		self.storage.file_upload(8, "a.txt", 999)
		self.storage.rollback(10, 5)
		# a.txt is back to size 100; uploading the same name is blocked.
		self.assertEqual(self.storage.file_upload(11, "a.txt", 5), "")
		self.assertEqual(self.storage.file_get(11, "a.txt"), "100")

	@timeout(0.4)
	def test_level_4_case_10_permanent_survives_rollback(self):
		self.storage.file_upload(2, "a.txt", 100)
		self.storage.rollback(50, 5)
		self.assertEqual(self.storage.file_get(99999, "a.txt"), "100")


if __name__ == "__main__":
	unittest.main()
