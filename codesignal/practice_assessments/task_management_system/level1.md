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
