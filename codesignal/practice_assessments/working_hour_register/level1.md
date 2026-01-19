# Scenario

Your task is to implement a simplified version of a working hour register system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of working hour register with various employees:

```plaintext
[WorkingHourRegister]
    Employee: "emp001"
        2024-01-15: 09:00 -> 17:00 (8 hours)
    Employee: "emp002"
        2024-01-15: 10:00 -> 18:00 (8 hours)
```

## Level 1 – Initial Design & Basic Functions

- **CLOCK_IN(timestamp, employee_id)**
  - Record when an employee starts work.
  - timestamp is in milliseconds since epoch.
  - If the employee is already clocked in (without clocking out), return "false".
  - Otherwise, return "true".

- **CLOCK_OUT(timestamp, employee_id)**
  - Record when an employee finishes work.
  - If the employee is not clocked in, return "" (empty string).
  - Calculate hours worked in this session (rounded down to nearest integer).
  - Return the hours worked in this session as a string.

- **GET_TOTAL_HOURS(employee_id)**
  - Get total hours worked by an employee across all sessions.
  - Return total hours as a string (rounded down to nearest integer).
  - If employee doesn't exist or has no completed sessions, return "0".

- **GET_EMPLOYEES_WORKING(timestamp)**
  - Get all employees currently clocked in at the given timestamp.
  - Return comma-separated list of employee_ids sorted alphabetically.
  - If no employees are working, return "" (empty string).

- **IS_CLOCKED_IN(employee_id)**
  - Check if an employee is currently clocked in.
  - Return "true" if clocked in, "false" if not or employee doesn't exist.
