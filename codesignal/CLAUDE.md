# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a mock CodeSignal Industry Coding Framework assessment repository designed to help developers prepare for technical pre-screen assessments. It contains practice problems that simulate the structure and complexity of real CodeSignal assessments.

## Python Version Requirement

**CRITICAL**: CodeSignal uses Python 3.13.1. All development and testing should use this specific version to match the assessment environment exactly. When installing dependencies or running tests, ensure you're using Python 3.13.1.

## Installation

Install required dependencies (numpy, sortedcontainers):
```bash
pip install -r requirements.txt
```

Or with a specific Python version:
```bash
/path/to/python3.13.1 -m pip install -r requirements.txt
```

## Test Running Commands

Tests are organized by level (test_group_1 through test_group_4). Run tests for specific levels using unittest:

```bash
# Level 1 tests
python3 -m unittest test_simulation.TestSimulateCodingFramework.test_group_1

# Level 2 tests
python3 -m unittest test_simulation.TestSimulateCodingFramework.test_group_2

# Level 3 tests
python3 -m unittest test_simulation.TestSimulateCodingFramework.test_group_3

# Level 4 tests
python3 -m unittest test_simulation.TestSimulateCodingFramework.test_group_4

# Run all tests
python3 -m unittest test_simulation.TestSimulateCodingFramework
```

## Repository Structure

```
practice_assessments/
├── banking_system/         # Bank account management with transactions
├── file_storage/           # File hosting service with TTL
├── in_memory_database/     # Key-value database with backup/restore
├── recipe_manager/         # Recipe and meal planning system
├── task_management_system/ # Task tracking with dependencies
└── working_hour_register/  # Employee time tracking and payroll
```

Each assessment directory contains:
- `simulation.py` - Implementation file (where you write solutions)
- `test_simulation.py` - Test cases for all levels
- `level1.md` through `level4.md` - Requirements for each level

## Assessment Architecture

### Core Design Pattern

Each practice assessment follows this structure:

1. **Main Function**: `simulate_coding_framework(list_of_lists)` - Takes a list of command lists and returns a list of result strings
2. **Command Format**: Each command is a list with the operation name followed by parameters
3. **Progressive Levels**: Each level builds on the previous, requiring refactoring to support new functionality

### Available Practice Assessments

#### 1. Banking System
**Focus**: Account management, transactions, scheduled payments, account merging
- **Level 1**: CREATE_ACCOUNT, DEPOSIT, WITHDRAW, TRANSFER with validation
- **Level 2**: TOP_SPENDERS, GET_PAYMENT_HISTORY with aggregation queries
- **Level 3**: SCHEDULE_PAYMENT with delays, ACCEPT_PAYMENT for 2FA on large transactions
- **Level 4**: MERGE_ACCOUNTS, GET_BANK_STATISTICS, CASHBACK rewards

#### 2. File Storage
**Focus**: File hosting service with TTL and time-based rollback
- **Level 1**: FILE_UPLOAD, FILE_GET, FILE_COPY with basic error handling
- **Level 2**: FILE_SEARCH with prefix matching and sorting by size
- **Level 3**: Time-aware operations with TTL (time-to-live) support
- **Level 4**: ROLLBACK to previous timestamps with TTL recalculation

#### 3. In-Memory Database
**Focus**: Key-value storage with field-level granularity, TTL, backup/restore
- **Level 1**: SET_FIELD, GET_FIELD, DELETE_FIELD, GET with nested structure
- **Level 2**: SCAN by prefix, SCAN_BY_FIELD, TOP_N_KEYS by field count
- **Level 3**: TTL support with SET_FIELD_WITH_TTL and time-aware queries
- **Level 4**: BACKUP, RESTORE with TTL recalculation, COMPARE backups

