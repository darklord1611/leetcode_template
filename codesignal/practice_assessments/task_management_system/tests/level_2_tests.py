import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from task_management_system_impl import TaskManagementSystemImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for Task Management System - Queries

	Tests cover: get_tasks_by_status, top_priority_tasks
	"""

	failureException = Exception

	def setUp(self):
		self.tms = TaskManagementSystemImpl()

	@timeout(0.4)
	def test_level_2_case_01_by_status_basic(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.assertEqual(self.tms.get_tasks_by_status(3, "open"), "t1, t2")

	@timeout(0.4)
	def test_level_2_case_02_by_status_none(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.get_tasks_by_status(2, "done"), "")

	@timeout(0.4)
	def test_level_2_case_03_by_status_filters(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.update_status(3, "t2", "done")
		self.assertEqual(self.tms.get_tasks_by_status(4, "open"), "t1")
		self.assertEqual(self.tms.get_tasks_by_status(5, "done"), "t2")

	@timeout(0.4)
	def test_level_2_case_04_by_status_priority_order(self):
		self.tms.create_task(1, "t1", 2)
		self.tms.create_task(2, "t2", 9)
		self.tms.create_task(3, "t3", 5)
		self.assertEqual(self.tms.get_tasks_by_status(4, "open"), "t2, t3, t1")

	@timeout(0.4)
	def test_level_2_case_05_by_status_tie_break(self):
		self.tms.create_task(1, "tb", 5)
		self.tms.create_task(2, "ta", 5)
		self.assertEqual(self.tms.get_tasks_by_status(3, "open"), "ta, tb")

	@timeout(0.4)
	def test_level_2_case_06_top_priority_basic(self):
		self.tms.create_task(1, "t1", 2)
		self.tms.create_task(2, "t2", 9)
		self.tms.create_task(3, "t3", 5)
		self.assertEqual(self.tms.top_priority_tasks(4, 2), "t2, t3")

	@timeout(0.4)
	def test_level_2_case_07_top_priority_more_than_exist(self):
		self.tms.create_task(1, "t1", 2)
		self.tms.create_task(2, "t2", 9)
		self.assertEqual(self.tms.top_priority_tasks(3, 5), "t2, t1")

	@timeout(0.4)
	def test_level_2_case_08_top_priority_empty(self):
		self.assertEqual(self.tms.top_priority_tasks(1, 3), "")

	@timeout(0.4)
	def test_level_2_case_09_top_priority_includes_done(self):
		self.tms.create_task(1, "t1", 5)
		self.tms.create_task(2, "t2", 3)
		self.tms.update_status(3, "t1", "done")
		self.assertEqual(self.tms.top_priority_tasks(4, 2), "t1, t2")

	@timeout(0.4)
	def test_level_2_case_10_top_priority_tie_break(self):
		self.tms.create_task(1, "tz", 5)
		self.tms.create_task(2, "ta", 5)
		self.tms.create_task(3, "tm", 5)
		self.assertEqual(self.tms.top_priority_tasks(4, 2), "ta, tm")


if __name__ == "__main__":
	unittest.main()
