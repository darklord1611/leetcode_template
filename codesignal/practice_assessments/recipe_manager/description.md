> ⚠️ **Disclaimer:** This is a fictional practice problem created for interview preparation only.
> It is **not** an official CodeSignal problem and is not affiliated with, authorized by, or endorsed by
> CodeSignal or any company. Any resemblance to real assessment content is coincidental.

# Scenario

Your task is to implement a simplified version of a **recipe manager**.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, keeping in mind that **you will need to reopen and refactor functions you wrote in earlier
levels** so they satisfy the additional requirements introduced later. The set of functions is intentionally small;
most of the difficulty comes from extending the *behaviour* of the same functions across levels. The central
evolving functions are the recipe **totals** (`get_total_calories` / `get_total_cost`): they are introduced in
Level 2, reopened in Level 3 for per-serving scaling, and reopened again in Level 4 to aggregate across recipes.
Please, do not change the existing method signatures.

## Task

All quantities, calories, costs, and servings are **non-negative integers** (servings are always `>= 1`). All
timestamps are integers and are **non-decreasing** across calls; every stateful method takes `timestamp` as its
first parameter even when a level does not use it. Counts and totals are returned as plain integer strings (e.g.
"1500"); failures return "" (empty string) unless stated otherwise. All per-serving and per-recipe divisions use
**floor division** (`//`), and test data is chosen so divisions are exact wherever it matters.

---

## Level 1 – Basic Recipe CRUD

- **add_recipe(timestamp, recipe_name)**
  - Create a new recipe. A new recipe has **1 serving** by default and no ingredients.
  - Return "false" if a recipe with that name already exists, otherwise "true".

- **add_ingredient(timestamp, recipe_name, ingredient_name, quantity)**
  - Add `quantity` (an int) of `ingredient_name` to the recipe. If the ingredient is already present, **add** to
    its existing quantity.
  - Return "true" on success, or "" if the recipe does not exist.

- **get_recipe(timestamp, recipe_name)**
  - Return the recipe's ingredients as `"ingredient:quantity"` pairs sorted by ingredient name ascending, joined
    by ", " (e.g. `"egg:2, flour:300"`).
  - Return "" if the recipe does not exist. A recipe that exists but currently has no ingredients also returns ""
    (the empty string).

- **remove_ingredient(timestamp, recipe_name, ingredient_name)**
  - Remove `ingredient_name` from the recipe entirely.
  - Return "true" if it was removed; "false" if the recipe or the ingredient does not exist.

- **delete_recipe(timestamp, recipe_name)**
  - Delete the recipe.
  - Return "true" if deleted; "false" if the recipe does not exist.

---

## Level 2 – Ingredient Properties & Totals

Ingredient nutritional/cost properties are **global per ingredient name** and shared across every recipe that uses
that ingredient. This level introduces the recipe **totals**, which later levels reopen.

- **set_ingredient_info(timestamp, ingredient_name, calories_per_unit, cost_per_unit)**
  - Set the global calories-per-unit and cost-per-unit for `ingredient_name` (overwriting any previous values).
  - Ingredients without info default to `0` calories and `0` cost per unit.
  - Return "true".

- **get_total_calories(timestamp, recipe_name)**
  - Return the sum over the recipe's ingredients of `quantity * calories_per_unit`, as a string.
  - Return "" if the recipe does not exist (a recipe with no ingredients returns "0").

- **get_total_cost(timestamp, recipe_name)**
  - Return the sum over the recipe's ingredients of `quantity * cost_per_unit`, as a string.
  - Return "" if the recipe does not exist (a recipe with no ingredients returns "0").

- **find_recipes_by_ingredient(timestamp, ingredient_name)**
  - Return the names of all recipes that currently contain `ingredient_name`, sorted ascending and joined by ", ".
  - Return "" if no recipe contains it.

---

## Level 3 – Servings & Scaling

A recipe yields a number of servings. The totals from Level 2 are **reopened** to support per-serving values.

- **set_servings(timestamp, recipe_name, servings)**
  - Set the number of servings the recipe yields (`servings >= 1`).
  - Return "true", or "" if the recipe does not exist.

- **get_calories_per_serving(timestamp, recipe_name)** *(updated — reopens the totals)*
  - Return `get_total_calories // servings` (floor division), as a string.
  - Return "" if the recipe does not exist.

- **get_cost_per_serving(timestamp, recipe_name)** *(updated — reopens the totals)*
  - Return `get_total_cost // servings` (floor division), as a string.
  - Return "" if the recipe does not exist.

- **find_recipes_in_budget(timestamp, max_cost_per_serving)**
  - Return the names of all recipes whose **cost per serving** is `<= max_cost_per_serving`, sorted by
    `(cost_per_serving ascending, recipe_name ascending)`, joined by ", ".
  - Return "" if no recipe qualifies.

---

## Level 4 – Meal Plans

A meal plan requests a number of servings of one or more recipes. The totals are **reopened** again to aggregate
scaled ingredient quantities and costs across every recipe in the plan.

- **create_meal_plan(timestamp, plan_name)**
  - Create a new, empty meal plan.
  - Return "false" if a plan with that name already exists, otherwise "true".

- **add_recipe_to_plan(timestamp, plan_name, recipe_name, servings)**
  - Record that the plan needs `servings` servings of `recipe_name`. If the recipe is already in the plan, **add**
    to the requested servings.
  - Return "true", or "" if the plan or the recipe does not exist.

- **get_plan_shopping_list(timestamp, plan_name)** *(updated — reopens the totals across recipes)*
  - For each recipe in the plan, scale each ingredient quantity to the requested servings:
    `scaled = quantity * requested_servings // recipe_default_servings` (floor division). Sum the scaled
    quantities of the **same ingredient name across all recipes** in the plan.
  - Return the aggregated quantities as `"ingredient:quantity"` sorted by ingredient name ascending, joined by ", ".
  - Return "" if the plan does not exist or is empty.

- **get_plan_cost(timestamp, plan_name)** *(updated — reopens the totals across recipes)*
  - For each recipe in the plan, the scaled cost is `recipe_total_cost * requested_servings // recipe_default_servings`
    (floor division). Return the sum of scaled costs across all recipes in the plan, as a string.
  - Return "" if the plan does not exist (an existing empty plan returns "0").
