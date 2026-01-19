import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from task_management_system_impl import TaskManagementSystemImpl


class Level1Tests(unittest.TestCase):
    """
    Level 1 tests for Task Management System - Basic CRUD Operations

    Tests cover: CREATE_TASK, GET_TASK, UPDATE_STATUS, UPDATE_PRIORITY, DELETE_TASK
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh TaskManagementSystem instance for each test."""
        self.tms = TaskManagementSystemImpl()

    @timeout(0.4)
    def test_level_1_case_01_create_task(self):
        """Test creating a new task."""
        result = self.tms.create_task("task1", "alice", 1)
        self.assertEqual(result, "true")

    @timeout(0.4)
    def test_level_1_case_02_create_duplicate_task(self):
        """Test that duplicate task creation returns false."""
        self.tms.create_task("task1", "alice", 1)
        result = self.tms.create_task("task1", "bob", 2)
        self.assertEqual(result, "false")

    @timeout(0.4)
    def test_level_1_case_03_get_task(self):
        """Test getting task details."""
        self.tms.create_task("task1", "alice", 2)
        result = self.tms.get_task("task1")
        self.assertEqual(result, "user:alice,status:TODO,priority:2")

    @timeout(0.4)
    def test_level_1_case_04_get_nonexistent_task(self):
        """Test getting non-existent task returns empty string."""
        result = self.tms.get_task("nonexistent")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_1_case_05_update_status(self):
        """Test updating task status."""
        self.tms.create_task("task1", "alice", 1)
        result = self.tms.update_status("task1", "IN_PROGRESS")
        self.assertEqual(result, "IN_PROGRESS")
        # Verify status changed
        task = self.tms.get_task("task1")
        self.assertEqual(task, "user:alice,status:IN_PROGRESS,priority:1")

    @timeout(0.4)
    def test_level_1_case_06_update_status_nonexistent_task(self):
        """Test updating status of non-existent task returns empty string."""
        result = self.tms.update_status("nonexistent", "DONE")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_1_case_07_update_priority(self):
        """Test updating task priority."""
        self.tms.create_task("task1", "bob", 3)
        result = self.tms.update_priority("task1", 1)
        self.assertEqual(result, "1")
        # Verify priority changed
        task = self.tms.get_task("task1")
        self.assertEqual(task, "user:bob,status:TODO,priority:1")

    @timeout(0.4)
    def test_level_1_case_08_delete_task(self):
        """Test deleting a task."""
        self.tms.create_task("task1", "alice", 1)
        result = self.tms.delete_task("task1")
        self.assertEqual(result, "true")
        # Verify task is deleted
        task = self.tms.get_task("task1")
        self.assertEqual(task, "")

    @timeout(0.4)
    def test_level_1_case_09_delete_nonexistent_task(self):
        """Test deleting non-existent task returns false."""
        result = self.tms.delete_task("nonexistent")
        self.assertEqual(result, "false")

    @timeout(0.4)
    def test_level_1_case_10_complete_scenario(self):
        """Test complete scenario from test_data_1."""
        self.assertEqual(self.tms.create_task("task1", "alice", 1), "true")
        self.assertEqual(self.tms.create_task("task2", "bob", 3), "true")
        self.assertEqual(self.tms.create_task("task3", "alice", 2), "true")
        self.assertEqual(self.tms.create_task("task1", "charlie", 1), "false")  # Duplicate
        self.assertEqual(self.tms.get_task("task1"), "user:alice,status:TODO,priority:1")
        self.assertEqual(self.tms.update_status("task1", "IN_PROGRESS"), "IN_PROGRESS")
        self.assertEqual(self.tms.get_task("task1"), "user:alice,status:IN_PROGRESS,priority:1")
        self.assertEqual(self.tms.update_priority("task2", 1), "1")
        self.assertEqual(self.tms.get_task("task2"), "user:bob,status:TODO,priority:1")
        self.assertEqual(self.tms.update_status("task3", "DONE"), "DONE")
        self.assertEqual(self.tms.delete_task("task3"), "true")
        self.assertEqual(self.tms.get_task("task3"), "")  # Deleted
        self.assertEqual(self.tms.update_status("nonexistent", "DONE"), "")


if __name__ == '__main__':
    unittest.main()
