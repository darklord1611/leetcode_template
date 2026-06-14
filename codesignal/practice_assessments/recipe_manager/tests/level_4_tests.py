import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from recipe_manager_impl import RecipeManagerImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for Recipe Manager - Meal Plans

	Tests cover: create_meal_plan, add_recipe_to_plan, get_plan_shopping_list,
	             get_plan_cost
	"""

	failureException = Exception

	def setUp(self):
		self.manager = RecipeManagerImpl()
		self.manager.set_ingredient_info(0, "flour", 4, 1)
		self.manager.set_ingredient_info(0, "egg", 70, 2)
		# pancakes: makes 2 servings, flour 100, egg 2 -> cost 104
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "flour", 100)
		self.manager.add_ingredient(3, "pancakes", "egg", 2)
		self.manager.set_servings(4, "pancakes", 2)
		# omelette: makes 1 serving, egg 3 -> cost 6
		self.manager.add_recipe(5, "omelette")
		self.manager.add_ingredient(6, "omelette", "egg", 3)
		self.manager.set_servings(7, "omelette", 1)

	@timeout(0.4)
	def test_level_4_case_01_create_meal_plan(self):
		self.assertEqual(self.manager.create_meal_plan(10, "week1"), "true")

	@timeout(0.4)
	def test_level_4_case_02_create_duplicate_plan(self):
		self.manager.create_meal_plan(10, "week1")
		self.assertEqual(self.manager.create_meal_plan(11, "week1"), "false")

	@timeout(0.4)
	def test_level_4_case_03_add_recipe_to_plan(self):
		self.manager.create_meal_plan(10, "week1")
		self.assertEqual(self.manager.add_recipe_to_plan(11, "week1", "pancakes", 4), "true")

	@timeout(0.4)
	def test_level_4_case_04_add_recipe_missing_plan(self):
		self.assertEqual(self.manager.add_recipe_to_plan(10, "missing", "pancakes", 4), "")

	@timeout(0.4)
	def test_level_4_case_05_add_missing_recipe(self):
		self.manager.create_meal_plan(10, "week1")
		self.assertEqual(self.manager.add_recipe_to_plan(11, "week1", "missing", 4), "")

	@timeout(0.4)
	def test_level_4_case_06_shopping_list_scaled(self):
		self.manager.create_meal_plan(10, "week1")
		# 4 servings of pancakes (default 2): scale 2x -> flour 200, egg 4
		self.manager.add_recipe_to_plan(11, "week1", "pancakes", 4)
		self.assertEqual(self.manager.get_plan_shopping_list(12, "week1"), "egg:4, flour:200")

	@timeout(0.4)
	def test_level_4_case_07_shopping_list_aggregated(self):
		self.manager.create_meal_plan(10, "week1")
		# pancakes 4 -> flour 200, egg 4 ; omelette 2 -> egg 6
		self.manager.add_recipe_to_plan(11, "week1", "pancakes", 4)
		self.manager.add_recipe_to_plan(12, "week1", "omelette", 2)
		self.assertEqual(self.manager.get_plan_shopping_list(13, "week1"), "egg:10, flour:200")

	@timeout(0.4)
	def test_level_4_case_08_add_recipe_accumulates(self):
		self.manager.create_meal_plan(10, "week1")
		self.manager.add_recipe_to_plan(11, "week1", "pancakes", 2)
		self.manager.add_recipe_to_plan(12, "week1", "pancakes", 2)
		# 4 servings total -> flour 200, egg 4
		self.assertEqual(self.manager.get_plan_shopping_list(13, "week1"), "egg:4, flour:200")

	@timeout(0.4)
	def test_level_4_case_09_plan_cost(self):
		self.manager.create_meal_plan(10, "week1")
		# pancakes cost 104, 4 servings/default 2 -> 208 ; omelette cost 6, 2/1 -> 12
		self.manager.add_recipe_to_plan(11, "week1", "pancakes", 4)
		self.manager.add_recipe_to_plan(12, "week1", "omelette", 2)
		self.assertEqual(self.manager.get_plan_cost(13, "week1"), "220")

	@timeout(0.4)
	def test_level_4_case_10_empty_and_missing(self):
		self.manager.create_meal_plan(10, "week1")
		self.assertEqual(self.manager.get_plan_shopping_list(11, "week1"), "")
		self.assertEqual(self.manager.get_plan_cost(12, "week1"), "0")
		self.assertEqual(self.manager.get_plan_shopping_list(13, "missing"), "")
		self.assertEqual(self.manager.get_plan_cost(14, "missing"), "")

	@timeout(0.4)
	def test_level_4_case_11_shopping_list_floor(self):
		self.manager.create_meal_plan(10, "week1")
		# 3 servings of pancakes (default 2): flour 100*3//2=150, egg 2*3//2=3
		self.manager.add_recipe_to_plan(11, "week1", "pancakes", 3)
		self.assertEqual(self.manager.get_plan_shopping_list(12, "week1"), "egg:3, flour:150")


if __name__ == "__main__":
	unittest.main()
