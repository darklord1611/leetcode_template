import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from recipe_manager_impl import RecipeManagerImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for Recipe Manager - Recipe Scaling and Tags

	Tests cover: SET_SERVING_SIZE, SCALE_RECIPE, GET_CALORIES_PER_SERVING,
	             ADD_RECIPE_TAG, FIND_RECIPES_BY_TAG, FIND_RECIPES_IN_BUDGET
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh RecipeManager instance for each test."""
		self.manager = RecipeManagerImpl()

	@timeout(0.4)
	def test_level_3_case_01_set_serving_size(self):
		"""Test setting serving size for a recipe."""
		self.manager.add_recipe("pasta_carbonara")
		result = self.manager.set_serving_size("pasta_carbonara", "2")
		self.assertEqual(result, "2")

	@timeout(0.4)
	def test_level_3_case_02_scale_recipe(self):
		"""Test scaling a recipe."""
		self.manager.add_recipe("pasta_carbonara")
		self.manager.add_ingredient_with_props("pasta_carbonara", "pasta", "200", "150", "2")
		self.manager.add_ingredient_with_props("pasta_carbonara", "bacon", "100", "500", "5")
		self.manager.add_ingredient_with_props("pasta_carbonara", "eggs", "2", "70", "1")
		self.manager.set_serving_size("pasta_carbonara", "2")
		result = self.manager.scale_recipe("pasta_carbonara", "4")
		# Scale from 2 to 4 servings: multiply by 2
		self.assertEqual(result, "bacon(200), eggs(4), pasta(400)")

	@timeout(0.4)
	def test_level_3_case_03_get_calories_per_serving(self):
		"""Test calculating calories per serving."""
		self.manager.add_recipe("pasta_carbonara")
		self.manager.add_ingredient_with_props("pasta_carbonara", "pasta", "200", "150", "2")
		self.manager.add_ingredient_with_props("pasta_carbonara", "bacon", "100", "500", "5")
		self.manager.add_ingredient_with_props("pasta_carbonara", "eggs", "2", "70", "1")
		self.manager.set_serving_size("pasta_carbonara", "2")
		result = self.manager.get_calories_per_serving("pasta_carbonara")
		# Total: 80140, servings: 2, per serving: 40070
		self.assertEqual(result, "40070")

	@timeout(0.4)
	def test_level_3_case_04_add_recipe_tag(self):
		"""Test adding a tag to a recipe."""
		self.manager.add_recipe("veggie_salad")
		result = self.manager.add_recipe_tag("veggie_salad", "vegetarian")
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_3_case_05_add_duplicate_tag(self):
		"""Test adding duplicate tag returns false."""
		self.manager.add_recipe("veggie_salad")
		self.manager.add_recipe_tag("veggie_salad", "vegetarian")
		result = self.manager.add_recipe_tag("veggie_salad", "vegetarian")
		self.assertEqual(result, "false")

	@timeout(0.4)
	def test_level_3_case_06_find_recipes_by_tag(self):
		"""Test finding recipes by tag."""
		self.manager.add_recipe("veggie_salad")
		self.manager.add_recipe("veggie_soup")
		self.manager.add_recipe("pasta")
		self.manager.add_recipe_tag("veggie_salad", "vegetarian")
		self.manager.add_recipe_tag("veggie_soup", "vegetarian")
		self.manager.add_recipe_tag("pasta", "italian")
		result = self.manager.find_recipes_by_tag("vegetarian")
		self.assertEqual(result, "veggie_salad, veggie_soup")

	@timeout(0.4)
	def test_level_3_case_07_find_recipes_in_budget(self):
		"""Test finding recipes within budget."""
		self.manager.add_recipe("pasta_carbonara")
		self.manager.add_ingredient_with_props("pasta_carbonara", "pasta", "200", "150", "2")
		self.manager.add_ingredient_with_props("pasta_carbonara", "bacon", "100", "500", "5")
		self.manager.set_serving_size("pasta_carbonara", "2")
		self.manager.add_recipe("veggie_salad")
		self.manager.add_ingredient_with_props("veggie_salad", "lettuce", "100", "15", "1")
		self.manager.add_ingredient_with_props("veggie_salad", "tomato", "50", "20", "2")
		self.manager.set_serving_size("veggie_salad", "1")
		result = self.manager.find_recipes_in_budget("300")
		# veggie_salad cost: 100*1 + 50*2 = 200, per serving: 200/1 = 200
		# pasta_carbonara cost: 200*2 + 100*5 = 900, per serving: 900/2 = 450
		self.assertEqual(result, "veggie_salad")

	@timeout(0.4)
	def test_level_3_case_08_scale_recipe_no_serving_size(self):
		"""Test scaling recipe without serving size returns empty string."""
		self.manager.add_recipe("pasta")
		self.manager.add_ingredient_with_props("pasta", "pasta", "200", "150", "2")
		result = self.manager.scale_recipe("pasta", "4")
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_3_case_09_calories_per_serving_no_serving_size(self):
		"""Test getting calories per serving without serving size returns empty string."""
		self.manager.add_recipe("pasta")
		self.manager.add_ingredient_with_props("pasta", "pasta", "200", "150", "2")
		result = self.manager.get_calories_per_serving("pasta")
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_3_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_3."""
		self.assertEqual(self.manager.add_recipe("pasta_carbonara"), "true")
		self.assertEqual(self.manager.add_ingredient_with_props("pasta_carbonara", "pasta", "200", "150", "2"), "200")
		self.assertEqual(self.manager.add_ingredient_with_props("pasta_carbonara", "bacon", "100", "500", "5"), "100")
		self.assertEqual(self.manager.add_ingredient_with_props("pasta_carbonara", "eggs", "2", "70", "1"), "2")
		self.assertEqual(self.manager.set_serving_size("pasta_carbonara", "2"), "2")
		self.assertEqual(self.manager.scale_recipe("pasta_carbonara", "4"), "bacon(200), eggs(4), pasta(400)")
		self.assertEqual(self.manager.get_calories_per_serving("pasta_carbonara"), "40070")
		self.assertEqual(self.manager.get_total_cost("pasta_carbonara"), "542")
		self.assertEqual(self.manager.add_recipe("veggie_salad"), "true")
		self.assertEqual(self.manager.add_ingredient_with_props("veggie_salad", "lettuce", "100", "15", "1"), "100")
		self.assertEqual(self.manager.add_ingredient_with_props("veggie_salad", "tomato", "50", "20", "2"), "50")
		self.assertEqual(self.manager.set_serving_size("veggie_salad", "1"), "1")
		self.assertEqual(self.manager.add_recipe_tag("veggie_salad", "vegetarian"), "true")
		self.assertEqual(self.manager.add_recipe_tag("veggie_salad", "vegan"), "true")
		self.assertEqual(self.manager.add_recipe_tag("pasta_carbonara", "high-protein"), "true")
		self.assertEqual(self.manager.find_recipes_by_tag("vegetarian"), "veggie_salad")
		self.assertEqual(self.manager.find_recipes_by_tag("vegan"), "veggie_salad")
		self.assertEqual(self.manager.find_recipes_in_budget("10"), "veggie_salad")


if __name__ == "__main__":
	unittest.main()
