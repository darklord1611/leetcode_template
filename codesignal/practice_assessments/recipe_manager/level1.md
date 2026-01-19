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
