import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from task_management_system_impl import TaskManagementSystemImpl


class Level4Tests(unittest.TestCase):
    """
    Level 4 tests for Task Management System - History and Reporting

    Tests cover: GET_TASK_HISTORY, GET_USER_STATISTICS, GET_COMPLETION_TIME,
                 GET_SLOWEST_TASKS, ROLLBACK_TASK, GET_CRITICAL_PATH, PREDICT_COMPLETION
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh TaskManagementSystem instance for each test."""
        self.tms = TaskManagementSystemImpl()

    @timeout(0.4)
    def test_level_4_case_01_get_task_history(self):
        """Test getting task status history."""
        self.tms.create_task("task1", "alice", 1)
        self.tms.update_status("task1", "IN_PROGRESS")
        self.tms.update_status("task1", "BLOCKED")
        self.tms.update_status("task1", "IN_PROGRESS")
        self.tms.update_status("task1", "DONE")
        result = self.tms.get_task_history("task1")
        self.assertEqual(result, "TODO->IN_PROGRESS->BLOCKED->IN_PROGRESS->DONE")

    @timeout(0.4)
    def test_level_4_case_02_get_user_statistics(self):
        """Test getting user statistics."""
        self.tms.create_task("task1", "alice", 1)
        self.tms.create_task("task2", "alice", 1)
        self.tms.create_task("task3", "alice", 2)
        self.tms.update_status("task1", "IN_PROGRESS")
        self.tms.update_status("task2", "DONE")
        result = self.tms.get_user_statistics("alice")
        self.assertEqual(result, "total:3,todo:1,in_progress:1,done:1,blocked:0")

    @timeout(0.4)
    def test_level_4_case_03_get_completion_time(self):
        """Test getting task completion time."""
        self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 10000)
        self.tms.update_status_with_check(5000, "task1", "DONE")
        result = self.tms.get_completion_time("task1")
        # 5000 - 1000 = 4000
        self.assertEqual(result, "4000")

    @timeout(0.4)
    def test_level_4_case_04_get_completion_time_not_done(self):
        """Test getting completion time for task not yet done."""
        self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 10000)
        result = self.tms.get_completion_time("task1")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_4_case_05_get_slowest_tasks(self):
        """Test getting slowest completed tasks."""
        self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 10000)
        self.tms.create_task_with_deadline(1000, "task2", "bob", 2, 10000)
        self.tms.create_task_with_deadline(1000, "task3", "charlie", 3, 10000)
        self.tms.update_status_with_check(5000, "task1", "DONE")  # 4000 ms
        self.tms.update_status_with_check(3000, "task2", "DONE")  # 2000 ms
        self.tms.update_status_with_check(7000, "task3", "DONE")  # 6000 ms
        result = self.tms.get_slowest_tasks(2)
        # Sorted by time descending: task3(6000), task1(4000)
        self.assertEqual(result, "task3(6000), task1(4000)")

    @timeout(0.4)
    def test_level_4_case_06_rollback_task(self):
        """Test rolling back task to previous status."""
        self.tms.create_task("task1", "alice", 1)
        self.tms.update_status("task1", "IN_PROGRESS")
        self.tms.update_status("task1", "DONE")
        result = self.tms.rollback_task("task1", "IN_PROGRESS")
        self.assertEqual(result, "IN_PROGRESS")
        # Verify rollback
        task = self.tms.get_task("task1")
        self.assertEqual(task, "user:alice,status:IN_PROGRESS,priority:1")

    @timeout(0.4)
    def test_level_4_case_07_get_critical_path(self):
        """Test getting critical path (longest dependency chain)."""
        self.tms.create_task("task1", "alice", 1)
        self.tms.create_task("task2", "bob", 2)
        self.tms.create_task("task3", "charlie", 3)
        self.tms.create_task("task4", "dave", 1)
        self.tms.add_dependency("task2", "task1")
        self.tms.add_dependency("task3", "task2")
        # Chain: task1 -> task2 -> task3 (length 3), task4 standalone (length 1)
        result = self.tms.get_critical_path()
        self.assertEqual(result, "task1, task2, task3")

    @timeout(0.4)
    def test_level_4_case_08_predict_completion(self):
        """Test predicting task completion time."""
        self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 10000)
        self.tms.create_task_with_deadline(1000, "task2", "bob", 2, 10000)
        self.tms.create_task("task3", "charlie", 3)
        self.tms.update_status_with_check(5000, "task1", "DONE")  # 4000 ms
        self.tms.update_status_with_check(3000, "task2", "DONE")  # 2000 ms
        # Average: (4000 + 2000) / 2 = 3000
        result = self.tms.predict_completion(6000, "task3")
        # 6000 + 3000 = 9000
        self.assertEqual(result, "9000")

    @timeout(0.4)
    def test_level_4_case_09_get_user_statistics_empty(self):
        """Test user statistics for user with no tasks."""
        result = self.tms.get_user_statistics("alice")
        self.assertEqual(result, "total:0,todo:0,in_progress:0,done:0,blocked:0")

    @timeout(0.4)
    def test_level_4_case_10_complete_scenario(self):
        """Test complete scenario from test_data_4."""
        self.assertEqual(self.tms.create_task_with_deadline(1000, "task1", "alice", 1, 10000), "true")
        self.assertEqual(self.tms.create_task_with_deadline(1000, "task2", "alice", 1, 10000), "true")
        self.assertEqual(self.tms.create_task("task3", "bob", 2), "true")
        self.assertEqual(self.tms.update_status("task1", "IN_PROGRESS"), "IN_PROGRESS")
        self.assertEqual(self.tms.update_status("task1", "BLOCKED"), "BLOCKED")
        self.assertEqual(self.tms.update_status("task1", "IN_PROGRESS"), "IN_PROGRESS")
        self.assertEqual(self.tms.update_status_with_check(5000, "task1", "DONE"), "DONE")
        self.assertEqual(self.tms.update_status_with_check(3000, "task2", "DONE"), "DONE")
        self.assertEqual(self.tms.get_task_history("task1"), "TODO->IN_PROGRESS->BLOCKED->IN_PROGRESS->DONE")
        self.assertEqual(self.tms.get_user_statistics("alice"), "total:2,todo:0,in_progress:0,done:2,blocked:0")
        self.assertEqual(self.tms.get_user_statistics("bob"), "total:1,todo:1,in_progress:0,done:0,blocked:0")
        self.assertEqual(self.tms.get_completion_time("task1"), "4000")  # 5000 - 1000
        self.assertEqual(self.tms.get_completion_time("task2"), "2000")  # 3000 - 1000
        self.assertEqual(self.tms.get_slowest_tasks(2), "task1(4000), task2(2000)")
        self.assertEqual(self.tms.rollback_task("task1", "IN_PROGRESS"), "IN_PROGRESS")
        self.assertEqual(self.tms.get_task("task1"), "user:alice,status:IN_PROGRESS,priority:1")
        self.assertEqual(self.tms.add_dependency("task3", "task1"), "true")
        self.assertEqual(self.tms.get_critical_path(), "task1, task3")
        # Average completion time: (4000 + 2000) / 2 = 3000
        # Prediction at 6000: 6000 + 3000 = 9000
        self.assertEqual(self.tms.predict_completion(6000, "task3"), "9000")


if __name__ == '__main__':
    unittest.main()
