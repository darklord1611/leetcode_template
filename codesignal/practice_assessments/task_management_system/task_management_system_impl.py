from task_management_system import TaskManagementSystem


class TaskManagementSystemImpl(TaskManagementSystem):
	"""
	Implementation of the TaskManagementSystem interface.

	The function set is small on purpose. Implement one level at a time and
	expect to reopen earlier functions to satisfy later requirements.
	"""

	def __init__(self):
		"""Initialize the task management system."""
		# TODO: implement
		pass

	# Level 1 Methods: Basic CRUD

	def create_task(self, timestamp: int, task_id: str, priority: int) -> str:
		"""Create a new task with the given priority and status "open"."""
		# TODO: implement
		pass

	def update_status(self, timestamp: int, task_id: str, status: str) -> str:
		"""Set the status of a task."""
		# TODO: implement
		pass

	def update_priority(self, timestamp: int, task_id: str, priority: int) -> str:
		"""Set the priority of a task."""
		# TODO: implement
		pass

	def get_task(self, timestamp: int, task_id: str) -> str:
		"""Look up a task."""
		# TODO: implement
		pass

	def delete_task(self, timestamp: int, task_id: str) -> str:
		"""Delete a task."""
		# TODO: implement
		pass

	# Level 2 Methods: Queries (read-only)

	def get_tasks_by_status(self, timestamp: int, status: str) -> str:
		"""Return all task ids with the given status."""
		# TODO: implement
		pass

	def top_priority_tasks(self, timestamp: int, n: int) -> str:
		"""Return the top n tasks by priority."""
		# TODO: implement
		pass

	# Level 3 Methods: Dependencies & Blocking

	def add_dependency(self, timestamp: int, task_id: str, depends_on_id: str) -> str:
		"""Declare that task_id depends on depends_on_id."""
		# TODO: implement
		pass

	def get_available_tasks(self, timestamp: int) -> str:
		"""Return tasks whose status != "done" and all of whose dependencies are "done"."""
		# TODO: implement
		pass

	# Level 4 Methods: Analytics

	def get_blocked_tasks(self, timestamp: int) -> str:
		"""Return non-done tasks that have at least one dependency not yet "done"."""
		# TODO: implement
		pass

	def get_critical_path(self, timestamp: int) -> str:
		"""Return the longest chain of dependencies in the task graph."""
		# TODO: implement
		pass
