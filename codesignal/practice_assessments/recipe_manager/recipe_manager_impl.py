from recipe_manager import RecipeManager


class RecipeManagerImpl(RecipeManager):
	"""
	Implementation of the RecipeManager interface.

	The function set is small on purpose. Implement one level at a time and
	expect to reopen earlier functions to satisfy later requirements.
	"""

	def __init__(self):
		"""Initialize the recipe manager."""
		# TODO: implement
		pass

	# Level 1 Methods: Basic Recipe CRUD

	def add_recipe(self, timestamp: int, recipe_name: str) -> str:
		"""Create a new recipe with a default of 1 serving."""
		# TODO: implement
		pass

	def add_ingredient(self, timestamp: int, recipe_name: str, ingredient_name: str, quantity: int) -> str:
		"""Add quantity of an ingredient to a recipe (accumulates if it exists)."""
		# TODO: implement
		pass

	def get_recipe(self, timestamp: int, recipe_name: str) -> str:
		"""Return the recipe's ingredients sorted by ingredient name ascending."""
		# TODO: implement
		pass

	def remove_ingredient(self, timestamp: int, recipe_name: str, ingredient_name: str) -> str:
		"""Remove an ingredient from a recipe entirely."""
		# TODO: implement
		pass

	def delete_recipe(self, timestamp: int, recipe_name: str) -> str:
		"""Delete a recipe."""
		# TODO: implement
		pass

	# Level 2 Methods: Ingredient Properties & Totals

	def set_ingredient_info(self, timestamp: int, ingredient_name: str, calories_per_unit: int, cost_per_unit: int) -> str:
		"""Set the global calories-per-unit and cost-per-unit for an ingredient."""
		# TODO: implement
		pass

	def get_total_calories(self, timestamp: int, recipe_name: str) -> str:
		"""Return the sum over ingredients of quantity * calories_per_unit."""
		# TODO: implement
		pass

	def get_total_cost(self, timestamp: int, recipe_name: str) -> str:
		"""Return the sum over ingredients of quantity * cost_per_unit."""
		# TODO: implement
		pass

	def find_recipes_by_ingredient(self, timestamp: int, ingredient_name: str) -> str:
		"""Return the names of recipes containing the ingredient, sorted ascending."""
		# TODO: implement
		pass

	# Level 3 Methods: Servings & Scaling

	def set_servings(self, timestamp: int, recipe_name: str, servings: int) -> str:
		"""Set the number of servings a recipe yields (servings >= 1)."""
		# TODO: implement
		pass

	def get_calories_per_serving(self, timestamp: int, recipe_name: str) -> str:
		"""Return total_calories // servings (floor division)."""
		# TODO: implement
		pass

	def get_cost_per_serving(self, timestamp: int, recipe_name: str) -> str:
		"""Return total_cost // servings (floor division)."""
		# TODO: implement
		pass

	def find_recipes_in_budget(self, timestamp: int, max_cost_per_serving: int) -> str:
		"""Return the names of recipes whose cost_per_serving is <= max_cost_per_serving."""
		# TODO: implement
		pass

	# Level 4 Methods: Meal Plans

	def create_meal_plan(self, timestamp: int, plan_name: str) -> str:
		"""Create a new, empty meal plan."""
		# TODO: implement
		pass

	def add_recipe_to_plan(self, timestamp: int, plan_name: str, recipe_name: str, servings: int) -> str:
		"""Record that the plan needs `servings` servings of recipe_name."""
		# TODO: implement
		pass

	def get_plan_shopping_list(self, timestamp: int, plan_name: str) -> str:
		"""Return aggregated scaled ingredient quantities across all recipes in the plan."""
		# TODO: implement
		pass

	def get_plan_cost(self, timestamp: int, plan_name: str) -> str:
		"""Return the total cost of the plan (sum across recipes of scaled cost)."""
		# TODO: implement
		pass
