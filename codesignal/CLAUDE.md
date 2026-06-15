# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a mock CodeSignal Industry Coding Framework (ICF) assessment repository designed to help developers prepare for technical pre-screen assessments. It contains practice problems that simulate the structure and progressive nature of real CodeSignal assessments.

## Python Version Requirement

**CRITICAL**: CodeSignal uses Python 3.13.1. Develop and test against this version to match the assessment environment. Use only the standard library plus what is in `requirements.txt` (numpy, sortedcontainers).

## Installation

```bash
pip install -r requirements.txt
```

## Repository Structure

```
practice_assessments/
├── banking_system/         # Accounts, scheduled payments, merges        (4 levels)
├── cache_system/           # LRU/TTL/dependency cache with namespaces     (7 levels)
├── dns_resolver/           # A-records, CNAME, round-robin, wildcards     (7 levels)
├── file_storage/           # File hosting service with TTL and rollback   (4 levels)
├── in_memory_database/     # Key-value DB with TTL and backup/restore     (4 levels)
├── recipe_manager/         # Recipes, scaling, meal planning              (4 levels)
├── task_management_system/ # Tasks, dependencies, critical path           (4 levels)
└── working_hour_register/  # Clock in/out, breaks, overtime, payroll      (4 levels)
└── reference/              # integer_container — minimal canonical example
```

### Files in each assessment directory

| File | Role |
|------|------|
| `<name>.py` | **Abstract base class** — the interface. Every method has a docstring + return contract and raises `NotImplementedError`. Methods are grouped by `# Level N Methods:` comments. |
| `<name>_impl.py` | **Implementation stub** — a subclass of the ABC where you write your solution. Ships with every method bodied as `# TODO: implement` + `pass`. This is the only file the solver edits. |
| `description.md` | Single-file spec covering all levels progressively (newer problems). Some older problems instead have cumulative `level1.md … level4.md` files. |
| `tests/level_N_tests.py` | One `unittest` file per level (`LevelNTests`), comprehensive deterministic cases, each decorated `@timeout(0.4)`. |
| `main.sh` | Runs all levels: `python3 -m unittest discover -s tests -p '*.py'`. |
| `run_single_test.sh` | Runs one case: `sh run_single_test.sh test_level_2_case_03`. |
| `timeout_decorator.py` | SIGALRM-based `@timeout(seconds)`; identical copy in every dir. |

> **Indentation is TABS** in all Python files. Match it exactly.

## Test Running Commands

```bash
cd practice_assessments/<assessment>
sh main.sh                                                   # all levels
python3 -m unittest discover -s tests -p '*.py' -k level_2   # one level
sh run_single_test.sh test_level_2_case_03                   # one case
```

## Assessment Architecture

### Core Design Pattern

Each assessment is a single class (the `*_impl.py` subclass of the ABC) — there is **no** `simulate_coding_framework` dispatcher. The solver implements real methods that hold instance state.

1. **Methods, not commands.** Each operation is a method on the class with a fixed signature.
2. **`timestamp` first.** Every stateful method takes `timestamp: int` as its first parameter, even at levels that ignore it, so time-based behaviour can be added in later levels **without changing signatures**.
3. **String returns.** Operations return strings (`"true"`, `"false"`, `""`, numbers as strings, or formatted lists). Failures generally return `""`.

### The "evolve the core" principle (most important)

These problems are deliberately built so that a **small set of core functions is reopened and extended across levels**, rather than each level bolting on a batch of independent new functions. A later level adds an edge case or a new requirement that the earlier level was told to ignore, forcing you to **rewrite the body of an existing function** (its name and signature stay the same). New functions are introduced only when genuinely needed; pure-introspection helpers are avoided.

Examples of the evolving core:
- **banking_system**: `deposit`/`pay`/`transfer` are reopened at L2 (accrue outgoing totals → `top_spenders`), again at L3 (every operation must first execute scheduled payments now due), and again at L4 (resolve merged-away accounts).
- **dns_resolver**: `resolve` is reopened at every level — L2 CNAME chains, L3 round-robin over multiple IPs, L4 skip expired records, L5 wildcard fallback, L7 weighted round-robin.
- **cache_system**: `put`/`get` are reopened for LRU eviction (L2), TTL expiry (L3), cascading dependency invalidation (L4), and pinning (L5).
- **recipe_manager**: the calorie/cost **totals** are reopened for ingredient properties (L2), per-serving scaling (L3), and meal-plan aggregation (L4).
- **task_management_system**: `update_status` is reopened so transitions are blocked until dependencies are `done` (L3) and for completion analytics (L4).
- **working_hour_register**: `get_total_hours`/pay calculation is reopened for break subtraction and overtime (L3) and shared across range/payroll queries (L4).

The canonical ICF level progression still holds: **L1** basic CRUD → **L2** queries/filtering/ranking → **L3** refactor for time/edge-cases → **L4** complex operations/analytics. (cache_system and dns_resolver extend this to 7 levels.)

### Source of truth for an assessment's spec

Read that assessment's `description.md` (or `level*.md`). The ABC (`<name>.py`) documents every method's exact return contract; the tests encode the precise expected values. Don't infer behaviour from this file — it only summarizes.

## Key Implementation Considerations

1. **Implement one level at a time**, expecting to reopen earlier functions.
2. **Never change a method signature** — extend the body instead.
3. **Backward compatibility**: each level's new behaviour should be a superset of the previous, so earlier-level tests keep passing.
4. **Determinism**: prefer integer arithmetic and explicit tie-break rules (documented in `description.md`) so tests are reproducible.

## Expected Time Per Level

Reference times from real CodeSignal assessments (per 4-level assessment, ~90 minutes total):

- Level 1: 10–15 min  •  Level 2: 20–30 min  •  Level 3: 30–60 min  •  Level 4: 30–60 min

## Contributing / Refactoring Assessments

A new or refactored assessment should:

1. Live in its own subdirectory under `practice_assessments/`, copying `main.sh`, `run_single_test.sh`, and `timeout_decorator.py` from an existing problem (e.g. `banking_system`).
2. Ship four files of substance: `<name>.py` (ABC), `<name>_impl.py` (TODO stub), `description.md` (single progressive spec), and `tests/level_N_tests.py` for each level.
3. **Keep the function set small and design for the evolve-the-core principle** above. Mark reopened functions `*(updated)*` in `description.md` and state what changed.
4. Give every stateful method `timestamp: int` as the first parameter; return strings; use TAB indentation.
5. **Validate before shipping**: temporarily write a complete reference solution into `<name>_impl.py`, run `python3 -m unittest discover -s tests -p '*.py'` until it prints `OK` with zero failures (this proves the tests' expected values are correct), then restore the empty stub so the solver starts from scratch.
6. Follow the guidelines in "CodeSignal Skills Evaluation Framework.pdf".
