import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level7Tests(unittest.TestCase):
	"""
	Level 7 tests for Cache System - Namespaces

	Tests cover: PUT_IN_NAMESPACE, GET_IN_NAMESPACE, SET_NAMESPACE_CAPACITY.
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_7_case_01_put_get_namespace(self):
		self.assertEqual(self.cache.put_in_namespace(1, "ns1", "a", "1"), "true")
		self.assertEqual(self.cache.get_in_namespace(2, "ns1", "a"), "1")

	@timeout(0.4)
	def test_level_7_case_02_namespace_isolation(self):
		self.cache.put_in_namespace(1, "ns1", "a", "1")
		self.assertEqual(self.cache.get_in_namespace(2, "ns2", "a"), "")

	@timeout(0.4)
	def test_level_7_case_03_namespace_not_visible_in_default(self):
		self.cache.put_in_namespace(1, "ns1", "a", "1")
		self.assertEqual(self.cache.get(2, "a"), "")

	@timeout(0.4)
	def test_level_7_case_04_default_namespace_matches_put(self):
		self.cache.put(1, "a", "1")
		self.assertEqual(self.cache.get_in_namespace(2, "", "a"), "1")

	@timeout(0.4)
	def test_level_7_case_05_same_key_different_namespaces(self):
		self.cache.put_in_namespace(1, "ns1", "k", "v1")
		self.cache.put_in_namespace(2, "ns2", "k", "v2")
		self.assertEqual(self.cache.get_in_namespace(3, "ns1", "k"), "v1")
		self.assertEqual(self.cache.get_in_namespace(4, "ns2", "k"), "v2")

	@timeout(0.4)
	def test_level_7_case_06_namespace_independent_capacity(self):
		self.cache.set_namespace_capacity(1, "ns1", 2)
		self.cache.put_in_namespace(2, "ns1", "a", "1")
		self.cache.put_in_namespace(3, "ns1", "b", "2")
		self.cache.put_in_namespace(4, "ns1", "c", "3")
		self.assertEqual(self.cache.get_in_namespace(5, "ns1", "a"), "")
		self.assertEqual(self.cache.get_in_namespace(6, "ns1", "b"), "2")
		self.assertEqual(self.cache.get_in_namespace(7, "ns1", "c"), "3")

	@timeout(0.4)
	def test_level_7_case_07_namespace_capacity_does_not_affect_default(self):
		self.cache.set_namespace_capacity(1, "ns1", 1)
		self.cache.put(2, "a", "1")
		self.cache.put(3, "b", "2")
		self.cache.put_in_namespace(4, "ns1", "x", "9")
		self.cache.put_in_namespace(5, "ns1", "y", "8")
		self.assertEqual(self.cache.get(6, "a"), "1")
		self.assertEqual(self.cache.get(7, "b"), "2")
		self.assertEqual(self.cache.get_in_namespace(8, "ns1", "x"), "")
		self.assertEqual(self.cache.get_in_namespace(9, "ns1", "y"), "8")

	@timeout(0.4)
	def test_level_7_case_08_set_namespace_capacity_returns_evicted(self):
		self.cache.put_in_namespace(1, "ns1", "a", "1")
		self.cache.put_in_namespace(2, "ns1", "b", "2")
		self.cache.put_in_namespace(3, "ns1", "c", "3")
		self.assertEqual(self.cache.set_namespace_capacity(4, "ns1", 1), "2")

	@timeout(0.4)
	def test_level_7_case_09_namespace_get_recency(self):
		# get_in_namespace refreshes recency within that namespace.
		self.cache.set_namespace_capacity(1, "ns1", 2)
		self.cache.put_in_namespace(2, "ns1", "a", "1")
		self.cache.put_in_namespace(3, "ns1", "b", "2")
		self.cache.get_in_namespace(4, "ns1", "a")  # a now MRU, b is LRU
		self.cache.put_in_namespace(5, "ns1", "c", "3")
		self.assertEqual(self.cache.get_in_namespace(6, "ns1", "b"), "")
		self.assertEqual(self.cache.get_in_namespace(7, "ns1", "a"), "1")

	@timeout(0.4)
	def test_level_7_case_10_set_namespace_capacity_isolated(self):
		# Shrinking ns1 must not evict from ns2.
		self.cache.put_in_namespace(1, "ns1", "a", "1")
		self.cache.put_in_namespace(2, "ns1", "b", "2")
		self.cache.put_in_namespace(3, "ns2", "a", "9")
		self.cache.put_in_namespace(4, "ns2", "b", "8")
		self.assertEqual(self.cache.set_namespace_capacity(5, "ns1", 1), "1")
		self.assertEqual(self.cache.get_in_namespace(6, "ns2", "a"), "9")
		self.assertEqual(self.cache.get_in_namespace(7, "ns2", "b"), "8")


if __name__ == "__main__":
	unittest.main()
