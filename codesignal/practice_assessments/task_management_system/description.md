> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified version of a **task management system**.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, keeping in mind that **you will need to reopen and refactor functions you wrote in earlier
levels** so they satisfy the additional requirements introduced later. The set of functions is intentionally small;
most of the difficulty comes from extending the *behaviour* of the same functions across levels.
Please, do not change the existing method signatures.

## Task

Every task has a `task_id`, an integer `priority`, and a `status` that is one of `"open"`, `"in_progress"`, or
`"done"`. All timestamps are integers and are **non-decreasing** across calls; the first parameter of every method is
`timestamp` even when a level does not use it. All return values are **strings**. List results are sorted by
`(-priority, task_id ascending)` — i.e. highest priority first, ties broken by task id in ascending order — and
joined with `", "`; an empty result is returned as `""` (empty string).

---

## Level 1 – Basic CRUD

- **create_task(timestamp, task_id, priority)**
  - Create a new task with the given integer `priority` and status `"open"`.
  - Return "false" if a task with that id already exists, otherwise "true".

- **update_status(timestamp, task_id, status)**
  - Set the task's status to `status` (one of `"open"`, `"in_progress"`, `"done"`).
  - Return "true" on success, or "" if the task does not exist.

- **update_priority(timestamp, task_id, priority)**
  - Set the task's priority.
  - Return "true" on success, or "" if the task does not exist.

- **get_task(timestamp, task_id)**
  - Return the task formatted as `"task_id(priority,status)"`, e.g. `"t1(5,open)"`.
  - Return "" if the task does not exist.

- **delete_task(timestamp, task_id)**
  - Remove the task.
  - Return "true" if the task existed and was removed, otherwise "false".

---

## Level 2 – Queries

Read-only additions that rank and filter the tasks created in Level 1.

- **get_tasks_by_status(timestamp, status)**
  - Return the ids of all tasks with the given status, sorted by `(-priority, task_id asc)`, joined with `", "`.
  - Return "" if no task has that status.

- **top_priority_tasks(timestamp, n)**
  - Return the ids of the `n` highest-priority tasks, sorted by `(-priority, task_id asc)`, joined with `", "`.
  - If fewer than `n` tasks exist, return all of them. Return "" if there are no tasks.

---

## Level 3 – Dependencies & Blocking

Tasks may depend on one another. A dependency means "this task can only progress once its prerequisites are done".
This forces you to **reopen `update_status` and `delete_task`**.

- **add_dependency(timestamp, task_id, depends_on_id)**
  - Declare that `task_id` depends on `depends_on_id` (i.e. `depends_on_id` must be `"done"` before `task_id` can
    advance). The stored edge points from a task to its prerequisite (`task_id -> depends_on_id`).
  - Return "false" if either task does not exist, or if adding the edge would create a cycle.
  - Return "true" otherwise.

- **update_status** *(updated)*
  - A task may only move to `"in_progress"` or `"done"` if **all** of its dependencies currently have status
    `"done"`. If the move is blocked, return "" and leave the status unchanged. Moving a task to `"open"` is always
    allowed. Tasks that do not exist still return "".

- **delete_task** *(updated)*
  - Deleting a task also removes it from the dependency lists of every other task that depended on it.

- **get_available_tasks(timestamp)**
  - Return the ids of every task whose status is **not** `"done"` and **all** of whose dependencies are `"done"`
    (a task with no dependencies qualifies), sorted by `(-priority, task_id asc)`, joined with `", "`.
  - Return "" if there are none.

---

## Level 4 – Analytics

Analytics over the dependency graph. **`update_status` is reopened** once more so completion is tracked correctly for
the queries below (the dependency rule from Level 3 still applies).

- **get_blocked_tasks(timestamp)**
  - Return the ids of every task whose status is **not** `"done"` that has **at least one** dependency which is not
    yet `"done"`, sorted by `(-priority, task_id asc)`, joined with `", "`.
  - This is the complement of `get_available_tasks` among the non-done tasks. Return "" if there are none.

- **get_critical_path(timestamp)**
  - Return the **longest chain of dependencies** in the whole task graph, following the `depends_on` edges. The chain
    is returned from the **deepest prerequisite to the final dependent**, joined with `,` (no spaces), e.g. a chain
    where `c` depends on `b` and `b` depends on `a` is returned as `"a,b,c"`.
  - If multiple chains share the maximum length, return the **lexicographically smallest** sequence (comparing the
    ordered list of task ids). Return "" if there are no dependencies at all.
