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
	Level 1 tests for Recipe Manager - Basic Recipe CRUD

	Tests cover: add_recipe, add_ingredient, get_recipe, remove_ingredient, delete_recipe
	"""

	failureException = Exception

	def setUp(self):
		self.manager = RecipeManagerImpl()

	@timeout(0.4)
	def test_level_1_case_01_add_recipe(self):
		self.assertEqual(self.manager.add_recipe(1, "pancakes"), "true")

	@timeout(0.4)
	def test_level_1_case_02_add_duplicate_recipe(self):
		self.manager.add_recipe(1, "pancakes")
		self.assertEqual(self.manager.add_recipe(2, "pancakes"), "false")

	@timeout(0.4)
	def test_level_1_case_03_add_ingredient(self):
		self.manager.add_recipe(1, "pancakes")
		self.assertEqual(self.manager.add_ingredient(2, "pancakes", "flour", 300), "true")

	@timeout(0.4)
	def test_level_1_case_04_add_ingredient_missing_recipe(self):
		self.assertEqual(self.manager.add_ingredient(1, "missing", "flour", 300), "")

	@timeout(0.4)
	def test_level_1_case_05_get_recipe_sorted(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "flour", 300)
		self.manager.add_ingredient(3, "pancakes", "egg", 2)
		self.assertEqual(self.manager.get_recipe(4, "pancakes"), "egg:2, flour:300")

	@timeout(0.4)
	def test_level_1_case_06_add_ingredient_accumulates(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "egg", 2)
		self.manager.add_ingredient(3, "pancakes", "egg", 3)
		self.assertEqual(self.manager.get_recipe(4, "pancakes"), "egg:5")

	@timeout(0.4)
	def test_level_1_case_07_get_recipe_missing(self):
		self.assertEqual(self.manager.get_recipe(1, "missing"), "")

	@timeout(0.4)
	def test_level_1_case_08_get_recipe_empty(self):
		self.manager.add_recipe(1, "empty")
		self.assertEqual(self.manager.get_recipe(2, "empty"), "")

	@timeout(0.4)
	def test_level_1_case_09_remove_ingredient(self):
		self.manager.add_recipe(1, "pancakes")
		self.manager.add_ingredient(2, "pancakes", "flour", 300)
		self.manager.add_ingredient(3, "pancakes", "egg", 2)
		self.assertEqual(self.manager.remove_ingredient(4, "pancakes", "flour"), "true")
		self.assertEqual(self.manager.get_recipe(5, "pancakes"), "egg:2")

	@timeout(0.4)
	def test_level_1_case_10_remove_ingredient_missing(self):
		self.manager.add_recipe(1, "pancakes")
		self.assertEqual(self.manager.remove_ingredient(2, "pancakes", "flour"), "false")
		self.assertEqual(self.manager.remove_ingredient(3, "missing", "flour"), "false")

	@timeout(0.4)
	def test_level_1_case_11_delete_recipe(self):
		self.manager.add_recipe(1, "pancakes")
		self.assertEqual(self.manager.delete_recipe(2, "pancakes"), "true")
		self.assertEqual(self.manager.delete_recipe(3, "pancakes"), "false")
		self.assertEqual(self.manager.get_recipe(4, "pancakes"), "")


if __name__ == "__main__":
	unittest.main()
