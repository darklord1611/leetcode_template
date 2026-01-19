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
