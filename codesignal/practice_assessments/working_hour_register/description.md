> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified version of a **working hour register**:
a system that tracks when employees clock in and out, answers questions about
the hours they have worked, and computes pay. All operations that should be
supported are listed below. Partial credit will be granted for each test
passed, so press "Submit" often to run tests and receive partial credits for
passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the
operations and complete the levels one by one, keeping in mind that **you will
need to reopen and refactor functions you wrote in earlier levels** so they
satisfy the additional requirements introduced later. The set of functions is
intentionally small; most of the difficulty comes from extending the
*behaviour* of the same functions across levels. Please, do not change the
existing method signatures.

## Task

All timestamps, durations, hours and pay are **integers**, and timestamps are
**non-decreasing** across calls. Every value is returned as a string. A
"session" is one completed clock-in/clock-out pair; its raw duration is
`clock_out_time - clock_in_time`.

---

## Level 1 – Clock In / Out

- **clock_in(timestamp, employee_id)**
  - Clock the employee in at `timestamp`. The employee is auto-created on their
    first `clock_in`.
  - Return "false" if the employee is already clocked in (an open session
    exists); otherwise start a session and return "true".

- **clock_out(timestamp, employee_id)**
  - Close the employee's open session.
  - Return the just-finished session's duration (`timestamp - clock_in_time`)
    as a string, or "" if the employee was not clocked in.

- **is_clocked_in(timestamp, employee_id)**
  - Return "true" if the employee currently has an open session, otherwise
    "false" (including for unknown employees).

- **get_total_hours(timestamp, employee_id)**
  - Return the sum of all **completed** session durations for the employee.
  - Return "0" if the employee has no completed sessions or does not exist. An
    open (not-yet-closed) session does not count.

---

## Level 2 – Range Queries

Read-only additions; no earlier function changes behaviour at this level.

- **get_hours_in_range(timestamp, employee_id, start, end)**
  - Return the total **completed** worked time that falls within the half-open
    window `[start, end)`. Each completed session is clipped to the window: a
    session `[in, out)` contributes `max(0, min(out, end) - max(in, start))`.
  - Return "0" if there is no overlapping completed time / unknown employee.

- **get_top_employees_by_hours(timestamp, n)**
  - Return the top `n` employees ranked by total completed hours, in descending
    order; ties broken by `employee_id` in ascending order.
  - Format: `"id1(hours1), id2(hours2), ..."`. If there are fewer than `n`
    employees, return all of them. Only completed sessions count. Return "" if
    there are no employees.

---

## Level 3 – Breaks & Overtime Pay

This level **reopens `clock_out`, `get_total_hours`, and `get_hours_in_range`**
so that recorded breaks are subtracted from worked time.

- **set_hourly_rate(timestamp, employee_id, rate)**
  - Set the employee's hourly pay rate.
  - Return "true" if set, "false" if the employee does not exist.

- **add_break(timestamp, employee_id, start, end)**
  - Record an unpaid break `[start, end)`. The break must lie **entirely within
    a single completed session** (`session_in <= start < end <= session_out`).
    Its duration `end - start` is subtracted from that session's worked time.
  - Return "true" if it was applied to exactly one session, otherwise "false"
    (no enclosing completed session, or `start >= end`). A session's worked
    time can never go below 0.

- **clock_out** *(updated)*
  - Still returns the session's raw duration (`timestamp - clock_in_time`).
    What changes is that this completed session is now the unit that
    `add_break` subtracts from and that `get_total_hours` /
    `get_hours_in_range` measure: those queries report the session's worked
    time **net of any breaks** later attached to it. The return value of
    `clock_out` itself is unaffected by breaks (breaks are added afterwards).

- **get_pay(timestamp, employee_id)**
  - Let `H` be the employee's total completed worked hours (net of breaks, as
    reported by `get_total_hours`) and `rate` the hourly rate. With an overtime
    threshold `OT_THRESHOLD = 40`:
    - `regular = min(H, OT_THRESHOLD)`
    - `overtime = max(0, H - OT_THRESHOLD)`
    - `pay = rate * regular + (rate * overtime * 3) // 2`
      (overtime is paid at 1.5x; the `* 3 // 2` keeps it integer).
  - Return the pay as a string, or "0" if no rate has been set or `H` is 0.

---

## Level 4 – Range Pay & Payroll

The pay calculation is **reopened and shared** by `get_pay`,
`get_pay_in_range`, and `generate_payroll`.

- **get_pay_in_range(timestamp, employee_id, start, end)**
  - Same overtime formula as `get_pay`, but `H` is the worked hours within the
    window `[start, end)` (net of breaks), i.e. the value
    `get_hours_in_range` would report. The `OT_THRESHOLD = 40` rule is applied
    to that windowed `H`.
  - Return the pay as a string, or "0" if no rate has been set or `H` is 0.

- **generate_payroll(timestamp, start, end)**
  - For every employee with worked hours in `[start, end)`, compute their pay
    using the same windowed rule as `get_pay_in_range`.
  - Return `"id1(pay1), id2(pay2), ..."` sorted by `employee_id` ascending.
    Employees whose computed pay is 0 are excluded (this covers both employees
    with no worked hours in the window and employees with hours but no hourly
    rate set). Return "" if no employee has non-zero pay in the window.
