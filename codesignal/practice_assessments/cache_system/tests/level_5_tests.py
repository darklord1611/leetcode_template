import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level5Tests(unittest.TestCase):
	"""
	Level 5 tests for Cache System - Pinning & Eviction Priority

	Tests cover: PIN, UNPIN, eviction skipping pinned entries, TTL + pin.
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_5_case_01_pin_existing(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.pin(2, "a"), "true")

	@timeout(0.4)
	def test_level_5_case_02_pin_absent(self):
		self.assertEqual(self.cache.pin(1, "missing"), "false")

	@timeout(0.4)
	def test_level_5_case_03_unpin_existing(self):
		self.cache.put(1, "a", "1")
		self.cache.pin(2, "a")
		self.assertEqual(self.cache.unpin(3, "a"), "true")

	@timeout(0.4)
	def test_level_5_case_04_unpin_absent(self):
		self.assertEqual(self.cache.unpin(1, "missing"), "false")

	@timeout(0.4)
	def test_level_5_case_05_pinned_not_evicted(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.pin(4, "a")
		# a is LRU but pinned, so b should be evicted instead
		self.cache.put(5, "c", "3")
		self.assertEqual(self.cache.exists(6, "a"), "true")
		self.assertEqual(self.cache.exists(7, "b"), "false")
		self.assertEqual(self.cache.exists(8, "c"), "true")

	@timeout(0.4)
	def test_level_5_case_06_all_pinned_full_rejects_new(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.pin(4, "a")
		self.cache.pin(5, "b")
		self.assertEqual(self.cache.put(6, "c", "3"), "false")
		self.assertEqual(self.cache.exists(7, "c"), "false")

	@timeout(0.4)
	def test_level_5_case_07_all_pinned_overwrite_allowed(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.pin(4, "a")
		self.cache.pin(5, "b")
		self.assertEqual(self.cache.put(6, "a", "11"), "true")
		self.assertEqual(self.cache.get(7, "a"), "11")

	@timeout(0.4)
	def test_level_5_case_08_pinned_ignores_ttl(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.cache.pin(10, "a")
		self.assertEqual(self.cache.get(20, "a"), "1")

	@timeout(0.4)
	def test_level_5_case_09_unpin_restores_expiry(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.cache.pin(10, "a")
		self.assertEqual(self.cache.get(20, "a"), "1")
		self.cache.unpin(20, "a")
		# TTL (expired at 15) applies again once unpinned
		self.assertEqual(self.cache.get(21, "a"), "")

	@timeout(0.4)
	def test_level_5_case_10_unpin_then_evictable(self):
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.pin(4, "a")
		self.cache.unpin(5, "a")
		# After unpin, a is LRU again and can be evicted
		self.cache.put(6, "c", "3")
		self.assertEqual(self.cache.exists(7, "a"), "false")
		self.assertEqual(self.cache.exists(8, "b"), "true")
		self.assertEqual(self.cache.exists(9, "c"), "true")


if __name__ == "__main__":
	unittest.main()
