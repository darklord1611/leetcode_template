import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from in_memory_database_impl import InMemoryDatabaseImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for In-Memory Database - Scans & Ranking

	Tests cover: scan_prefix, top_n_keys
	"""

	failureException = Exception

	def setUp(self):
		self.db = InMemoryDatabaseImpl()

	@timeout(0.4)
	def test_level_2_case_01_scan_prefix_basic(self):
		self.db.set_field(1, "a", "field1", "1")
		self.db.set_field(2, "a", "field2", "2")
		self.db.set_field(3, "a", "other", "3")
		self.assertEqual(self.db.scan_prefix(4, "a", "field"), "field1=1, field2=2")

	@timeout(0.4)
	def test_level_2_case_02_scan_prefix_no_match(self):
		self.db.set_field(1, "a", "field1", "1")
		self.assertEqual(self.db.scan_prefix(2, "a", "zzz"), "")

	@timeout(0.4)
	def test_level_2_case_03_scan_prefix_missing_key(self):
		self.assertEqual(self.db.scan_prefix(1, "missing", "f"), "")

	@timeout(0.4)
	def test_level_2_case_04_scan_prefix_empty_prefix(self):
		self.db.set_field(1, "a", "b", "2")
		self.db.set_field(2, "a", "a", "1")
		self.assertEqual(self.db.scan_prefix(3, "a", ""), "a=1, b=2")

	@timeout(0.4)
	def test_level_2_case_05_scan_prefix_sorted(self):
		self.db.set_field(1, "a", "fb", "2")
		self.db.set_field(2, "a", "fa", "1")
		self.db.set_field(3, "a", "fc", "3")
		self.assertEqual(self.db.scan_prefix(4, "a", "f"), "fa=1, fb=2, fc=3")

	@timeout(0.4)
	def test_level_2_case_06_top_n_keys_basic(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field(2, "a", "f2", "2")
		self.db.set_field(3, "b", "f1", "1")
		self.assertEqual(self.db.top_n_keys(4, 2), "a(2), b(1)")

	@timeout(0.4)
	def test_level_2_case_07_top_n_keys_tie_break(self):
		self.db.set_field(1, "b", "f1", "1")
		self.db.set_field(2, "a", "f1", "1")
		self.db.set_field(3, "c", "f1", "1")
		self.assertEqual(self.db.top_n_keys(4, 3), "a(1), b(1), c(1)")

	@timeout(0.4)
	def test_level_2_case_08_top_n_keys_limit(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field(2, "b", "f1", "1")
		self.db.set_field(3, "c", "f1", "1")
		self.assertEqual(self.db.top_n_keys(4, 2), "a(1), b(1)")

	@timeout(0.4)
	def test_level_2_case_09_top_n_keys_more_than_exist(self):
		self.db.set_field(1, "a", "f1", "1")
		self.assertEqual(self.db.top_n_keys(2, 5), "a(1)")

	@timeout(0.4)
	def test_level_2_case_10_top_n_keys_empty(self):
		self.assertEqual(self.db.top_n_keys(1, 3), "")

	@timeout(0.4)
	def test_level_2_case_11_top_n_keys_reflects_delete(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field(2, "a", "f2", "2")
		self.db.set_field(3, "b", "f1", "1")
		self.db.delete_field(4, "a", "f2")
		self.assertEqual(self.db.top_n_keys(5, 2), "a(1), b(1)")


if __name__ == "__main__":
	unittest.main()
