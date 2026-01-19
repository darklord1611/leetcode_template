# Scenario

Your task is to implement a simplified version of a recipe management system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press "Submit" often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of recipe management system with various recipes:

```plaintext
[RecipeManager]
    Recipe: "pasta_carbonara"
        ingredient: "pasta" -> 200g
        ingredient: "bacon" -> 100g
        ingredient: "eggs" -> 2 units
    Recipe: "caesar_salad"
        ingredient: "lettuce" -> 150g
        ingredient: "croutons" -> 50g
```

## Level 1 – Initial Design & Basic Functions

- **ADD_RECIPE(recipe_name)**
  - Add a new recipe with the given recipe_name.
  - If a recipe with the same name already exists, return "false".
  - Otherwise, create an empty recipe and return "true".

- **ADD_INGREDIENT(recipe_name, ingredient_name, quantity)**
  - Add an ingredient with quantity to a recipe.
  - quantity is a positive integer.
  - If the recipe doesn't exist, return "" (empty string).
  - If the ingredient already exists in this recipe, update its quantity.
  - Return the quantity as a string.

- **GET_RECIPE(recipe_name)**
  - Get all ingredients for a recipe.
  - Return a string in the format: "ingredient1(quantity1), ingredient2(quantity2)"
  - Ingredients should be sorted alphabetically by ingredient name.
  - If the recipe doesn't exist or has no ingredients, return "" (empty string).

- **REMOVE_INGREDIENT(recipe_name, ingredient_name)**
  - Remove a specific ingredient from a recipe.
  - If the recipe or ingredient doesn't exist, return "false".
  - Otherwise, return "true".

- **DELETE_RECIPE(recipe_name)**
  - Delete an entire recipe.
  - If the recipe doesn't exist, return "false".
  - Otherwise, delete the recipe and return "true".

## Level 2 – Aggregations & Filtering

Now ingredients have additional properties: calories (per unit) and cost (per unit).

- **ADD_INGREDIENT_WITH_PROPS(recipe_name, ingredient_name, quantity, calories_per_unit, cost_per_unit)**
  - Add an ingredient with quantity, calories per unit, and cost per unit.
  - If the recipe doesn't exist, return "" (empty string).
  - If the ingredient already exists, update all its properties.
  - Return the quantity as a string.

- **GET_TOTAL_CALORIES(recipe_name)**
  - Calculate total calories for a recipe (sum of quantity * calories_per_unit for all ingredients).
  - If the recipe doesn't exist, return "" (empty string).
  - Return the total as a string.

- **GET_TOTAL_COST(recipe_name)**
  - Calculate total cost for a recipe (sum of quantity * cost_per_unit for all ingredients).
  - If the recipe doesn't exist, return "" (empty string).
  - Return the total as a string (rounded down to nearest integer).

- **FIND_RECIPES_BY_INGREDIENT(ingredient_name)**
  - Find all recipes that contain the specified ingredient.
  - Return a comma-separated list of recipe names sorted alphabetically.
  - If no recipes contain this ingredient, return "" (empty string).
  - Example: "pasta_carbonara, spaghetti_bolognese"

- **GET_MOST_EXPENSIVE_RECIPES(n)**
  - Return the top n recipes by total cost.
  - Format: "recipe1(cost1), recipe2(cost2), recipe3(cost3)"
  - Order by total cost in descending order, then by recipe name alphabetically for ties.
  - If there are fewer than n recipes, return all recipes.

## Level 3 – Recipe Scaling & Serving Sizes

Recipes now have a base serving size. Implement operations to scale recipes and filter by dietary constraints.

- **SET_SERVING_SIZE(recipe_name, servings)**
  - Set the base serving size for a recipe.
  - The current ingredient quantities represent this many servings.
  - If the recipe doesn't exist, return "" (empty string).
  - Return the servings as a string.

