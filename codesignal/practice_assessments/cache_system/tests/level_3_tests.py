import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for Cache System - TTL & Expiration

	Tests cover: PUT_WITH_TTL and expiry-aware reads (GET/EXISTS).
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_3_case_01_put_with_ttl_returns_true(self):
		self.assertEqual(self.cache.put_with_ttl(10, "a", "1", 5), "true")

	@timeout(0.4)
	def test_level_3_case_02_get_before_expiry(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.assertEqual(self.cache.get(12, "a"), "1")

	@timeout(0.4)
	def test_level_3_case_03_get_at_expiry_boundary(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.assertEqual(self.cache.get(15, "a"), "")

	@timeout(0.4)
	def test_level_3_case_04_get_after_expiry(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.assertEqual(self.cache.get(99, "a"), "")

	@timeout(0.4)
	def test_level_3_case_05_exists_respects_expiry(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.assertEqual(self.cache.exists(14, "a"), "true")
		self.assertEqual(self.cache.exists(15, "a"), "false")

	@timeout(0.4)
	def test_level_3_case_06_plain_put_never_expires(self):
		self.cache.put(10, "a", "1")
		self.assertEqual(self.cache.get(1000, "a"), "1")

	@timeout(0.4)
	def test_level_3_case_07_overwrite_with_ttl_then_plain(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.cache.put(11, "a", "2")
		# Plain overwrite clears the TTL, so the value survives past 15.
		self.assertEqual(self.cache.get(20, "a"), "2")

	@timeout(0.4)
	def test_level_3_case_08_overwrite_plain_then_ttl(self):
		self.cache.put(10, "a", "1")
		self.cache.put_with_ttl(11, "a", "2", 4)
		# Now a expires at 15.
		self.assertEqual(self.cache.get(14, "a"), "2")
		self.assertEqual(self.cache.get(15, "a"), "")

	@timeout(0.4)
	def test_level_3_case_09_expired_does_not_count_toward_capacity(self):
		self.cache.set_capacity(1, 2)
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.cache.put(10, "b", "2")
		# At t=20, a has expired and should be purged instead of evicting b
		self.cache.put(20, "c", "3")
		self.assertEqual(self.cache.exists(21, "a"), "false")
		self.assertEqual(self.cache.exists(22, "b"), "true")
		self.assertEqual(self.cache.exists(23, "c"), "true")

	@timeout(0.4)
	def test_level_3_case_10_expired_entry_frees_capacity_slot(self):
		# Capacity 1; once a expires, b can be inserted without evicting a live entry.
		self.cache.set_capacity(1, 1)
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.cache.put(20, "b", "2")
		self.assertEqual(self.cache.get(21, "a"), "")
		self.assertEqual(self.cache.get(22, "b"), "2")


if __name__ == "__main__":
	unittest.main()
