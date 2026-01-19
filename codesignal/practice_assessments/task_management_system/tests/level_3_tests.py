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
	Level 3 tests for Task Management System - Deadlines and Dependencies

	Tests cover: CREATE_TASK_WITH_DEADLINE, SET_DEADLINE, ADD_DEPENDENCY,
	             UPDATE_STATUS_WITH_CHECK, GET_OVERDUE_TASKS, GET_TASK_WITH_DETAILS,
	             GET_AVAILABLE_TASKS
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh TaskManagementSystem instance for each test."""
		self.tms = TaskManagementSystemImpl()

	@timeout(0.4)
	def test_level_3_case_01_create_task_with_deadline(self):
		"""Test creating a task with a deadline."""
		result = self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 5000)
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_3_case_02_set_deadline(self):
		"""Test setting deadline for existing task."""
		self.tms.create_task("task1", "alice", 1)
		result = self.tms.set_deadline("task1", 6000)
		self.assertEqual(result, "6000")

	@timeout(0.4)
	def test_level_3_case_03_add_dependency(self):
		"""Test adding dependency between tasks."""
		self.tms.create_task("task1", "alice", 1)
		self.tms.create_task("task2", "bob", 2)
		result = self.tms.add_dependency("task2", "task1")
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_3_case_04_update_status_with_check_blocked(self):
		"""Test status update blocked by unsatisfied dependencies."""
		self.tms.create_task("task1", "alice", 1)
		self.tms.create_task("task2", "bob", 2)
		self.tms.add_dependency("task2", "task1")
		result = self.tms.update_status_with_check(2000, "task2", "IN_PROGRESS")
		self.assertEqual(result, "dependencies not satisfied")

	@timeout(0.4)
	def test_level_3_case_05_update_status_with_check_allowed(self):
		"""Test status update allowed when dependencies satisfied."""
		self.tms.create_task("task1", "alice", 1)
		self.tms.create_task("task2", "bob", 2)
		self.tms.add_dependency("task2", "task1")
		self.tms.update_status("task1", "DONE")
		result = self.tms.update_status_with_check(2000, "task2", "IN_PROGRESS")
		self.assertEqual(result, "IN_PROGRESS")

	@timeout(0.4)
	def test_level_3_case_06_get_overdue_tasks(self):
		"""Test getting overdue tasks."""
		self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 5000)
		self.tms.create_task_with_deadline(1000, "task2", "bob", 2, 3000)
		self.tms.create_task_with_deadline(1000, "task3", "alice", 1, 7000)
		self.tms.update_status("task1", "DONE")  # Not overdue (completed)
		result = self.tms.get_overdue_tasks(4000)
		# task2 is overdue (deadline 3000 < 4000), task1 is DONE so not overdue
		self.assertEqual(result, "task2")

	@timeout(0.4)
	def test_level_3_case_07_get_task_with_details(self):
		"""Test getting detailed task information."""
		self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 5000)
		self.tms.create_task_with_deadline(1000, "task2", "bob", 2, 3000)
		self.tms.add_dependency("task2", "task1")
		result = self.tms.get_task_with_details("task2")
		self.assertEqual(result, "user:bob,status:TODO,priority:2,deadline:3000,dependencies:[task1]")

	@timeout(0.4)
	def test_level_3_case_08_get_available_tasks(self):
		"""Test getting available tasks (no unsatisfied dependencies)."""
		self.tms.create_task("task1", "alice", 1)
		self.tms.create_task("task2", "alice", 2)
		self.tms.create_task("task3", "alice", 1)
		self.tms.add_dependency("task3", "task2")
		# task1 and task2 are available (no dependencies), task3 is blocked
		result = self.tms.get_available_tasks("alice")
		self.assertEqual(result, "task1, task2")

	@timeout(0.4)
	def test_level_3_case_09_circular_dependency_detection(self):
		"""Test that circular dependencies are prevented."""
		self.tms.create_task("task1", "alice", 1)
		self.tms.create_task("task2", "bob", 2)
		self.tms.create_task("task3", "charlie", 3)
		self.tms.add_dependency("task2", "task1")
		self.tms.add_dependency("task3", "task2")
		# Trying to add task1 -> task3 would create a cycle
		result = self.tms.add_dependency("task1", "task3")
		self.assertEqual(result, "false")

	@timeout(0.4)
	def test_level_3_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_3."""
		self.assertEqual(self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 5000), "true")
		self.assertEqual(self.tms.create_task_with_deadline(1000, "task2", "bob", 2, 3000), "true")
		self.assertEqual(self.tms.create_task("task3", "alice", 1), "true")
		self.assertEqual(self.tms.set_deadline("task3", 6000), "6000")
		self.assertEqual(self.tms.add_dependency("task2", "task1"), "true")
		# task2 depends on task1, so can't start yet
		self.assertEqual(self.tms.update_status_with_check(2000, "task2", "IN_PROGRESS"), "dependencies not satisfied")
		self.assertEqual(self.tms.update_status("task1", "IN_PROGRESS"), "IN_PROGRESS")
		self.assertEqual(self.tms.update_status("task1", "DONE"), "DONE")
		# Now task2 can start
		self.assertEqual(self.tms.update_status_with_check(2000, "task2", "IN_PROGRESS"), "IN_PROGRESS")
		# At time 4000, task2 is overdue (deadline 3000)
		self.assertEqual(self.tms.get_overdue_tasks(4000), "task2")
		self.assertEqual(self.tms.get_task_with_details("task2"), "user:bob,status:IN_PROGRESS,priority:2,deadline:3000,dependencies:[task1]")
		# task3 has no dependencies, so it's available for alice
		self.assertEqual(self.tms.get_available_tasks("alice"), "task3")
		self.assertEqual(self.tms.add_dependency("task3", "task2"), "true")
		# Now task3 is blocked by task2
		self.assertEqual(self.tms.get_available_tasks("alice"), "")


if __name__ == "__main__":
	unittest.main()
