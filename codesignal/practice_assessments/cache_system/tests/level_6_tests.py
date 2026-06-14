import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level6Tests(unittest.TestCase):
	"""
	Level 6 tests for Cache System - Statistics & Analytics

	Tests cover: GET_STATS and TOP_ACCESSED.
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_6_case_01_stats_empty(self):
		self.assertEqual(self.cache.get_stats(1), "hits=0,misses=0,hit_ratio=0.00")

	@timeout(0.4)
	def test_level_6_case_02_stats_hits_and_misses(self):
		self.cache.put(1, "a", "1")
		self.cache.get(2, "a")        # hit
		self.cache.get(3, "missing")  # miss
		self.cache.get(4, "a")        # hit
		self.assertEqual(self.cache.get_stats(5), "hits=2,misses=1,hit_ratio=0.67")

	@timeout(0.4)
	def test_level_6_case_03_stats_all_hits(self):
		self.cache.put(1, "a", "1")
		self.cache.get(2, "a")
		self.cache.get(3, "a")
		self.assertEqual(self.cache.get_stats(4), "hits=2,misses=0,hit_ratio=1.00")

	@timeout(0.4)
	def test_level_6_case_04_expired_get_is_miss(self):
		self.cache.put_with_ttl(10, "a", "1", 5)
		self.cache.get(20, "a")  # expired -> miss
		self.assertEqual(self.cache.get_stats(21), "hits=0,misses=1,hit_ratio=0.00")

	@timeout(0.4)
	def test_level_6_case_05_stats_all_misses(self):
		self.cache.get(1, "x")
		self.cache.get(2, "y")
		self.assertEqual(self.cache.get_stats(3), "hits=0,misses=2,hit_ratio=0.00")

	@timeout(0.4)
	def test_level_6_case_06_top_accessed(self):
		self.cache.put(1, "a", "1")
		self.cache.put(2, "b", "2")
		self.cache.put(3, "c", "3")
		self.cache.get(4, "a")
		self.cache.get(5, "a")
		self.cache.get(6, "a")
		self.cache.get(7, "c")
		self.cache.get(8, "c")
		self.cache.get(9, "b")
		self.assertEqual(self.cache.top_accessed(10, 2), "a,c")

	@timeout(0.4)
	def test_level_6_case_07_top_accessed_tie_breaks_by_mru(self):
		self.cache.put(1, "a", "1")
		self.cache.put(2, "b", "2")
		self.cache.get(3, "a")  # a: 1 hit
		self.cache.get(4, "b")  # b: 1 hit, more recently used
		self.assertEqual(self.cache.top_accessed(5, 2), "b,a")

	@timeout(0.4)
	def test_level_6_case_08_top_accessed_empty(self):
		self.assertEqual(self.cache.top_accessed(1, 3), "")

	@timeout(0.4)
	def test_level_6_case_09_top_accessed_limit(self):
		self.cache.put(1, "a", "1")
		self.cache.put(2, "b", "2")
		self.cache.put(3, "c", "3")
		self.cache.get(4, "a")
		self.cache.get(5, "a")
		self.cache.get(6, "b")
		self.assertEqual(self.cache.top_accessed(7, 1), "a")

	@timeout(0.4)
	def test_level_6_case_10_top_accessed_excludes_evicted(self):
		# Only currently-present keys are reported by top_accessed.
		self.cache.set_capacity(1, 2)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.get(4, "a")
		self.cache.get(5, "a")  # a has the most hits...
		self.cache.put(6, "c", "3")  # ...but evicts b (LRU), a stays
		self.cache.get(7, "c")
		self.assertEqual(self.cache.top_accessed(8, 3), "a,c")


if __name__ == "__main__":
	unittest.main()
