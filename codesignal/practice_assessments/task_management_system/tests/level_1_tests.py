import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from task_management_system_impl import TaskManagementSystemImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for Task Management System - Basic CRUD

	Tests cover: create_task, update_status, update_priority, get_task, delete_task
	"""

	failureException = Exception

	def setUp(self):
		self.tms = TaskManagementSystemImpl()

	@timeout(0.4)
	def test_level_1_case_01_create_task(self):
		self.assertEqual(self.tms.create_task(1, "t1", 5), "true")

	@timeout(0.4)
	def test_level_1_case_02_create_duplicate(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.create_task(2, "t1", 9), "false")

	@timeout(0.4)
	def test_level_1_case_03_get_task(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.get_task(2, "t1"), "t1(5,open)")

	@timeout(0.4)
	def test_level_1_case_04_get_missing(self):
		self.assertEqual(self.tms.get_task(1, "missing"), "")

	@timeout(0.4)
	def test_level_1_case_05_update_status(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.update_status(2, "t1", "in_progress"), "true")
		self.assertEqual(self.tms.get_task(3, "t1"), "t1(5,in_progress)")

	@timeout(0.4)
	def test_level_1_case_06_update_status_missing(self):
		self.assertEqual(self.tms.update_status(1, "missing", "done"), "")

	@timeout(0.4)
	def test_level_1_case_07_update_priority(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.update_priority(2, "t1", 8), "true")
		self.assertEqual(self.tms.get_task(3, "t1"), "t1(8,open)")

	@timeout(0.4)
	def test_level_1_case_08_update_priority_missing(self):
		self.assertEqual(self.tms.update_priority(1, "missing", 3), "")

	@timeout(0.4)
	def test_level_1_case_09_delete_task(self):
		self.tms.create_task(1, "t1", 5)
		self.assertEqual(self.tms.delete_task(2, "t1"), "true")
		self.assertEqual(self.tms.get_task(3, "t1"), "")

	@timeout(0.4)
	def test_level_1_case_10_delete_missing(self):
		self.assertEqual(self.tms.delete_task(1, "missing"), "false")

	@timeout(0.4)
	def test_level_1_case_11_full_scenario(self):
		self.assertEqual(self.tms.create_task(1, "t1", 5), "true")
		self.assertEqual(self.tms.create_task(2, "t2", 3), "true")
		self.assertEqual(self.tms.create_task(3, "t1", 1), "false")
		self.assertEqual(self.tms.update_status(4, "t1", "done"), "true")
		self.assertEqual(self.tms.update_priority(5, "t2", 9), "true")
		self.assertEqual(self.tms.get_task(6, "t1"), "t1(5,done)")
		self.assertEqual(self.tms.get_task(7, "t2"), "t2(9,open)")
		self.assertEqual(self.tms.delete_task(8, "t2"), "true")
		self.assertEqual(self.tms.delete_task(9, "t2"), "false")


if __name__ == "__main__":
	unittest.main()
