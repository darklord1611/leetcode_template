import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from file_storage_impl import FileStorageImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for File Storage - TTL

	Tests cover: FILE_UPLOAD_WITH_TTL and the reopened FILE_UPLOAD,
	FILE_GET, FILE_COPY, FILE_SEARCH.
	"""

	failureException = Exception

	def setUp(self):
		self.storage = FileStorageImpl()

	@timeout(0.4)
	def test_level_3_case_01_upload_with_ttl(self):
		self.assertEqual(self.storage.file_upload_with_ttl(10, "a.txt", 100, 5), "true")

	@timeout(0.4)
	def test_level_3_case_02_get_while_alive(self):
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 5)
		self.assertEqual(self.storage.file_get(14, "a.txt"), "100")

	@timeout(0.4)
	def test_level_3_case_03_get_at_expiry_boundary(self):
		# Alive for [10, 15); expired at 15.
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 5)
		self.assertEqual(self.storage.file_get(15, "a.txt"), "")

	@timeout(0.4)
	def test_level_3_case_04_upload_reclaims_expired_name(self):
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 5)
		self.assertEqual(self.storage.file_upload(15, "a.txt", 200), "true")
		self.assertEqual(self.storage.file_get(16, "a.txt"), "200")

	@timeout(0.4)
	def test_level_3_case_05_upload_blocked_while_alive(self):
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 5)
		self.assertEqual(self.storage.file_upload(12, "a.txt", 200), "")

	@timeout(0.4)
	def test_level_3_case_06_permanent_lives_forever(self):
		self.storage.file_upload(10, "a.txt", 100)
		self.assertEqual(self.storage.file_get(100000, "a.txt"), "100")

	@timeout(0.4)
	def test_level_3_case_07_search_ignores_expired(self):
		self.storage.file_upload_with_ttl(10, "doc_a", 100, 5)
		self.storage.file_upload(10, "doc_b", 50)
		self.assertEqual(self.storage.file_search(20, "doc"), "doc_b")

	@timeout(0.4)
	def test_level_3_case_08_copy_preserves_remaining_ttl(self):
		# Source alive [10, 20); copy at 15 -> dest expires at 20 too.
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 10)
		self.assertEqual(self.storage.file_copy(15, "a.txt", "b.txt"), "true")
		self.assertEqual(self.storage.file_get(19, "b.txt"), "100")
		self.assertEqual(self.storage.file_get(20, "b.txt"), "")

	@timeout(0.4)
	def test_level_3_case_09_copy_expired_source_fails(self):
		self.storage.file_upload_with_ttl(10, "a.txt", 100, 5)
		self.assertEqual(self.storage.file_copy(15, "a.txt", "b.txt"), "")
		self.assertEqual(self.storage.file_get(15, "b.txt"), "")

	@timeout(0.4)
	def test_level_3_case_10_copy_permanent_source_permanent_dest(self):
		self.storage.file_upload(10, "a.txt", 100)
		self.storage.file_copy(11, "a.txt", "b.txt")
		self.assertEqual(self.storage.file_get(99999, "b.txt"), "100")


if __name__ == "__main__":
	unittest.main()
