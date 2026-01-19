# Scenario

Your task is to implement a simplified version of a working hour register system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Level 1 – Initial Design & Basic Functions

- **CLOCK_IN(timestamp, employee_id)**
- **CLOCK_OUT(timestamp, employee_id)**
- **GET_TOTAL_HOURS(employee_id)**
- **GET_EMPLOYEES_WORKING(timestamp)**
- **IS_CLOCKED_IN(employee_id)**

## Level 2 – Date-based Queries & Filtering

Timestamps represent dates. Implement operations to query hours by date range.

- **GET_HOURS_ON_DATE(employee_id, date)**
  - Get total hours worked by an employee on a specific date.
  - date format: "YYYY-MM-DD"
  - Return hours as a string (rounded down).
  - If no hours worked that day, return "0".

- **GET_HOURS_IN_RANGE(employee_id, start_date, end_date)**
  - Get total hours worked by an employee between start_date and end_date (inclusive).
  - date format: "YYYY-MM-DD"
  - Return hours as a string (rounded down).
  - If no hours in range, return "0".

- **GET_TOP_EMPLOYEES_BY_HOURS(n)**
  - Get top n employees by total hours worked.
  - Format: "emp_id1(hours1), emp_id2(hours2)"
  - Order by hours descending, then by employee_id alphabetically for ties.
  - If fewer than n employees, return all available.
  - If no employees, return "" (empty string).

- **GET_EMPLOYEES_BY_DATE(date)**
  - Get all employees who worked on a specific date.
  - Return comma-separated list of employee_ids sorted alphabetically.
  - If no employees worked that day, return "" (empty string).

- **GET_AVERAGE_DAILY_HOURS(employee_id)**
  - Calculate average hours per day for an employee (across days they worked).
  - Return average as a string (rounded down).
  - If employee has no completed sessions, return "0".
