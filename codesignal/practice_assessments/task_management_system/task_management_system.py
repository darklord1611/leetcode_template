"""
Task Management System - Abstract Base Class

This class defines the interface for a task management system
with task tracking, priorities, deadlines, dependencies, and analytics.
"""


class TaskManagementSystem:
    """
    Abstract base class for a task management system that manages tasks,
    priorities, deadlines, dependencies, and provides various query and analytics operations.
    """

    def __init__(self):
        """Initialize the task management system."""
        raise NotImplementedError("Subclasses must implement __init__")

    # Level 1 Methods: Basic CRUD Operations

    def create_task(self, task_id: str, user: str, priority: int) -> str:
        """
        Create a new task.

        Args:
            task_id (str): Unique identifier for the task
            user (str): User assigned to the task
            priority (int): Task priority (1=highest, 3=lowest)

        Returns:
            str: "true" if task created successfully, "false" if task already exists
        """
        raise NotImplementedError("Subclasses must implement create_task()")

    def get_task(self, task_id: str) -> str:
        """
        Get task details.

        Args:
            task_id (str): Task identifier

        Returns:
            str: "user:USER,status:STATUS,priority:PRIORITY" if task exists,
                 "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_task()")

    def update_status(self, task_id: str, status: str) -> str:
        """
        Update task status.

        Args:
            task_id (str): Task identifier
            status (str): New status (TODO, IN_PROGRESS, DONE, BLOCKED)

        Returns:
            str: New status if successful, "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement update_status()")

    def update_priority(self, task_id: str, priority: int) -> str:
        """
        Update task priority.

        Args:
            task_id (str): Task identifier
            priority (int): New priority (1=highest, 3=lowest)

        Returns:
            str: New priority as string if successful, "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement update_priority()")

    def delete_task(self, task_id: str) -> str:
        """
        Delete a task.

        Args:
            task_id (str): Task identifier

        Returns:
            str: "true" if task deleted successfully, "false" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement delete_task()")

    # Level 2 Methods: Filtering and Querying

    def get_tasks_by_user(self, user: str) -> str:
        """
        Get all tasks assigned to a user.

        Args:
            user (str): User name

        Returns:
            str: Comma-separated task IDs sorted by priority ascending, then by task_id ascending
                 Example: "task2, task4, task1"
        """
        raise NotImplementedError("Subclasses must implement get_tasks_by_user()")

    def get_tasks_by_status(self, status: str) -> str:
        """
        Get all tasks with a specific status.

        Args:
            status (str): Status to filter by (TODO, IN_PROGRESS, DONE, BLOCKED)

        Returns:
            str: Comma-separated task IDs sorted by priority ascending, then by task_id ascending
        """
        raise NotImplementedError("Subclasses must implement get_tasks_by_status()")

    def get_tasks_by_priority(self, priority: int) -> str:
        """
        Get all tasks with a specific priority.

        Args:
            priority (int): Priority to filter by

        Returns:
            str: Comma-separated task IDs sorted by task_id ascending
        """
        raise NotImplementedError("Subclasses must implement get_tasks_by_priority()")

    def top_priority_tasks(self, n: int) -> str:
        """
        Get top N highest priority tasks that are not DONE.

        Args:
            n (int): Number of tasks to return

        Returns:
            str: Formatted string "task1(priority), task2(priority), ..."
                 sorted by priority ascending, then by task_id ascending
                 Excludes tasks with status DONE
        """
        raise NotImplementedError("Subclasses must implement top_priority_tasks()")

    def reassign_task(self, task_id: str, new_user: str) -> str:
        """
        Reassign a task to a different user.

        Args:
            task_id (str): Task identifier
            new_user (str): New user to assign the task to

        Returns:
            str: New user name if successful, "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement reassign_task()")

    # Level 3 Methods: Deadlines and Dependencies

    def create_task_with_deadline(self, timestamp: int, task_id: str, user: str,
                                  priority: int, deadline: int) -> str:
        """
        Create a new task with a deadline.

        Args:
            timestamp (int): Creation timestamp
            task_id (str): Unique identifier for the task
            user (str): User assigned to the task
            priority (int): Task priority
            deadline (int): Deadline timestamp

        Returns:
            str: "true" if task created successfully, "false" if task already exists
        """
        raise NotImplementedError("Subclasses must implement create_task_with_deadline()")

    def set_deadline(self, task_id: str, deadline: int) -> str:
        """
        Set or update deadline for an existing task.

        Args:
            task_id (str): Task identifier
            deadline (int): Deadline timestamp

        Returns:
            str: Deadline as string if successful, "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement set_deadline()")

    def add_dependency(self, task_id: str, depends_on_task_id: str) -> str:
        """
        Add a dependency between tasks (task_id depends on depends_on_task_id).

        Args:
            task_id (str): Task that has the dependency
            depends_on_task_id (str): Task that must be completed first

        Returns:
            str: "true" if dependency added successfully,
                 "false" if would create circular dependency or task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement add_dependency()")

    def update_status_with_check(self, timestamp: int, task_id: str, status: str) -> str:
        """
        Update task status with dependency checking.

        Args:
            timestamp (int): Update timestamp
            task_id (str): Task identifier
            status (str): New status

        Returns:
            str: New status if successful,
                 "dependencies not satisfied" if dependencies are not met,
                 "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement update_status_with_check()")

    def get_overdue_tasks(self, timestamp: int) -> str:
        """
        Get all tasks that are overdue (not DONE and past their deadline).

        Args:
            timestamp (int): Current timestamp

        Returns:
            str: Comma-separated task IDs sorted by deadline ascending, then by task_id ascending
        """
        raise NotImplementedError("Subclasses must implement get_overdue_tasks()")

    def get_task_with_details(self, task_id: str) -> str:
        """
        Get detailed task information including dependencies.

        Args:
            task_id (str): Task identifier

        Returns:
            str: "user:USER,status:STATUS,priority:PRIORITY,deadline:DEADLINE,dependencies:[dep1,dep2]"
                 if task exists, "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_task_with_details()")

    def get_available_tasks(self, user: str) -> str:
        """
        Get all tasks assigned to a user that have no unsatisfied dependencies.

        Args:
            user (str): User name

        Returns:
            str: Comma-separated task IDs sorted by priority ascending, then by task_id ascending
        """
        raise NotImplementedError("Subclasses must implement get_available_tasks()")

    # Level 4 Methods: History and Reporting

    def get_task_history(self, task_id: str) -> str:
        """
        Get the status history of a task.

        Args:
            task_id (str): Task identifier

        Returns:
            str: Status history in format "STATUS1->STATUS2->STATUS3",
                 "" if task doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_task_history()")

    def get_user_statistics(self, user: str) -> str:
        """
        Get statistics for a user's tasks.

        Args:
            user (str): User name

        Returns:
            str: "total:N,todo:N,in_progress:N,done:N,blocked:N"
        """
        raise NotImplementedError("Subclasses must implement get_user_statistics()")

    def get_completion_time(self, task_id: str) -> str:
        """
        Get the time taken to complete a task.

        Args:
            task_id (str): Task identifier

        Returns:
            str: Time taken in milliseconds as string (completion_time - creation_time),
                 "" if task doesn't exist or is not DONE
        """
        raise NotImplementedError("Subclasses must implement get_completion_time()")

    def get_slowest_tasks(self, n: int) -> str:
        """
        Get the N slowest completed tasks.

        Args:
            n (int): Number of tasks to return

        Returns:
            str: Formatted string "task1(time), task2(time), ..."
                 sorted by completion time descending, then by task_id ascending
        """
        raise NotImplementedError("Subclasses must implement get_slowest_tasks()")

    def rollback_task(self, task_id: str, status: str) -> str:
        """
        Rollback a task to a previous status.

        Args:
            task_id (str): Task identifier
            status (str): Status to rollback to

        Returns:
            str: New status if successful, "" if task doesn't exist or status not in history
        """
        raise NotImplementedError("Subclasses must implement rollback_task()")

    def get_critical_path(self) -> str:
        """
        Get the critical path (longest chain of dependent tasks).

        Returns:
            str: Comma-separated task IDs representing the longest dependency chain
                 If multiple chains have same length, return the one starting with smallest task_id
        """
        raise NotImplementedError("Subclasses must implement get_critical_path()")

    def predict_completion(self, timestamp: int, task_id: str) -> str:
        """
        Predict when a task will be completed based on average completion times.

        Args:
            timestamp (int): Current timestamp
            task_id (str): Task identifier

        Returns:
            str: Predicted completion timestamp as string,
                 "" if task doesn't exist or is already DONE
        """
        raise NotImplementedError("Subclasses must implement predict_completion()")
