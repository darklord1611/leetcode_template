import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from recipe_manager_impl import RecipeManagerImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for Recipe Manager - Ingredient Properties & Totals

	Tests cover: set_ingredient_info, get_total_calories, get_total_cost,
	             find_recipes_by_ingredient
	"""

	failureException = Exception

	def setUp(self):
		self.manager = RecipeManagerImpl()

	@timeout(0.4)
	def test_level_2_case_01_set_ingredient_info(self):
		self.assertEqual(self.manager.set_ingredient_info(1, "flour", 4, 1), "true")

	@timeout(0.4)
	def test_level_2_case_02_total_calories(self):
		self.manager.set_ingredient_info(1, "flour", 4, 1)
		self.manager.set_ingredient_info(2, "egg", 70, 2)
		self.manager.add_recipe(3, "pancakes")
		self.manager.add_ingredient(4, "pancakes", "flour", 100)
		self.manager.add_ingredient(5, "pancakes", "egg", 2)
		# 100*4 + 2*70 = 540
		self.assertEqual(self.manager.get_total_calories(6, "pancakes"), "540")

	@timeout(0.4)
	def test_level_2_case_03_total_cost(self):
		self.manager.set_ingredient_info(1, "flour", 4, 1)
		self.manager.set_ingredient_info(2, "egg", 70, 2)
		self.manager.add_recipe(3, "pancakes")
		self.manager.add_ingredient(4, "pancakes", "flour", 100)
		self.manager.add_ingredient(5, "pancakes", "egg", 2)
		# 100*1 + 2*2 = 104
		self.assertEqual(self.manager.get_total_cost(6, "pancakes"), "104")

	@timeout(0.4)
	def test_level_2_case_04_default_zero_props(self):
		self.manager.add_recipe(1, "plain")
		self.manager.add_ingredient(2, "plain", "water", 500)
		self.assertEqual(self.manager.get_total_calories(3, "plain"), "0")
		self.assertEqual(self.manager.get_total_cost(4, "plain"), "0")

	@timeout(0.4)
	def test_level_2_case_05_info_is_global(self):
		self.manager.set_ingredient_info(1, "egg", 70, 2)
		self.manager.add_recipe(2, "omelette")
		self.manager.add_recipe(3, "cake")
		self.manager.add_ingredient(4, "omelette", "egg", 3)
		self.manager.add_ingredient(5, "cake", "egg", 4)
		self.assertEqual(self.manager.get_total_calories(6, "omelette"), "210")
		self.assertEqual(self.manager.get_total_calories(7, "cake"), "280")

	@timeout(0.4)
	def test_level_2_case_06_info_overwrite(self):
		self.manager.set_ingredient_info(1, "egg", 70, 2)
		self.manager.add_recipe(2, "omelette")
		self.manager.add_ingredient(3, "omelette", "egg", 2)
		self.assertEqual(self.manager.get_total_calories(4, "omelette"), "140")
		self.manager.set_ingredient_info(5, "egg", 80, 3)
		self.assertEqual(self.manager.get_total_calories(6, "omelette"), "160")
		self.assertEqual(self.manager.get_total_cost(7, "omelette"), "6")

	@timeout(0.4)
	def test_level_2_case_07_totals_missing_recipe(self):
		self.assertEqual(self.manager.get_total_calories(1, "missing"), "")
		self.assertEqual(self.manager.get_total_cost(2, "missing"), "")

	@timeout(0.4)
	def test_level_2_case_08_empty_recipe_totals(self):
		self.manager.add_recipe(1, "empty")
		self.assertEqual(self.manager.get_total_calories(2, "empty"), "0")
		self.assertEqual(self.manager.get_total_cost(3, "empty"), "0")

	@timeout(0.4)
	def test_level_2_case_09_find_recipes_by_ingredient(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_recipe(2, "cake")
		self.manager.add_recipe(3, "soup")
		self.manager.add_ingredient(4, "pancakes", "egg", 2)
		self.manager.add_ingredient(5, "cake", "egg", 4)
		self.manager.add_ingredient(6, "soup", "water", 500)
		self.assertEqual(self.manager.find_recipes_by_ingredient(7, "egg"), "cake, pancakes")

	@timeout(0.4)
	def test_level_2_case_10_find_recipes_none(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "egg", 2)
		self.assertEqual(self.manager.find_recipes_by_ingredient(3, "sugar"), "")

	@timeout(0.4)
	def test_level_2_case_11_find_after_remove(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "egg", 2)
		self.manager.remove_ingredient(3, "pancakes", "egg")
		self.assertEqual(self.manager.find_recipes_by_ingredient(4, "egg"), "")


if __name__ == "__main__":
	unittest.main()