#### 4. Recipe Manager
**Focus**: Recipe management with ingredients, nutritional info, meal planning
- **Level 1**: ADD_RECIPE, ADD_INGREDIENT, GET_RECIPE, REMOVE_INGREDIENT
- **Level 2**: ADD_INGREDIENT_WITH_PROPS (calories, cost), GET_TOTAL_CALORIES, FIND_RECIPES_BY_INGREDIENT
- **Level 3**: SCALE_RECIPE for servings, ADD_RECIPE_TAG, FIND_RECIPES_IN_BUDGET
- **Level 4**: CREATE_MEAL_PLAN, GET_MEAL_PLAN_SHOPPING_LIST, SUGGEST_SIMILAR_RECIPES, OPTIMIZE_MEAL_PLAN

#### 5. Task Management System
**Focus**: Task tracking with priorities, deadlines, dependencies, history
- **Level 1**: CREATE_TASK, UPDATE_STATUS, UPDATE_PRIORITY, DELETE_TASK
- **Level 2**: GET_TASKS_BY_USER, GET_TASKS_BY_STATUS, TOP_PRIORITY_TASKS, REASSIGN_TASK
- **Level 3**: CREATE_TASK_WITH_DEADLINE, ADD_DEPENDENCY with circular detection, GET_OVERDUE_TASKS, GET_AVAILABLE_TASKS
- **Level 4**: GET_TASK_HISTORY, GET_USER_STATISTICS, GET_CRITICAL_PATH, PREDICT_COMPLETION

#### 6. Working Hour Register
**Focus**: Employee time tracking, overtime calculation, payroll, shift management
- **Level 1**: CLOCK_IN, CLOCK_OUT, GET_TOTAL_HOURS, IS_CLOCKED_IN
- **Level 2**: GET_HOURS_ON_DATE, GET_HOURS_IN_RANGE, GET_TOP_EMPLOYEES_BY_HOURS, GET_AVERAGE_DAILY_HOURS
- **Level 3**: SET_HOURLY_RATE, CALCULATE_OVERTIME_HOURS, GET_PAY_FOR_DATE, ADD_BREAK
- **Level 4**: CREATE_SHIFT, ASSIGN_SHIFT, GENERATE_PAYROLL_REPORT, GET_SHIFT_STATISTICS, CALCULATE_WEEKLY_OVERTIME

### Key Implementation Considerations

1. **Incremental Development**: Implement one level at a time, refactoring as needed
2. **Return Format**: The function returns a list of strings describing operation results
3. **Time Handling**: Level 3+ uses ISO 8601 timestamps (e.g., "2021-07-01T12:00:00")
4. **Method Signature**: Never change the `simulate_coding_framework(list_of_lists)` signature
5. **Available Libraries**: numpy and sortedcontainers are available (see requirements.txt)

## Expected Time Per Level

These are reference times from real CodeSignal assessments:

- Level 1: 10-15 minutes
- Level 2: 20-30 minutes
- Level 3: 30-60 minutes
- Level 4: 30-60 minutes

Total assessment time: 90 minutes (though all levels may take 90-165 minutes to complete fully)

## Choosing an Assessment to Practice

Each assessment tests different aspects of software engineering:

- **Banking System**: Financial transactions, state management, scheduled operations
- **File Storage**: TTL management, time-based operations, rollback functionality
- **In-Memory Database**: Nested data structures, backup/restore, data persistence
- **Recipe Manager**: Aggregations, filtering, optimization algorithms
- **Task Management System**: Graph algorithms (dependencies), analytics, predictive modeling
- **Working Hour Register**: Time calculations, date ranges, payroll logic

Start with the assessment that aligns with your target company's domain or the skills you want to practice.

## Contributing New Assessments

New practice assessments should:
1. Follow the same structure as existing assessments (e.g., `banking_system/`, `file_storage/`)
2. Be placed in a new subdirectory under `practice_assessments/`
3. Include level*.md files describing requirements for each level
4. Include simulation.py (implementation template) and test_simulation.py (comprehensive tests)
5. Follow the ICF pattern: Level 1 (basic CRUD), Level 2 (queries/filtering), Level 3 (refactoring/advanced features), Level 4 (complex operations/analytics)
6. Follow guidelines in the PDF: "CodeSignal Skills Evaluation Framework.pdf"
