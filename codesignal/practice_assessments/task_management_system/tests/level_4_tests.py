import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from task_management_system_impl import TaskManagementSystemImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for Task Management System - Analytics

	Tests cover: get_blocked_tasks, get_critical_path
	"""

	failureException = Exception

	def setUp(self):
		self.tms = TaskManagementSystemImpl()

	@timeout(0.4)
	def test_level_4_case_01_blocked_basic(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		self.assertEqual(self.tms.get_blocked_tasks(4), "t1")

	@timeout(0.4)
	def test_level_4_case_02_blocked_none(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.assertEqual(self.tms.get_blocked_tasks(3), "")

	@timeout(0.4)
	def test_level_4_case_03_blocked_clears_when_dep_done(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		self.tms.update_status(4, "t2", "done")
		self.assertEqual(self.tms.get_blocked_tasks(5), "")

	@timeout(0.4)
	def test_level_4_case_04_blocked_excludes_done(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		# even though t1's dependency t2 is not done, t1 itself is done -> excluded
		self.tms.update_status(4, "t1", "open")
		self.assertEqual(self.tms.get_blocked_tasks(5), "t1")

	@timeout(0.4)
	def test_level_4_case_05_blocked_priority_order(self):
		self.tms.create_task(1, "base", 1)
		self.tms.create_task(2, "low", 2)
		self.tms.create_task(3, "high", 9)
		self.tms.add_dependency(4, "low", "base")
		self.tms.add_dependency(5, "high", "base")
		self.assertEqual(self.tms.get_blocked_tasks(6), "high, low")

	@timeout(0.4)
	def test_level_4_case_06_critical_path_chain(self):
		self.tms.create_task(1, "a", 1)
		self.tms.create_task(2, "b", 1)
		self.tms.create_task(3, "c", 1)
		# c depends on b, b depends on a
		self.tms.add_dependency(4, "b", "a")
		self.tms.add_dependency(5, "c", "b")
		self.assertEqual(self.tms.get_critical_path(6), "a,b,c")

	@timeout(0.4)
	def test_level_4_case_07_critical_path_none(self):
		self.tms.create_task(1, "a", 1)
		self.tms.create_task(2, "b", 1)
		self.assertEqual(self.tms.get_critical_path(3), "")

	@timeout(0.4)
	def test_level_4_case_08_critical_path_single_edge(self):
		self.tms.create_task(1, "a", 1)
		self.tms.create_task(2, "b", 1)
		self.tms.add_dependency(3, "b", "a")
		self.assertEqual(self.tms.get_critical_path(4), "a,b")

	@timeout(0.4)
	def test_level_4_case_09_critical_path_tie_lexicographic(self):
		# Two independent chains of equal length: x->y and a->b
		self.tms.create_task(1, "x", 1)
		self.tms.create_task(2, "y", 1)
		self.tms.create_task(3, "a", 1)
		self.tms.create_task(4, "b", 1)
		self.tms.add_dependency(5, "y", "x")
		self.tms.add_dependency(6, "b", "a")
		# ["a","b"] < ["x","y"] lexicographically
		self.assertEqual(self.tms.get_critical_path(7), "a,b")

	@timeout(0.4)
	def test_level_4_case_10_critical_path_longest_wins(self):
		self.tms.create_task(1, "a", 1)
		self.tms.create_task(2, "b", 1)
		self.tms.create_task(3, "c", 1)
		self.tms.create_task(4, "p", 1)
		self.tms.create_task(5, "q", 1)
		# chain a->b->c (length 3) vs p->q (length 2)
		self.tms.add_dependency(6, "b", "a")
		self.tms.add_dependency(7, "c", "b")
		self.tms.add_dependency(8, "q", "p")
		self.assertEqual(self.tms.get_critical_path(9), "a,b,c")

	@timeout(0.4)
	def test_level_4_case_11_critical_path_branching(self):
		# d depends on both b and c; b depends on a; c depends on a
		self.tms.create_task(1, "a", 1)
		self.tms.create_task(2, "b", 1)
		self.tms.create_task(3, "c", 1)
		self.tms.create_task(4, "d", 1)
		self.tms.add_dependency(5, "b", "a")
		self.tms.add_dependency(6, "c", "a")
		self.tms.add_dependency(7, "d", "b")
		self.tms.add_dependency(8, "d", "c")
		# longest chains: a,b,d and a,c,d (both length 3); smallest is a,b,d
		self.assertEqual(self.tms.get_critical_path(9), "a,b,d")


if __name__ == "__main__":
	unittest.main()
