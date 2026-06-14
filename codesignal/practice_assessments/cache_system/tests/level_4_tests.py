import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from cache_system_impl import CacheSystemImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for Cache System - Dependencies & Cascading Invalidation

	Tests cover: PUT_WITH_DEPS, INVALIDATE, and overwrite cascade
	(observed via GET/EXISTS).
	"""

	failureException = Exception

	def setUp(self):
		self.cache = CacheSystemImpl()

	@timeout(0.4)
	def test_level_4_case_01_put_with_deps_returns_true(self):
		self.cache.put(1, "a", "va")
		self.assertEqual(self.cache.put_with_deps(2, "b", "vb", ["a"]), "true")

	@timeout(0.4)
	def test_level_4_case_02_put_with_deps_value_readable(self):
		self.cache.put(1, "a", "va")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		self.assertEqual(self.cache.get(3, "b"), "vb")

	@timeout(0.4)
	def test_level_4_case_03_invalidate_cascade(self):
		self.cache.put(1, "a", "va")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		self.cache.put_with_deps(3, "c", "vc", ["b"])
		self.cache.put_with_deps(4, "d", "vd", ["a"])
		self.assertEqual(self.cache.invalidate(5, "a"), "4")
		self.assertEqual(self.cache.exists(6, "a"), "false")
		self.assertEqual(self.cache.exists(7, "b"), "false")
		self.assertEqual(self.cache.exists(8, "c"), "false")
		self.assertEqual(self.cache.exists(9, "d"), "false")

	@timeout(0.4)
	def test_level_4_case_04_invalidate_partial(self):
		self.cache.put(1, "a", "va")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		self.cache.put_with_deps(3, "c", "vc", ["b"])
		# Invalidating b removes b and c, but not a
		self.assertEqual(self.cache.invalidate(4, "b"), "2")
		self.assertEqual(self.cache.exists(5, "a"), "true")
		self.assertEqual(self.cache.exists(6, "b"), "false")
		self.assertEqual(self.cache.exists(7, "c"), "false")

	@timeout(0.4)
	def test_level_4_case_05_invalidate_absent(self):
		self.assertEqual(self.cache.invalidate(1, "missing"), "0")

	@timeout(0.4)
	def test_level_4_case_06_invalidate_independent_kept(self):
		self.cache.put(1, "a", "va")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		self.cache.put(3, "x", "vx")
		# x does not depend on a, so it survives a's invalidation.
		self.assertEqual(self.cache.invalidate(4, "a"), "2")
		self.assertEqual(self.cache.get(5, "x"), "vx")

	@timeout(0.4)
	def test_level_4_case_07_overwrite_invalidates_dependents(self):
		self.cache.put(1, "a", "v1")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		# Overwriting a makes b stale -> removed
		self.cache.put(3, "a", "v2")
		self.assertEqual(self.cache.get(4, "a"), "v2")
		self.assertEqual(self.cache.exists(5, "b"), "false")

	@timeout(0.4)
	def test_level_4_case_08_overwrite_keeps_unrelated_dependents(self):
		self.cache.put(1, "a", "va")
		self.cache.put(2, "z", "vz")
		self.cache.put_with_deps(3, "b", "vb", ["a"])
		self.cache.put_with_deps(4, "c", "vc", ["z"])
		# Overwriting a only invalidates b; c (depends on z) stays.
		self.cache.put(5, "a", "va2")
		self.assertEqual(self.cache.exists(6, "b"), "false")
		self.assertEqual(self.cache.get(7, "c"), "vc")

	@timeout(0.4)
	def test_level_4_case_09_transitive_overwrite_cascade(self):
		self.cache.put(1, "a", "va")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		self.cache.put_with_deps(3, "c", "vc", ["b"])
		# Overwriting a invalidates b, and transitively c
		self.cache.put(4, "a", "va2")
		self.assertEqual(self.cache.exists(5, "b"), "false")
		self.assertEqual(self.cache.exists(6, "c"), "false")

	@timeout(0.4)
	def test_level_4_case_10_multiple_dependents_cascade(self):
		self.cache.put(1, "a", "va")
		self.cache.put_with_deps(2, "b", "vb", ["a"])
		self.cache.put_with_deps(3, "c", "vc", ["a"])
		# Both direct dependents of a are removed on invalidate.
		self.assertEqual(self.cache.invalidate(4, "a"), "3")
		self.assertEqual(self.cache.exists(5, "b"), "false")
		self.assertEqual(self.cache.exists(6, "c"), "false")


if __name__ == "__main__":
	unittest.main()
