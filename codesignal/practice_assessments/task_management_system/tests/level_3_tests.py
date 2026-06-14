import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from task_management_system_impl import TaskManagementSystemImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for Task Management System - Dependencies & Blocking

	Tests cover: add_dependency, update_status (updated), delete_task (updated),
	get_available_tasks
	"""

	failureException = Exception

	def setUp(self):
		self.tms = TaskManagementSystemImpl()

	@timeout(0.4)
	def test_level_3_case_01_add_dependency(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.assertEqual(self.tms.add_dependency(3, "t1", "t2"), "true")

	@timeout(0.4)
	def test_level_3_case_02_add_dependency_missing(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.add_dependency(2, "t1", "missing"), "false")
		self.assertEqual(self.tms.add_dependency(3, "missing", "t1"), "false")

	@timeout(0.4)
	def test_level_3_case_03_add_dependency_cycle(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.create_task(3, "t3", 1)
		self.assertEqual(self.tms.add_dependency(4, "t1", "t2"), "true")
		self.assertEqual(self.tms.add_dependency(5, "t2", "t3"), "true")
		# t3 -> t1 would close the cycle t1 -> t2 -> t3 -> t1
		self.assertEqual(self.tms.add_dependency(6, "t3", "t1"), "false")

	@timeout(0.4)
	def test_level_3_case_04_add_dependency_self_cycle(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.add_dependency(2, "t1", "t1"), "false")

	@timeout(0.4)
	def test_level_3_case_05_status_blocked(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		# t2 not done, so t1 cannot advance
		self.assertEqual(self.tms.update_status(4, "t1", "in_progress"), "")
		self.assertEqual(self.tms.get_task(5, "t1"), "t1(5,open)")

	@timeout(0.4)
	def test_level_3_case_06_status_unblocked_after_dep_done(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		self.assertEqual(self.tms.update_status(4, "t2", "done"), "true")
		self.assertEqual(self.tms.update_status(5, "t1", "in_progress"), "true")
		self.assertEqual(self.tms.get_task(6, "t1"), "t1(5,in_progress)")

	@timeout(0.4)
	def test_level_3_case_07_status_open_always_allowed(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		self.assertEqual(self.tms.update_status(4, "t1", "open"), "true")

	@timeout(0.4)
	def test_level_3_case_08_delete_clears_dependency(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		# deleting t2 removes it as a dependency of t1, unblocking it
		self.assertEqual(self.tms.delete_task(4, "t2"), "true")
		self.assertEqual(self.tms.update_status(5, "t1", "done"), "true")

	@timeout(0.4)
	def test_level_3_case_09_available_tasks(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.create_task(3, "t3", 9)
		self.tms.add_dependency(4, "t1", "t2")
		# t1 blocked by t2; t2 and t3 have no deps and are not done
		self.assertEqual(self.tms.get_available_tasks(5), "t3, t2")

	@timeout(0.4)
	def test_level_3_case_10_available_excludes_done(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.add_dependency(3, "t1", "t2")
		self.tms.update_status(4, "t2", "done")
		# t2 is done (excluded); t1 now available
		self.assertEqual(self.tms.get_available_tasks(5), "t1")

	@timeout(0.4)
	def test_level_3_case_11_available_none(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.update_status(2, "t1", "done")
		self.assertEqual(self.tms.get_available_tasks(3), "")


if __name__ == "__main__":
	unittest.main()
