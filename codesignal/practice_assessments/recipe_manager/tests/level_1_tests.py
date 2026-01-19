import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from recipe_manager_impl import RecipeManagerImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for Recipe Manager - Basic Operations

	Tests cover: ADD_RECIPE, ADD_INGREDIENT, GET_RECIPE, REMOVE_INGREDIENT, DELETE_RECIPE
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh RecipeManager instance for each test."""
		self.manager = RecipeManagerImpl()

	@timeout(0.4)
	def test_level_1_case_01_add_recipe(self):
		"""Test adding a new recipe."""
		result = self.manager.add_recipe("pasta_carbonara")
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_1_case_02_add_duplicate_recipe(self):
		"""Test that duplicate recipe creation returns false."""
		self.manager.add_recipe("pasta_carbonara")
		result = self.manager.add_recipe("pasta_carbonara")
		self.assertEqual(result, "false")

	@timeout(0.4)
	def test_level_1_case_03_add_ingredient(self):
		"""Test adding ingredient to recipe."""
		self.manager.add_recipe("pasta_carbonara")
		result = self.manager.add_ingredient("pasta_carbonara", "pasta", "200")
		self.assertEqual(result, "200")

	@timeout(0.4)
	def test_level_1_case_04_add_ingredient_nonexistent_recipe(self):
		"""Test adding ingredient to non-existent recipe returns empty string."""
		result = self.manager.add_ingredient("nonexistent", "pasta", "200")
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_1_case_05_update_ingredient_quantity(self):
		"""Test updating ingredient quantity."""
		self.manager.add_recipe("pasta_carbonara")
		self.manager.add_ingredient("pasta_carbonara", "pasta", "200")
		result = self.manager.add_ingredient("pasta_carbonara", "pasta", "250")
		self.assertEqual(result, "250")

	@timeout(0.4)
	def test_level_1_case_06_get_recipe(self):
		"""Test getting recipe ingredients sorted alphabetically."""
		self.manager.add_recipe("pasta_carbonara")
		self.manager.add_ingredient("pasta_carbonara", "pasta", "200")
		self.manager.add_ingredient("pasta_carbonara", "bacon", "100")
		self.manager.add_ingredient("pasta_carbonara", "eggs", "2")
		result = self.manager.get_recipe("pasta_carbonara")
		self.assertEqual(result, "bacon(100), eggs(2), pasta(200)")

	@timeout(0.4)
	def test_level_1_case_07_remove_ingredient(self):
		"""Test removing ingredient from recipe."""
		self.manager.add_recipe("pasta_carbonara")
		self.manager.add_ingredient("pasta_carbonara", "pasta", "200")
		self.manager.add_ingredient("pasta_carbonara", "bacon", "100")
		result = self.manager.remove_ingredient("pasta_carbonara", "bacon")
		self.assertEqual(result, "true")
		recipe = self.manager.get_recipe("pasta_carbonara")
		self.assertEqual(recipe, "pasta(200)")

	@timeout(0.4)
	def test_level_1_case_08_remove_ingredient_nonexistent(self):
		"""Test removing non-existent ingredient returns false."""
		self.manager.add_recipe("pasta_carbonara")
		result = self.manager.remove_ingredient("nonexistent", "ingredient")
		self.assertEqual(result, "false")

	@timeout(0.4)
	def test_level_1_case_09_delete_recipe(self):
		"""Test deleting a recipe."""
		self.manager.add_recipe("caesar_salad")
		result = self.manager.delete_recipe("caesar_salad")
		self.assertEqual(result, "true")
		recipe = self.manager.get_recipe("caesar_salad")
		self.assertEqual(recipe, "")

	@timeout(0.4)
	def test_level_1_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_1."""
		self.assertEqual(self.manager.add_recipe("pasta_carbonara"), "true")
		self.assertEqual(self.manager.add_recipe("caesar_salad"), "true")
		self.assertEqual(self.manager.add_recipe("pasta_carbonara"), "false")
		self.assertEqual(self.manager.add_ingredient("pasta_carbonara", "pasta", "200"), "200")
		self.assertEqual(self.manager.add_ingredient("pasta_carbonara", "bacon", "100"), "100")
		self.assertEqual(self.manager.add_ingredient("pasta_carbonara", "eggs", "2"), "2")
		self.assertEqual(self.manager.add_ingredient("caesar_salad", "lettuce", "150"), "150")
		self.assertEqual(self.manager.add_ingredient("caesar_salad", "croutons", "50"), "50")
		self.assertEqual(self.manager.get_recipe("pasta_carbonara"), "bacon(100), eggs(2), pasta(200)")
		self.assertEqual(self.manager.get_recipe("caesar_salad"), "croutons(50), lettuce(150)")
		self.assertEqual(self.manager.add_ingredient("pasta_carbonara", "pasta", "250"), "250")
		self.assertEqual(self.manager.get_recipe("pasta_carbonara"), "bacon(100), eggs(2), pasta(250)")
		self.assertEqual(self.manager.remove_ingredient("pasta_carbonara", "bacon"), "true")
		self.assertEqual(self.manager.get_recipe("pasta_carbonara"), "eggs(2), pasta(250)")
		self.assertEqual(self.manager.remove_ingredient("nonexistent", "ingredient"), "false")
		self.assertEqual(self.manager.delete_recipe("caesar_salad"), "true")
		self.assertEqual(self.manager.get_recipe("caesar_salad"), "")


if __name__ == "__main__":
	unittest.main()
