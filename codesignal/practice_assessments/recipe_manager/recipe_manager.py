"""
Recipe Manager - Abstract Base Class

A simplified recipe management system. The set of operations is intentionally
small: later levels extend the BEHAVIOUR of the same functions rather than
adding many new ones. The central evolving functions are the recipe TOTALS
(calories and cost), which are reopened for ingredient properties (L2),
per-serving scaling (L3), and meal-plan aggregation (L4). Implement one level
at a time and expect to reopen earlier functions.
"""


class RecipeManager:
	"""Abstract base class for the recipe manager."""

	def __init__(self):
		"""Initialize the recipe manager."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: Basic Recipe CRUD

	def add_recipe(self, timestamp: int, recipe_name: str) -> str:
		"""
		Create a new recipe with a default of 1 serving.

		Returns:
		    str: "true" if created, "false" if the recipe already exists.
		"""
		raise NotImplementedError("Subclasses must implement add_recipe()")

	def add_ingredient(self, timestamp: int, recipe_name: str, ingredient_name: str, quantity: int) -> str:
		"""
		Add quantity of an ingredient to a recipe (accumulates if it exists).

		Returns:
		    str: "true" if added, or "" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement add_ingredient()")

	def get_recipe(self, timestamp: int, recipe_name: str) -> str:
		"""
		Return the recipe's ingredients as "ingredient:quantity" pairs sorted by
		ingredient name ascending, joined by ", ".

		Returns:
		    str: The formatted ingredient list, or "" if the recipe does not
		         exist (also "" if the recipe exists but has no ingredients).
		"""
		raise NotImplementedError("Subclasses must implement get_recipe()")

	def remove_ingredient(self, timestamp: int, recipe_name: str, ingredient_name: str) -> str:
		"""
		Remove an ingredient from a recipe entirely.

		Returns:
		    str: "true" if removed, "false" otherwise (recipe or ingredient
		         missing).
		"""
		raise NotImplementedError("Subclasses must implement remove_ingredient()")

	def delete_recipe(self, timestamp: int, recipe_name: str) -> str:
		"""
		Delete a recipe.

		Returns:
		    str: "true" if deleted, "false" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement delete_recipe()")

	# Level 2 Methods: Ingredient Properties & Totals
	# (The totals introduced here are reopened by every later level.)

	def set_ingredient_info(self, timestamp: int, ingredient_name: str, calories_per_unit: int, cost_per_unit: int) -> str:
		"""
		Set the global calories-per-unit and cost-per-unit for an ingredient
		name. Properties are shared across every recipe using that ingredient.

		Returns:
		    str: "true".
		"""
		raise NotImplementedError("Subclasses must implement set_ingredient_info()")

	def get_total_calories(self, timestamp: int, recipe_name: str) -> str:
		"""
		Return the sum over ingredients of quantity * calories_per_unit.

		Returns:
		    str: The total calories, or "" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement get_total_calories()")

	def get_total_cost(self, timestamp: int, recipe_name: str) -> str:
		"""
		Return the sum over ingredients of quantity * cost_per_unit.

		Returns:
		    str: The total cost, or "" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement get_total_cost()")

	def find_recipes_by_ingredient(self, timestamp: int, ingredient_name: str) -> str:
		"""
		Return the names of recipes containing the ingredient, sorted ascending
		and joined by ", ".

		Returns:
		    str: The formatted recipe list, or "" if none.
		"""
		raise NotImplementedError("Subclasses must implement find_recipes_by_ingredient()")

	# Level 3 Methods: Servings & Scaling
	# (get_total_calories / get_total_cost are reopened to divide by servings.)

	def set_servings(self, timestamp: int, recipe_name: str, servings: int) -> str:
		"""
		Set the number of servings a recipe yields (servings >= 1).

		Returns:
		    str: "true", or "" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement set_servings()")

	def get_calories_per_serving(self, timestamp: int, recipe_name: str) -> str:
		"""
		Return total_calories // servings (floor division).

		Returns:
		    str: The per-serving calories, or "" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement get_calories_per_serving()")

	def get_cost_per_serving(self, timestamp: int, recipe_name: str) -> str:
		"""
		Return total_cost // servings (floor division).

		Returns:
		    str: The per-serving cost, or "" if the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement get_cost_per_serving()")

	def find_recipes_in_budget(self, timestamp: int, max_cost_per_serving: int) -> str:
		"""
		Return the names of recipes whose cost_per_serving is <=
		max_cost_per_serving, sorted by (cost_per_serving asc, name asc) and
		joined by ", ".

		Returns:
		    str: The formatted recipe list, or "" if none.
		"""
		raise NotImplementedError("Subclasses must implement find_recipes_in_budget()")

	# Level 4 Methods: Meal Plans
	# (The totals are reopened to aggregate scaled quantities across recipes.)

	def create_meal_plan(self, timestamp: int, plan_name: str) -> str:
		"""
		Create a new, empty meal plan.

		Returns:
		    str: "true" if created, "false" if the plan already exists.
		"""
		raise NotImplementedError("Subclasses must implement create_meal_plan()")

	def add_recipe_to_plan(self, timestamp: int, plan_name: str, recipe_name: str, servings: int) -> str:
		"""
		Record that the plan needs `servings` servings of recipe_name
		(accumulates if the recipe is already in the plan).

		Returns:
		    str: "true", or "" if the plan or the recipe does not exist.
		"""
		raise NotImplementedError("Subclasses must implement add_recipe_to_plan()")

	def get_plan_shopping_list(self, timestamp: int, plan_name: str) -> str:
		"""
		Return aggregated ingredient quantities across all recipes in the plan,
		each recipe's quantities scaled to its requested servings, as
		"ingredient:quantity" sorted by ingredient ascending and joined by ", ".

		Returns:
		    str: The formatted shopping list, or "" if the plan is missing or
		         empty.
		"""
		raise NotImplementedError("Subclasses must implement get_plan_shopping_list()")

	def get_plan_cost(self, timestamp: int, plan_name: str) -> str:
		"""
		Return the total cost of the plan (sum across recipes of scaled cost).

		Returns:
		    str: The total cost, or "" if the plan does not exist.
		"""
		raise NotImplementedError("Subclasses must implement get_plan_cost()")
