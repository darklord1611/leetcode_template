"""
Task Management System - Abstract Base Class

A simplified task tracker. The set of operations is intentionally small:
later levels extend the BEHAVIOUR of the same functions rather than adding many
new ones. Implement one level at a time and expect to reopen earlier functions.
"""


class TaskManagementSystem:
	"""Abstract base class for the task management system."""

	def __init__(self):
		"""Initialize the task management system."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: Basic CRUD

	def create_task(self, timestamp: int, task_id: str, priority: int) -> str:
		"""
		Create a new task with the given priority and status "open".

		Returns:
		    str: "true" if created, "false" if the task already exists.
		"""
		raise NotImplementedError("Subclasses must implement create_task()")

	def update_status(self, timestamp: int, task_id: str, status: str) -> str:
		"""
		Set the status of a task. status is one of "open", "in_progress", "done".

		Returns:
		    str: "true" on success, or "" if the task does not exist.
		"""
		raise NotImplementedError("Subclasses must implement update_status()")

	def update_priority(self, timestamp: int, task_id: str, priority: int) -> str:
		"""
		Set the priority of a task.

		Returns:
		    str: "true" on success, or "" if the task does not exist.
		"""
		raise NotImplementedError("Subclasses must implement update_priority()")

	def get_task(self, timestamp: int, task_id: str) -> str:
		"""
		Look up a task.

		Returns:
		    str: "task_id(priority,status)" e.g. "t1(5,open)", or "" if missing.
		"""
		raise NotImplementedError("Subclasses must implement get_task()")

	def delete_task(self, timestamp: int, task_id: str) -> str:
		"""
		Delete a task.

		Returns:
		    str: "true" if the task existed and was removed, otherwise "false".
		"""
		raise NotImplementedError("Subclasses must implement delete_task()")

	# Level 2 Methods: Queries (read-only)

	def get_tasks_by_status(self, timestamp: int, status: str) -> str:
		"""
		Return all task ids with the given status.

		Returns:
		    str: ids sorted by (-priority, task_id asc), joined ", "; "" if none.
		"""
		raise NotImplementedError("Subclasses must implement get_tasks_by_status()")

	def top_priority_tasks(self, timestamp: int, n: int) -> str:
		"""
		Return the top n tasks by priority.

		Returns:
		    str: ids sorted by (-priority, task_id asc), joined ", "; "" if none.
		"""
		raise NotImplementedError("Subclasses must implement top_priority_tasks()")

	# Level 3 Methods: Dependencies & Blocking
	# (update_status and delete_task must be reopened to honour dependencies.)

	def add_dependency(self, timestamp: int, task_id: str, depends_on_id: str) -> str:
		"""
		Declare that task_id depends on depends_on_id.

		Returns:
		    str: "true" on success; "false" if either task is missing or the edge
		         would create a cycle.
		"""
		raise NotImplementedError("Subclasses must implement add_dependency()")

	def get_available_tasks(self, timestamp: int) -> str:
		"""
		Return tasks whose status != "done" and all of whose dependencies are "done".

		Returns:
		    str: ids sorted by (-priority, task_id asc), joined ", "; "" if none.
		"""
		raise NotImplementedError("Subclasses must implement get_available_tasks()")

	# Level 4 Methods: Analytics
	# (update_status must be reopened to track completion.)

	def get_blocked_tasks(self, timestamp: int) -> str:
		"""
		Return tasks with status != "done" that have at least one dependency
		that is not yet "done".

		Returns:
		    str: ids sorted by (-priority, task_id asc), joined ", "; "" if none.
		"""
		raise NotImplementedError("Subclasses must implement get_blocked_tasks()")

	def get_critical_path(self, timestamp: int) -> str:
		"""
		Return the longest chain of dependencies in the task graph, from the
		deepest prerequisite to the final dependent, joined with ",".

		Returns:
		    str: the critical path, or "" if there are no dependencies. Ties on
		         length are broken by the lexicographically smallest sequence.
		"""
		raise NotImplementedError("Subclasses must implement get_critical_path()")