- **SCALE_RECIPE(recipe_name, target_servings)**
  - Calculate scaled ingredient quantities for the target number of servings.
  - Format: "ingredient1(scaled_qty1), ingredient2(scaled_qty2)"
  - Quantities should be rounded down to nearest integer.
  - Ingredients sorted alphabetically.
  - If the recipe doesn't exist or serving size not set, return "" (empty string).
  - Formula: scaled_quantity = (original_quantity * target_servings) / base_servings

- **GET_CALORIES_PER_SERVING(recipe_name)**
  - Calculate calories per serving (total_calories / base_servings).
  - If recipe doesn't exist or serving size not set, return "" (empty string).
  - Return rounded down to nearest integer.

- **ADD_RECIPE_TAG(recipe_name, tag)**
  - Add a dietary tag to a recipe (e.g., "vegetarian", "vegan", "gluten-free", "low-carb").
  - If recipe doesn't exist, return "false".
  - Return "true" if tag added successfully.

- **FIND_RECIPES_BY_TAG(tag)**
  - Find all recipes with the specified tag.
  - Return comma-separated list of recipe names sorted alphabetically.
  - If no recipes have this tag, return "" (empty string).

- **FIND_RECIPES_IN_BUDGET(max_cost_per_serving)**
  - Find all recipes where cost per serving <= max_cost_per_serving.
  - Cost per serving = total_cost / base_servings.
  - Return comma-separated list of recipe names sorted alphabetically.
  - Only include recipes with serving size set.
  - If no recipes match, return "" (empty string).

## Level 4 – Meal Planning & Ingredient Inventory

- **CREATE_MEAL_PLAN(meal_plan_name)**
  - Create a new meal plan (a collection of recipes).
  - If a meal plan with this name already exists, return "false".
  - Return "true" if created successfully.

- **ADD_RECIPE_TO_MEAL_PLAN(meal_plan_name, recipe_name, servings)**
  - Add a recipe with specified servings to a meal plan.
  - If meal plan or recipe doesn't exist, return "" (empty string).
  - If recipe already in meal plan, update the servings.
  - Return the servings as a string.

- **GET_MEAL_PLAN_SHOPPING_LIST(meal_plan_name)**
  - Get aggregated shopping list for all recipes in the meal plan.
  - Combine quantities for the same ingredient across recipes (accounting for scaling).
  - Format: "ingredient1(total_qty), ingredient2(total_qty)"
  - Ingredients sorted alphabetically.
  - Quantities rounded down to nearest integer.
  - If meal plan doesn't exist or is empty, return "" (empty string).

- **GET_MEAL_PLAN_COST(meal_plan_name)**
  - Calculate total cost for all recipes in the meal plan (accounting for scaling).
  - If meal plan doesn't exist, return "" (empty string).
  - Return total cost rounded down to nearest integer.

- **GET_MEAL_PLAN_CALORIES(meal_plan_name)**
  - Calculate total calories for all recipes in the meal plan (accounting for scaling).
  - If meal plan doesn't exist, return "" (empty string).
  - Return total calories as a string.

- **SUGGEST_SIMILAR_RECIPES(recipe_name, n)**
  - Find n most similar recipes based on shared ingredients.
  - Similarity score = number of common ingredients.
  - Format: "recipe1(score1), recipe2(score2), recipe3(score3)"
  - Order by similarity score descending, then by recipe name alphabetically for ties.
  - Exclude the input recipe itself from results.
  - If recipe doesn't exist or there are no other recipes, return "" (empty string).
  - If fewer than n similar recipes exist, return all available.

- **OPTIMIZE_MEAL_PLAN(meal_plan_name, max_total_calories, max_total_cost)**
  - Remove recipes from meal plan to satisfy both calorie and cost constraints.
  - Remove recipes with lowest calorie-to-cost ratio first (cost/calories).
  - Keep removing until both constraints are satisfied or meal plan is empty.
  - Return comma-separated list of removed recipe names in the order they were removed.
  - If meal plan doesn't exist, return "" (empty string).
  - If constraints already satisfied, return "" (empty string).
