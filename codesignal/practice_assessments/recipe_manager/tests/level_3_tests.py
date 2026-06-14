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
	Level 3 tests for Recipe Manager - Servings & Scaling

	Tests cover: set_servings, get_calories_per_serving, get_cost_per_serving,
	             find_recipes_in_budget
	"""

	failureException = Exception

	def setUp(self):
		self.manager = RecipeManagerImpl()
		self.manager.set_ingredient_info(0, "flour", 4, 1)
		self.manager.set_ingredient_info(0, "egg", 70, 2)

	def _make_pancakes(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "flour", 100)
		self.manager.add_ingredient(3, "pancakes", "egg", 2)
		# total calories = 540, total cost = 104

	@timeout(0.4)
	def test_level_3_case_01_set_servings(self):
		self._make_pancakes()
		self.assertEqual(self.manager.set_servings(4, "pancakes", 4), "true")

	@timeout(0.4)
	def test_level_3_case_02_set_servings_missing(self):
		self.assertEqual(self.manager.set_servings(1, "missing", 4), "")

	@timeout(0.4)
	def test_level_3_case_03_default_serving_is_one(self):
		self._make_pancakes()
		self.assertEqual(self.manager.get_calories_per_serving(4, "pancakes"), "540")
		self.assertEqual(self.manager.get_cost_per_serving(5, "pancakes"), "104")

	@timeout(0.4)
	def test_level_3_case_04_calories_per_serving(self):
		self._make_pancakes()
		self.manager.set_servings(4, "pancakes", 4)
		# 540 // 4 = 135
		self.assertEqual(self.manager.get_calories_per_serving(5, "pancakes"), "135")

	@timeout(0.4)
	def test_level_3_case_05_cost_per_serving(self):
		self._make_pancakes()
		self.manager.set_servings(4, "pancakes", 4)
		# 104 // 4 = 26
		self.assertEqual(self.manager.get_cost_per_serving(5, "pancakes"), "26")

	@timeout(0.4)
	def test_level_3_case_06_floor_division(self):
		self.manager.add_recipe(1, "snack")
		self.manager.add_ingredient(2, "snack", "egg", 1)
		# total calories = 70, cost = 2
		self.manager.set_servings(3, "snack", 3)
		self.assertEqual(self.manager.get_calories_per_serving(4, "snack"), "23")
		self.assertEqual(self.manager.get_cost_per_serving(5, "snack"), "0")

	@timeout(0.4)
	def test_level_3_case_07_per_serving_missing(self):
		self.assertEqual(self.manager.get_calories_per_serving(1, "missing"), "")
		self.assertEqual(self.manager.get_cost_per_serving(2, "missing"), "")

	@timeout(0.4)
	def test_level_3_case_08_find_in_budget(self):
		self._make_pancakes()
		self.manager.set_servings(4, "pancakes", 4)  # cost/serving = 26
		self.manager.add_recipe(5, "omelette")
		self.manager.add_ingredient(6, "omelette", "egg", 3)  # cost 6
		self.manager.set_servings(7, "omelette", 2)  # cost/serving = 3
		self.assertEqual(self.manager.find_recipes_in_budget(8, 30), "omelette, pancakes")

	@timeout(0.4)
	def test_level_3_case_09_find_in_budget_ordering(self):
		# cost/serving ascending, then name ascending
		self.manager.add_recipe(1, "alpha")
		self.manager.add_ingredient(2, "alpha", "egg", 5)  # cost 10
		# default 1 serving -> 10
		self.manager.add_recipe(3, "beta")
		self.manager.add_ingredient(4, "beta", "egg", 5)  # cost 10 -> 10
		self.manager.add_recipe(5, "cheap")
		self.manager.add_ingredient(6, "cheap", "flour", 2)  # cost 2 -> 2
		self.assertEqual(self.manager.find_recipes_in_budget(7, 100), "cheap, alpha, beta")

	@timeout(0.4)
	def test_level_3_case_10_find_in_budget_filter(self):
		self.manager.add_recipe(1, "cheap")
		self.manager.add_ingredient(2, "cheap", "flour", 2)  # cost/serving 2
		self.manager.add_recipe(3, "pricey")
		self.manager.add_ingredient(4, "pricey", "egg", 50)  # cost/serving 100
		self.assertEqual(self.manager.find_recipes_in_budget(5, 10), "cheap")

	@timeout(0.4)
	def test_level_3_case_11_find_in_budget_none(self):
		self.manager.add_recipe(1, "pricey")
		self.manager.add_ingredient(2, "pricey", "egg", 50)  # cost/serving 100
		self.assertEqual(self.manager.find_recipes_in_budget(3, 5), "")


if __name__ == "__main__":
	unittest.main()
