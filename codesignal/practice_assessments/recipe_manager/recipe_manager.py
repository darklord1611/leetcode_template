"""
Recipe Manager - Abstract Base Class

This class defines the interface for a recipe management system
with recipe CRUD operations, ingredient management, nutritional info, and meal planning.
"""


class RecipeManager:
    """
    Abstract base class for a recipe management system that manages recipes,
    ingredients with nutritional properties, tags, and meal plans.
    """

    def __init__(self):
        """Initialize the recipe manager."""
        raise NotImplementedError("Subclasses must implement __init__")

    # Level 1 Methods: Basic Operations

    def add_recipe(self, recipe_name: str) -> str:
        """
        Add a new recipe.

        Args:
            recipe_name (str): Unique identifier for the recipe

        Returns:
            str: "true" if recipe created successfully, "false" if recipe already exists
        """
        raise NotImplementedError("Subclasses must implement add_recipe()")

    def add_ingredient(self, recipe_name: str, ingredient_name: str, quantity: str) -> str:
        """
        Add an ingredient to a recipe or update its quantity.

        Args:
            recipe_name (str): Recipe to add ingredient to
            ingredient_name (str): Name of the ingredient
            quantity (str): Quantity as string (can be numeric or text like "2 cups")

        Returns:
            str: The quantity as string if successful, "" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement add_ingredient()")

    def get_recipe(self, recipe_name: str) -> str:
        """
        Get all ingredients in a recipe.

        Args:
            recipe_name (str): Recipe to query

        Returns:
            str: Formatted string "ingredient1(quantity), ingredient2(quantity), ..."
                 sorted alphabetically by ingredient name, "" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_recipe()")

    def remove_ingredient(self, recipe_name: str, ingredient_name: str) -> str:
        """
        Remove an ingredient from a recipe.

        Args:
            recipe_name (str): Recipe to remove ingredient from
            ingredient_name (str): Ingredient to remove

        Returns:
            str: "true" if removed successfully, "false" if recipe or ingredient doesn't exist
        """
        raise NotImplementedError("Subclasses must implement remove_ingredient()")

    def delete_recipe(self, recipe_name: str) -> str:
        """
        Delete a recipe.

        Args:
            recipe_name (str): Recipe to delete

        Returns:
            str: "true" if deleted successfully, "false" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement delete_recipe()")

    # Level 2 Methods: Nutritional Properties and Queries

    def add_ingredient_with_props(self, recipe_name: str, ingredient_name: str,
                                   quantity: str, calories_per_unit: str, cost_per_unit: str) -> str:
        """
        Add an ingredient with nutritional and cost properties.

        Args:
            recipe_name (str): Recipe to add ingredient to
            ingredient_name (str): Name of the ingredient
            quantity (str): Quantity
            calories_per_unit (str): Calories per unit of quantity
            cost_per_unit (str): Cost per unit of quantity

        Returns:
            str: The quantity as string if successful, "" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement add_ingredient_with_props()")

    def get_total_calories(self, recipe_name: str) -> str:
        """
        Calculate total calories for a recipe.

        Args:
            recipe_name (str): Recipe to query

        Returns:
            str: Total calories as string (quantity * calories_per_unit for all ingredients),
                 "" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_total_calories()")

    def get_total_cost(self, recipe_name: str) -> str:
        """
        Calculate total cost for a recipe.

        Args:
            recipe_name (str): Recipe to query

        Returns:
            str: Total cost as string (quantity * cost_per_unit for all ingredients),
                 "" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_total_cost()")

    def find_recipes_by_ingredient(self, ingredient_name: str) -> str:
        """
        Find all recipes containing a specific ingredient.

        Args:
            ingredient_name (str): Ingredient to search for

        Returns:
            str: Comma-separated list of recipe names sorted alphabetically,
                 "" if no recipes found
        """
        raise NotImplementedError("Subclasses must implement find_recipes_by_ingredient()")

    def get_most_expensive_recipes(self, n: str) -> str:
        """
        Get the N most expensive recipes.

        Args:
            n (str): Number of recipes to return

        Returns:
            str: Formatted string "recipe1(cost), recipe2(cost), ..."
                 sorted by cost descending, then by recipe name ascending
        """
        raise NotImplementedError("Subclasses must implement get_most_expensive_recipes()")

    # Level 3 Methods: Recipe Scaling and Tags

    def set_serving_size(self, recipe_name: str, servings: str) -> str:
        """
        Set the serving size for a recipe.

        Args:
            recipe_name (str): Recipe to update
            servings (str): Number of servings

        Returns:
            str: The servings as string if successful, "" if recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement set_serving_size()")

    def scale_recipe(self, recipe_name: str, target_servings: str) -> str:
        """
        Scale a recipe to a different number of servings.

        Args:
            recipe_name (str): Recipe to scale
            target_servings (str): Target number of servings

        Returns:
            str: Formatted string of scaled ingredients "ingredient1(quantity), ingredient2(quantity), ..."
                 sorted alphabetically, "" if recipe doesn't exist or no serving size set
        """
        raise NotImplementedError("Subclasses must implement scale_recipe()")

    def get_calories_per_serving(self, recipe_name: str) -> str:
        """
        Get calories per serving for a recipe.

        Args:
            recipe_name (str): Recipe to query

        Returns:
            str: Calories per serving as string (total_calories / servings),
                 "" if recipe doesn't exist or no serving size set
        """
        raise NotImplementedError("Subclasses must implement get_calories_per_serving()")

    def add_recipe_tag(self, recipe_name: str, tag: str) -> str:
        """
        Add a tag to a recipe.

        Args:
            recipe_name (str): Recipe to tag
            tag (str): Tag to add

        Returns:
            str: "true" if tag added successfully, "false" if recipe doesn't exist or tag already exists
        """
        raise NotImplementedError("Subclasses must implement add_recipe_tag()")

    def find_recipes_by_tag(self, tag: str) -> str:
        """
        Find all recipes with a specific tag.

        Args:
            tag (str): Tag to search for

        Returns:
            str: Comma-separated list of recipe names sorted alphabetically,
                 "" if no recipes found
        """
        raise NotImplementedError("Subclasses must implement find_recipes_by_tag()")

    def find_recipes_in_budget(self, max_cost_per_serving: str) -> str:
        """
        Find all recipes within a cost per serving budget.

        Args:
            max_cost_per_serving (str): Maximum cost per serving

        Returns:
            str: Comma-separated list of recipe names sorted alphabetically,
                 "" if no recipes found
        """
        raise NotImplementedError("Subclasses must implement find_recipes_in_budget()")

    # Level 4 Methods: Meal Planning

    def create_meal_plan(self, plan_name: str) -> str:
        """
        Create a new meal plan.

        Args:
            plan_name (str): Unique identifier for the meal plan

        Returns:
            str: "true" if meal plan created successfully, "false" if it already exists
        """
        raise NotImplementedError("Subclasses must implement create_meal_plan()")

    def add_recipe_to_meal_plan(self, plan_name: str, recipe_name: str, servings: str) -> str:
        """
        Add a recipe to a meal plan.

        Args:
            plan_name (str): Meal plan to add to
            recipe_name (str): Recipe to add
            servings (str): Number of servings to add

        Returns:
            str: The servings as string if successful,
                 "" if meal plan or recipe doesn't exist
        """
        raise NotImplementedError("Subclasses must implement add_recipe_to_meal_plan()")

    def get_meal_plan_shopping_list(self, plan_name: str) -> str:
        """
        Get aggregated shopping list for a meal plan.

        Args:
            plan_name (str): Meal plan to query

        Returns:
            str: Formatted string "ingredient1(total_quantity), ingredient2(total_quantity), ..."
                 sorted alphabetically, "" if meal plan doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_meal_plan_shopping_list()")

    def get_meal_plan_cost(self, plan_name: str) -> str:
        """
        Calculate total cost for a meal plan.

        Args:
            plan_name (str): Meal plan to query

        Returns:
            str: Total cost as string, "" if meal plan doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_meal_plan_cost()")

    def get_meal_plan_calories(self, plan_name: str) -> str:
        """
        Calculate total calories for a meal plan.

        Args:
            plan_name (str): Meal plan to query

        Returns:
            str: Total calories as string, "" if meal plan doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_meal_plan_calories()")

    def suggest_similar_recipes(self, recipe_name: str, n: str) -> str:
        """
        Suggest N similar recipes based on shared ingredients.

        Args:
            recipe_name (str): Recipe to find similar recipes for
            n (str): Number of suggestions to return

        Returns:
            str: Formatted string "recipe1(shared_count), recipe2(shared_count), ..."
                 sorted by shared ingredient count descending, then by recipe name ascending
        """
        raise NotImplementedError("Subclasses must implement suggest_similar_recipes()")

    def optimize_meal_plan(self, plan_name: str, max_calories: str, max_cost: str) -> str:
        """
        Optimize a meal plan by removing recipes to fit within calorie and cost constraints.

        Args:
            plan_name (str): Meal plan to optimize
            max_calories (str): Maximum total calories
            max_cost (str): Maximum total cost

        Returns:
            str: Name of the recipe removed (the one with worst cost/calorie ratio),
                 "" if constraints already met or meal plan doesn't exist
        """
        raise NotImplementedError("Subclasses must implement optimize_meal_plan()")
