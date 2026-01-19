import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from timeout_decorator import timeout
from working_hour_register_impl import WorkingHourRegisterImpl


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for Working Hour Register - Basic Clock In/Out Operations

	Tests cover: CLOCK_IN, CLOCK_OUT, GET_TOTAL_HOURS, IS_CLOCKED_IN, GET_EMPLOYEES_WORKING
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh WorkingHourRegister instance for each test."""
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_1_case_01_clock_in(self):
		"""Test clocking in an employee."""
		result = self.whr.clock_in(1000000, "emp001")
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_1_case_02_clock_in_twice(self):
		"""Test that clocking in when already clocked in returns false."""
		self.whr.clock_in(1000000, "emp001")
		result = self.whr.clock_in(2000000, "emp001")
		self.assertEqual(result, "false")

	@timeout(0.4)
	def test_level_1_case_03_is_clocked_in(self):
		"""Test checking if employee is clocked in."""
		self.whr.clock_in(1000000, "emp001")
		self.assertEqual(self.whr.is_clocked_in("emp001"), "true")
		self.assertEqual(self.whr.is_clocked_in("emp002"), "false")

	@timeout(0.4)
	def test_level_1_case_04_clock_out_basic(self):
		"""Test basic clock out and hours calculation."""
		self.whr.clock_in(1000000, "emp001")
		# 9000000 ms = 2.5 hours, rounded down to 2
		result = self.whr.clock_out(10000000, "emp001")
		self.assertEqual(result, "2")

	@timeout(0.4)
	def test_level_1_case_05_clock_out_not_clocked_in(self):
		"""Test clocking out when not clocked in returns empty string."""
		result = self.whr.clock_out(10000000, "emp001")
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_1_case_06_get_total_hours(self):
		"""Test getting total hours across multiple sessions."""
		self.whr.clock_in(1000000, "emp001")
		self.whr.clock_out(10000000, "emp001")  # 2 hours
		self.whr.clock_in(11000000, "emp001")
		self.whr.clock_out(25000000, "emp001")  # 3 hours
		result = self.whr.get_total_hours("emp001")
		self.assertEqual(result, "5")

	@timeout(0.4)
	def test_level_1_case_07_get_employees_working(self):
		"""Test getting list of currently working employees."""
		self.whr.clock_in(1000000, "emp001")
		self.whr.clock_in(1500000, "emp002")
		result = self.whr.get_employees_working(1800000)
		self.assertEqual(result, "emp001, emp002")

	@timeout(0.4)
	def test_level_1_case_08_get_employees_working_after_clock_out(self):
		"""Test employees working list after some clock out."""
		self.whr.clock_in(1000000, "emp001")
		self.whr.clock_in(1500000, "emp002")
		self.whr.clock_out(10000000, "emp001")
		result = self.whr.get_employees_working(11000000)
		self.assertEqual(result, "emp002")

	@timeout(0.4)
	def test_level_1_case_09_multiple_employees(self):
		"""Test tracking multiple employees independently."""
		self.assertEqual(self.whr.clock_in(1000000, "emp001"), "true")
		self.assertEqual(self.whr.clock_in(1500000, "emp002"), "true")
		self.assertEqual(self.whr.clock_out(10000000, "emp001"), "2")
		self.assertEqual(self.whr.is_clocked_in("emp001"), "false")
		self.assertEqual(self.whr.is_clocked_in("emp002"), "true")

	@timeout(0.4)
	def test_level_1_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_1."""
		self.assertEqual(self.whr.clock_in(1000000, "emp001"), "true")
		self.assertEqual(self.whr.clock_in(1500000, "emp002"), "true")
		self.assertEqual(self.whr.is_clocked_in("emp001"), "true")
		self.assertEqual(self.whr.is_clocked_in("emp003"), "false")
		self.assertEqual(self.whr.clock_in(2000000, "emp001"), "false")
		self.assertEqual(self.whr.get_employees_working(1800000), "emp001, emp002")
		self.assertEqual(self.whr.clock_out(10000000, "emp001"), "2")
		self.assertEqual(self.whr.is_clocked_in("emp001"), "false")
		self.assertEqual(self.whr.get_total_hours("emp001"), "2")
		self.assertEqual(self.whr.clock_in(11000000, "emp001"), "true")
		self.assertEqual(self.whr.clock_out(25000000, "emp001"), "3")
		self.assertEqual(self.whr.get_total_hours("emp001"), "5")
		self.assertEqual(self.whr.clock_out(30000000, "emp002"), "7916")
		self.assertEqual(self.whr.get_total_hours("emp002"), "7916")


if __name__ == "__main__":
	unittest.main()
