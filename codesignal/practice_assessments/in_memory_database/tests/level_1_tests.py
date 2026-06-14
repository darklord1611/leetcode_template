import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from in_memory_database_impl import InMemoryDatabaseImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for In-Memory Database - Field Operations

	Tests cover: set_field, get_field, delete_field, get_record
	"""

	failureException = Exception

	def setUp(self):
		self.db = InMemoryDatabaseImpl()

	@timeout(0.4)
	def test_level_1_case_01_set_field_returns_true(self):
		self.assertEqual(self.db.set_field(1, "a", "f1", "v1"), "true")

	@timeout(0.4)
	def test_level_1_case_02_get_field(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.assertEqual(self.db.get_field(2, "a", "f1"), "v1")

	@timeout(0.4)
	def test_level_1_case_03_get_missing_key(self):
		self.assertEqual(self.db.get_field(1, "missing", "f1"), "")

	@timeout(0.4)
	def test_level_1_case_04_get_missing_field(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.assertEqual(self.db.get_field(2, "a", "f2"), "")

	@timeout(0.4)
	def test_level_1_case_05_overwrite_field(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.db.set_field(2, "a", "f1", "v2")
		self.assertEqual(self.db.get_field(3, "a", "f1"), "v2")

	@timeout(0.4)
	def test_level_1_case_06_delete_field(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.assertEqual(self.db.delete_field(2, "a", "f1"), "true")
		self.assertEqual(self.db.get_field(3, "a", "f1"), "")

	@timeout(0.4)
	def test_level_1_case_07_delete_missing_field(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.assertEqual(self.db.delete_field(2, "a", "nope"), "false")

	@timeout(0.4)
	def test_level_1_case_08_delete_missing_key(self):
		self.assertEqual(self.db.delete_field(1, "missing", "f1"), "false")

	@timeout(0.4)
	def test_level_1_case_09_get_record_sorted(self):
		self.db.set_field(1, "a", "b", "2")
		self.db.set_field(2, "a", "a", "1")
		self.db.set_field(3, "a", "c", "3")
		self.assertEqual(self.db.get_record(4, "a"), "a=1, b=2, c=3")

	@timeout(0.4)
	def test_level_1_case_10_get_record_missing_key(self):
		self.assertEqual(self.db.get_record(1, "missing"), "")

	@timeout(0.4)
	def test_level_1_case_11_record_removed_when_empty(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.db.delete_field(2, "a", "f1")
		self.assertEqual(self.db.get_record(3, "a"), "")


if __name__ == "__main__":
	unittest.main()
