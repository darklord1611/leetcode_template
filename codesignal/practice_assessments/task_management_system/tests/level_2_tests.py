import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from task_management_system_impl import TaskManagementSystemImpl


class Level2Tests(unittest.TestCase):
    """
    Level 2 tests for Task Management System - Filtering and Querying

    Tests cover: GET_TASKS_BY_USER, GET_TASKS_BY_STATUS, GET_TASKS_BY_PRIORITY,
                 TOP_PRIORITY_TASKS, REASSIGN_TASK
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh TaskManagementSystem instance for each test."""
        self.tms = TaskManagementSystemImpl()

    @timeout(0.4)
    def test_level_2_case_01_get_tasks_by_user(self):
        """Test getting tasks by user."""
        self.tms.create_task("task1", "alice", 2)
        self.tms.create_task("task2", "alice", 1)
        self.tms.create_task("task3", "bob", 3)
        result = self.tms.get_tasks_by_user("alice")
        # Sorted by priority ascending (1, 2), then by task_id
        self.assertEqual(result, "task2, task1")

    @timeout(0.4)
    def test_level_2_case_02_get_tasks_by_status(self):
        """Test getting tasks by status."""
        self.tms.create_task("task1", "alice", 2)
        self.tms.create_task("task2", "bob", 1)
        self.tms.create_task("task3", "alice", 1)
        self.tms.update_status("task2", "IN_PROGRESS")
        result_todo = self.tms.get_tasks_by_status("TODO")
        result_in_progress = self.tms.get_tasks_by_status("IN_PROGRESS")
        # TODO: task3(1), task1(2) - sorted by priority then task_id
        self.assertEqual(result_todo, "task1, task3")
        self.assertEqual(result_in_progress, "task2")

    @timeout(0.4)
    def test_level_2_case_03_get_tasks_by_priority(self):
        """Test getting tasks by priority."""
        self.tms.create_task("task1", "alice", 1)
        self.tms.create_task("task2", "bob", 1)
        self.tms.create_task("task3", "charlie", 2)
        result = self.tms.get_tasks_by_priority(1)
        # Sorted by task_id ascending
        self.assertEqual(result, "task1, task2")

    @timeout(0.4)
    def test_level_2_case_04_top_priority_tasks(self):
        """Test top priority tasks excluding DONE tasks."""
        self.tms.create_task("task1", "alice", 2)
        self.tms.create_task("task2", "bob", 1)
        self.tms.create_task("task3", "charlie", 3)
        self.tms.create_task("task4", "alice", 1)
        self.tms.update_status("task3", "DONE")
        result = self.tms.top_priority_tasks(3)
        # Excludes task3 (DONE), returns task2(1), task4(1), task1(2)
        self.assertEqual(result, "task2(1), task4(1), task1(2)")

    @timeout(0.4)
    def test_level_2_case_05_reassign_task(self):
        """Test reassigning a task to a different user."""
        self.tms.create_task("task1", "alice", 1)
        result = self.tms.reassign_task("task1", "bob")
        self.assertEqual(result, "bob")
        # Verify reassignment
        task = self.tms.get_task("task1")
        self.assertEqual(task, "user:bob,status:TODO,priority:1")

    @timeout(0.4)
    def test_level_2_case_06_reassign_nonexistent_task(self):
        """Test reassigning non-existent task returns empty string."""
        result = self.tms.reassign_task("nonexistent", "alice")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_2_case_07_get_tasks_by_user_empty(self):
        """Test getting tasks for user with no tasks."""
        self.tms.create_task("task1", "alice", 1)
        result = self.tms.get_tasks_by_user("bob")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_2_case_08_top_priority_tasks_with_limit(self):
        """Test top priority tasks respects the limit."""
        for i in range(5):
            self.tms.create_task(f"task{i}", "alice", i % 3 + 1)
        result = self.tms.top_priority_tasks(3)
        # task0(1), task3(1), task1(2) - first 3 by priority
        self.assertEqual(result, "task0(1), task3(1), task1(2)")

    @timeout(0.4)
    def test_level_2_case_09_mixed_status_filtering(self):
        """Test multiple status filtering."""
        self.tms.create_task("task1", "alice", 1)
        self.tms.create_task("task2", "bob", 2)
        self.tms.create_task("task3", "charlie", 1)
        self.tms.update_status("task1", "IN_PROGRESS")
        self.tms.update_status("task2", "DONE")
        result_todo = self.tms.get_tasks_by_status("TODO")
        result_done = self.tms.get_tasks_by_status("DONE")
        self.assertEqual(result_todo, "task3")
        self.assertEqual(result_done, "task2")

    @timeout(0.4)
    def test_level_2_case_10_complete_scenario(self):
        """Test complete scenario from test_data_2."""
        self.assertEqual(self.tms.create_task("task1", "alice", 2), "true")
        self.assertEqual(self.tms.create_task("task2", "alice", 1), "true")
        self.assertEqual(self.tms.create_task("task3", "bob", 3), "true")
        self.assertEqual(self.tms.create_task("task4", "alice", 1), "true")
        self.assertEqual(self.tms.create_task("task5", "bob", 2), "true")
        self.assertEqual(self.tms.update_status("task2", "IN_PROGRESS"), "IN_PROGRESS")
        self.assertEqual(self.tms.update_status("task3", "DONE"), "DONE")
        # Alice's tasks: task2(1), task4(1), task1(2) - sorted by priority then task_id
        self.assertEqual(self.tms.get_tasks_by_user("alice"), "task2, task4, task1")
        # Bob's tasks: task5(2), task3(3)
        self.assertEqual(self.tms.get_tasks_by_user("bob"), "task5, task3")
        # TODO tasks: task1, task4, task5
        self.assertEqual(self.tms.get_tasks_by_status("TODO"), "task1, task4, task5")
        # IN_PROGRESS tasks: task2
        self.assertEqual(self.tms.get_tasks_by_status("IN_PROGRESS"), "task2")
        # Priority 1 tasks: task2, task4
        self.assertEqual(self.tms.get_tasks_by_priority(1), "task2, task4")
        # Top 3 priority tasks (excluding DONE): task2(1), task4(1), task1(2)
        self.assertEqual(self.tms.top_priority_tasks(3), "task2(1), task4(1), task1(2)")
        # Reassign task1 to charlie
        self.assertEqual(self.tms.reassign_task("task1", "charlie"), "charlie")
        # Alice's tasks after reassignment: task2, task4
        self.assertEqual(self.tms.get_tasks_by_user("alice"), "task2, task4")
        # Charlie's tasks: task1
        self.assertEqual(self.tms.get_tasks_by_user("charlie"), "task1")


if __name__ == '__main__':
    unittest.main()
