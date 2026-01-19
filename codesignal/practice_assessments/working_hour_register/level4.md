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

- **SET_HOURLY_RATE(employee_id, rate)**
- **CALCULATE_OVERTIME_HOURS(employee_id, date)**
- **GET_PAY_FOR_DATE(employee_id, date)**
- **ADD_BREAK(timestamp_start, timestamp_end, employee_id)**
- **GET_TOTAL_PAY(employee_id)**
- **GET_EMPLOYEES_WITH_OVERTIME(date)**

## Level 4 – Shift Management & Payroll Reports

- **CREATE_SHIFT(shift_id, start_time, end_time, shift_type)**
  - Create a shift template with specific hours and type.
  - shift_type: "MORNING", "EVENING", "NIGHT"
  - start_time and end_time in format "HH:MM" (24-hour format)
  - If shift_id already exists, return "false".
  - Return "true" if created successfully.

- **ASSIGN_SHIFT(employee_id, date, shift_id)**
  - Assign a shift to an employee for a specific date.
  - If employee or shift doesn't exist, return "false".
  - Return "true" if assigned successfully.

- **GET_SHIFT_COMPLIANCE(employee_id, date)**
  - Check if employee's actual hours match their assigned shift.
  - Return "compliant" if within 30 minutes of shift hours.
  - Return "under" if worked significantly less than shift.
  - Return "over" if worked significantly more than shift.
  - Return "" if no shift assigned or no hours worked.

- **GENERATE_PAYROLL_REPORT(start_date, end_date)**
  - Generate payroll summary for all employees in date range.
  - Format: "emp_id1(total_pay1), emp_id2(total_pay2)"
  - Order by total_pay descending, then by employee_id alphabetically.
  - Only include employees who worked in this period.
  - If no employees, return "" (empty string).

- **GET_SHIFT_STATISTICS(shift_type, start_date, end_date)**
  - Get statistics for a specific shift type in a date range.
  - Format: "total_hours:{hours},employees:{count},avg_hours:{avg}"
  - total_hours: sum of all hours worked by employees assigned to this shift type
  - employees: count of unique employees who worked this shift
  - avg_hours: average hours per employee (rounded down)
  - If no data for shift type, return "total_hours:0,employees:0,avg_hours:0".

- **FIND_UNCOVERED_SHIFTS(date)**
  - Find all shifts assigned to employees who didn't work on that date.
  - Return comma-separated list of "employee_id:shift_id" sorted alphabetically.
  - If all shifts were covered, return "" (empty string).

- **EXPORT_TIMESHEET(employee_id, start_date, end_date)**
  - Generate detailed timesheet for an employee.
  - Format: "date1(hours1), date2(hours2), date3(hours3)"
  - Order by date ascending.
  - Only include dates where hours > 0.
  - If no hours in range, return "" (empty string).

- **CALCULATE_WEEKLY_OVERTIME(employee_id, week_start_date)**
  - Calculate overtime for a week (7 days starting from week_start_date).
  - Weekly overtime: hours worked > 40 in the week.
  - Return overtime hours as a string (rounded down).
  - If total hours <= 40, return "0".
