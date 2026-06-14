import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for Cache System - Capacity & LRU Eviction

	Tests cover: SET_CAPACITY, and updated PUT/GET (recency + LRU eviction).
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_2_case_01_set_capacity_no_eviction(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.set_capacity(2, 3), "0")

	@timeout(0.4)
	def test_level_2_case_02_set_capacity_shrink_evicts_lru(self):
		self.cache.put(1, "a", "1")
		self.cache.put(2, "b", "2")
		self.cache.put(3, "c", "3")
		self.assertEqual(self.cache.set_capacity(4, 2), "1")
		self.assertEqual(self.cache.exists(5, "a"), "false")
		self.assertEqual(self.cache.exists(6, "b"), "true")
		self.assertEqual(self.cache.exists(7, "c"), "true")

	@timeout(0.4)
	def test_level_2_case_03_put_evicts_lru_when_full(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.put(4, "c", "3")
		self.assertEqual(self.cache.get(5, "a"), "")
		self.assertEqual(self.cache.get(6, "b"), "2")
		self.assertEqual(self.cache.get(7, "c"), "3")

	@timeout(0.4)
	def test_level_2_case_04_get_marks_mru(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		# Touch a so b becomes LRU
		self.assertEqual(self.cache.get(4, "a"), "1")
		self.cache.put(5, "c", "3")
		self.assertEqual(self.cache.exists(6, "a"), "true")
		self.assertEqual(self.cache.exists(7, "b"), "false")
		self.assertEqual(self.cache.exists(8, "c"), "true")

	@timeout(0.4)
	def test_level_2_case_05_overwrite_marks_mru(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		# Overwrite a so it becomes MRU; b is now LRU
		self.cache.put(4, "a", "11")
		self.cache.put(5, "c", "3")
		self.assertEqual(self.cache.exists(6, "a"), "true")
		self.assertEqual(self.cache.exists(7, "b"), "false")
		self.assertEqual(self.cache.exists(8, "c"), "true")

	@timeout(0.4)
	def test_level_2_case_06_overwrite_does_not_grow_size(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.put(4, "b", "22")
		self.assertEqual(self.cache.exists(5, "a"), "true")
		self.assertEqual(self.cache.get(6, "b"), "22")

	@timeout(0.4)
	def test_level_2_case_07_lru_victim_is_oldest_untouched(self):
		# a is the least-recently-used; inserting a third key evicts a.
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.put(4, "c", "3")
		self.assertEqual(self.cache.exists(5, "a"), "false")
		self.assertEqual(self.cache.exists(6, "b"), "true")
		self.assertEqual(self.cache.exists(7, "c"), "true")

	@timeout(0.4)
	def test_level_2_case_08_get_refreshes_lru_victim(self):
		# After touching a, b becomes the LRU victim of the next insert.
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.get(4, "a")
		self.cache.put(5, "c", "3")
		self.assertEqual(self.cache.exists(6, "b"), "false")
		self.assertEqual(self.cache.exists(7, "a"), "true")
		self.assertEqual(self.cache.exists(8, "c"), "true")

	@timeout(0.4)
	def test_level_2_case_09_zero_capacity_evicts_all(self):
		self.cache.put(1, "a", "1")
		self.cache.put(2, "b", "2")
		self.assertEqual(self.cache.set_capacity(3, 0), "2")
		self.assertEqual(self.cache.exists(4, "a"), "false")
		self.assertEqual(self.cache.exists(5, "b"), "false")

	@timeout(0.4)
	def test_level_2_case_10_exists_does_not_change_recency(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		# exists must not refresh a
		self.cache.exists(4, "a")
		self.cache.put(5, "c", "3")
		self.assertEqual(self.cache.exists(6, "a"), "false")
		self.assertEqual(self.cache.exists(7, "b"), "true")


if __name__ == "__main__":
	unittest.main()
