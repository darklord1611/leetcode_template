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

- **GET_HOURS_ON_DATE(employee_id, date)**
- **GET_HOURS_IN_RANGE(employee_id, start_date, end_date)**
- **GET_TOP_EMPLOYEES_BY_HOURS(n)**
- **GET_EMPLOYEES_BY_DATE(date)**
- **GET_AVERAGE_DAILY_HOURS(employee_id)**

## Level 3 – Overtime & Breaks

Introduce hourly rates and overtime calculation. Standard work day is 8 hours.

- **SET_HOURLY_RATE(employee_id, rate)**
  - Set the hourly rate for an employee.
  - If employee doesn't exist, return "false".
  - Return "true" if set successfully.

- **CALCULATE_OVERTIME_HOURS(employee_id, date)**
  - Calculate overtime hours for an employee on a specific date.
  - Overtime = hours worked - 8 (if > 8, otherwise 0).
  - Return overtime hours as a string (rounded down).
  - If no hours worked that day, return "0".

- **GET_PAY_FOR_DATE(employee_id, date)**
  - Calculate total pay for an employee on a specific date.
  - Pay = (regular_hours * rate) + (overtime_hours * rate * 1.5)
  - regular_hours = min(hours_worked, 8)
  - overtime_hours = max(0, hours_worked - 8)
  - Return pay as a string (rounded down to nearest integer).
  - If hourly rate not set or no hours worked, return "0".

- **ADD_BREAK(timestamp_start, timestamp_end, employee_id)**
  - Record a break period that should be subtracted from work hours.
  - Break must be during an active clock-in session.
  - If employee not clocked in during this period, return "false".
  - Return "true" if break added successfully.
  - Note: Breaks reduce the hours calculated for the day.

- **GET_TOTAL_PAY(employee_id)**
  - Calculate total pay for an employee across all days worked.
  - Return total pay as a string (rounded down).
  - If hourly rate not set, return "0".

- **GET_EMPLOYEES_WITH_OVERTIME(date)**
  - Get all employees who worked overtime (>8 hours) on a specific date.
  - Return comma-separated list of employee_ids sorted alphabetically.
  - If no employees with overtime, return "" (empty string).
