import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from in_memory_database_impl import InMemoryDatabaseImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for In-Memory Database - TTL

	Tests cover: set_field_with_ttl plus reopened reads
	"""

	failureException = Exception

	def setUp(self):
		self.db = InMemoryDatabaseImpl()

	@timeout(0.4)
	def test_level_3_case_01_ttl_returns_true(self):
		self.assertEqual(self.db.set_field_with_ttl(1, "a", "f1", "v1", 10), "true")

	@timeout(0.4)
	def test_level_3_case_02_get_field_before_expiry(self):
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 10)
		self.assertEqual(self.db.get_field(5, "a", "f1"), "v1")

	@timeout(0.4)
	def test_level_3_case_03_get_field_on_expiry_boundary(self):
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 10)
		# expires at 1 + 10 = 11 (exclusive)
		self.assertEqual(self.db.get_field(11, "a", "f1"), "")

	@timeout(0.4)
	def test_level_3_case_04_get_field_just_before_expiry(self):
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 10)
		self.assertEqual(self.db.get_field(10, "a", "f1"), "v1")

	@timeout(0.4)
	def test_level_3_case_05_plain_set_is_permanent(self):
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 10)
		self.db.set_field(2, "a", "f1", "v2")
		self.assertEqual(self.db.get_field(100, "a", "f1"), "v2")

	@timeout(0.4)
	def test_level_3_case_06_get_record_ignores_expired(self):
		self.db.set_field(1, "a", "perm", "p")
		self.db.set_field_with_ttl(1, "a", "temp", "t", 5)
		self.assertEqual(self.db.get_record(10, "a"), "perm=p")

	@timeout(0.4)
	def test_level_3_case_07_record_gone_when_all_expired(self):
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 5)
		self.assertEqual(self.db.get_record(10, "a"), "")

	@timeout(0.4)
	def test_level_3_case_08_scan_prefix_ignores_expired(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field_with_ttl(1, "a", "f2", "2", 5)
		self.assertEqual(self.db.scan_prefix(10, "a", "f"), "f1=1")

	@timeout(0.4)
	def test_level_3_case_09_top_n_keys_ignores_expired(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field_with_ttl(1, "a", "f2", "2", 5)
		self.db.set_field(1, "b", "f1", "1")
		# at t=10 a has 1 live field, b has 1; tie -> a, b
		self.assertEqual(self.db.top_n_keys(10, 2), "a(1), b(1)")

	@timeout(0.4)
	def test_level_3_case_10_top_n_keys_drops_fully_expired_key(self):
		self.db.set_field_with_ttl(1, "a", "f1", "1", 5)
		self.db.set_field(1, "b", "f1", "1")
		self.assertEqual(self.db.top_n_keys(10, 5), "b(1)")

	@timeout(0.4)
	def test_level_3_case_11_delete_expired_field_returns_false(self):
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 5)
		self.assertEqual(self.db.delete_field(10, "a", "f1"), "false")


if __name__ == "__main__":
	unittest.main()
