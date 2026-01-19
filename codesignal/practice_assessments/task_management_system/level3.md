# Scenario

Your task is to implement a simplified version of a task management system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of task management system with various tasks:

```plaintext
[TaskManagementSystem]
    Task: "task1"
        user: "alice"
        status: "TODO"
        priority: 1
    Task: "task2"
        user: "bob"
        status: "IN_PROGRESS"
        priority: 3
```

## Level 1 – Initial Design & Basic Functions

- **CREATE_TASK(task_id, user, priority)**
  - Create a new task with the given task_id, assigned to user, with priority level.
  - Priority is an integer (1 = highest priority, higher numbers = lower priority).
  - Initial status is "TODO".
  - If a task with the same task_id already exists, return "false".
  - Otherwise, return "true".

- **UPDATE_STATUS(task_id, new_status)**
  - Update the status of a task.
  - Valid statuses: "TODO", "IN_PROGRESS", "DONE", "BLOCKED".
  - If the task doesn't exist, return "" (empty string).
  - Return the new status as a string.

- **GET_TASK(task_id)**
  - Get information about a task.
  - Format: "user:{user},status:{status},priority:{priority}"
  - If the task doesn't exist, return "" (empty string).

- **UPDATE_PRIORITY(task_id, new_priority)**
  - Update the priority of a task.
  - If the task doesn't exist, return "" (empty string).
  - Return the new priority as a string.

- **DELETE_TASK(task_id)**
  - Delete a task.
  - If the task doesn't exist, return "false".
  - Otherwise, return "true".

## Level 2 – Filtering & Querying

- **GET_TASKS_BY_USER(user)**
  - Get all tasks assigned to a user.
  - Return comma-separated list of task_ids sorted by priority (ascending, lowest number first), then by task_id alphabetically.
  - If no tasks found, return "" (empty string).
  - Example: "task1, task3, task5"

- **GET_TASKS_BY_STATUS(status)**
  - Get all tasks with the specified status.
  - Return comma-separated list of task_ids sorted by priority (ascending), then by task_id alphabetically.
  - If no tasks found, return "" (empty string).

- **GET_TASKS_BY_PRIORITY(priority)**
  - Get all tasks with the specified priority level.
  - Return comma-separated list of task_ids sorted alphabetically.
  - If no tasks found, return "" (empty string).

- **TOP_PRIORITY_TASKS(n)**
  - Get the top n highest priority tasks (lowest priority numbers).
  - Format: "task_id1(priority1), task_id2(priority2)"
  - Order by priority ascending, then by task_id alphabetically for ties.
  - Only include tasks that are not "DONE".
  - If there are fewer than n tasks, return all available tasks.

- **REASSIGN_TASK(task_id, new_user)**
  - Reassign a task to a different user.
  - If task doesn't exist, return "" (empty string).
  - Return the new user as a string.

## Level 3 – Deadlines & Dependencies

Tasks now support deadlines and dependencies. Add timestamp parameter to operations.

- **CREATE_TASK_WITH_DEADLINE(timestamp, task_id, user, priority, deadline)**
  - Create a task with a deadline (timestamp in milliseconds).
  - If task_id already exists, return "false".
  - Return "true" if created successfully.

- **SET_DEADLINE(task_id, deadline)**
  - Set or update the deadline for a task.
  - If task doesn't exist, return "" (empty string).
  - Return the deadline as a string.

- **ADD_DEPENDENCY(task_id, depends_on_task_id)**
  - Specify that task_id depends on depends_on_task_id.
  - A task cannot be moved to "IN_PROGRESS" or "DONE" until all its dependencies are "DONE".
  - If either task doesn't exist, return "false".
  - If this would create a circular dependency, return "false".
  - Return "true" if dependency added successfully.

- **UPDATE_STATUS_WITH_CHECK(timestamp, task_id, new_status)**
  - Update status with dependency checking.
  - If new_status is "IN_PROGRESS" or "DONE", check that all dependencies are "DONE".
  - If dependencies not satisfied, return "dependencies not satisfied".
  - If task doesn't exist, return "" (empty string).
  - Return the new status if successful.

- **GET_OVERDUE_TASKS(timestamp)**
  - Get all tasks that are overdue at the given timestamp.
  - A task is overdue if: status is not "DONE" AND deadline < timestamp.
  - Return comma-separated list of task_ids sorted by deadline (earliest first), then by task_id alphabetically.
  - If no overdue tasks, return "" (empty string).

- **GET_TASK_WITH_DETAILS(task_id)**
  - Get detailed task information including deadline and dependencies.
  - Format: "user:{user},status:{status},priority:{priority},deadline:{deadline},dependencies:[dep1,dep2]"
  - If no deadline set, use "deadline:none".
  - If no dependencies, use "dependencies:[]".
  - Dependencies listed alphabetically.
  - If task doesn't exist, return "" (empty string).

- **GET_AVAILABLE_TASKS(user)**
  - Get tasks assigned to user that can be started (all dependencies satisfied and status is "TODO").
  - Return comma-separated list of task_ids sorted by priority, then alphabetically.
  - If no tasks available, return "" (empty string).
