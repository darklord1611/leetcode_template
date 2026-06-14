import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for Cache System - Basic Cache Operations

	Tests cover: PUT, GET, DELETE, EXISTS
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_1_case_01_put_returns_true(self):
		self.assertEqual(self.cache.put(1, "a", "1"), "true")

	@timeout(0.4)
	def test_level_1_case_02_get_existing(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.get(2, "a"), "1")

	@timeout(0.4)
	def test_level_1_case_03_get_missing_returns_empty(self):
		self.assertEqual(self.cache.get(1, "missing"), "")

	@timeout(0.4)
	def test_level_1_case_04_put_overwrites(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.put(2, "a", "2"), "true")
		self.assertEqual(self.cache.get(3, "a"), "2")

	@timeout(0.4)
	def test_level_1_case_05_delete_existing(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.delete(2, "a"), "true")
		self.assertEqual(self.cache.get(3, "a"), "")

	@timeout(0.4)
	def test_level_1_case_06_delete_missing(self):
		self.assertEqual(self.cache.delete(1, "missing"), "false")

	@timeout(0.4)
	def test_level_1_case_07_exists_true(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.exists(2, "a"), "true")

	@timeout(0.4)
	def test_level_1_case_08_exists_false(self):
		self.assertEqual(self.cache.exists(1, "a"), "false")

	@timeout(0.4)
	def test_level_1_case_09_exists_false_after_delete(self):
		self.cache.put(1, "a", "1")
		self.cache.delete(2, "a")
		self.assertEqual(self.cache.exists(3, "a"), "false")

	@timeout(0.4)
	def test_level_1_case_10_multiple_keys_independent(self):
		self.cache.put(1, "a", "1")
		self.cache.put(2, "b", "2")
		self.assertEqual(self.cache.get(3, "a"), "1")
		self.assertEqual(self.cache.get(4, "b"), "2")


if __name__ == "__main__":
	unittest.main()
