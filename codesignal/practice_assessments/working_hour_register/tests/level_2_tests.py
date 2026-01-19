import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from timeout_decorator import timeout
from working_hour_register_impl import WorkingHourRegisterImpl


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for Working Hour Register - Date-Based Queries

	Tests cover: GET_HOURS_ON_DATE, GET_HOURS_IN_RANGE, GET_EMPLOYEES_BY_DATE,
	             GET_TOP_EMPLOYEES_BY_HOURS, GET_AVERAGE_DAILY_HOURS
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh WorkingHourRegister instance for each test."""
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_2_case_01_get_hours_on_date_single_session(self):
		"""Test getting hours for a specific date with one session."""
		# 2024-01-15 09:00 to 17:00 = 8 hours
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		result = self.whr.get_hours_on_date("emp001", "2024-01-15")
		self.assertEqual(result, "8")

	@timeout(0.4)
	def test_level_2_case_02_get_hours_on_date_different_dates(self):
		"""Test getting hours across different dates."""
		# 2024-01-15 09:00 to 17:00 = 8 hours
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		# 2024-01-16 09:00 to 15:00 = 6 hours
		self.whr.clock_in(1705395600000, "emp001")
		self.whr.clock_out(1705417200000, "emp001")
		self.assertEqual(self.whr.get_hours_on_date("emp001", "2024-01-15"), "8")
		self.assertEqual(self.whr.get_hours_on_date("emp001", "2024-01-16"), "6")

	@timeout(0.4)
	def test_level_2_case_03_get_hours_in_range(self):
		"""Test getting total hours in a date range."""
		# 2024-01-15 09:00 to 17:00 = 8 hours
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		# 2024-01-16 09:00 to 15:00 = 6 hours
		self.whr.clock_in(1705395600000, "emp001")
		self.whr.clock_out(1705417200000, "emp001")
		result = self.whr.get_hours_in_range("emp001", "2024-01-15", "2024-01-16")
		self.assertEqual(result, "14")

	@timeout(0.4)
	def test_level_2_case_04_get_employees_by_date(self):
		"""Test getting all employees who worked on a date."""
		# Both emp001 and emp002 work on 2024-01-15
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		self.whr.clock_in(1705309200000, "emp002")
		self.whr.clock_out(1705345200000, "emp002")
		result = self.whr.get_employees_by_date("2024-01-15")
		self.assertEqual(result, "emp001, emp002")

	@timeout(0.4)
	def test_level_2_case_05_get_top_employees_by_hours(self):
		"""Test getting top employees by total hours worked."""
		# emp001: 8 + 6 = 14 hours
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		self.whr.clock_in(1705395600000, "emp001")
		self.whr.clock_out(1705417200000, "emp001")
		# emp002: 10 hours
		self.whr.clock_in(1705309200000, "emp002")
		self.whr.clock_out(1705345200000, "emp002")
		result = self.whr.get_top_employees_by_hours(2)
		self.assertEqual(result, "emp001(14), emp002(10)")

	@timeout(0.4)
	def test_level_2_case_06_get_average_daily_hours(self):
		"""Test calculating average daily hours for an employee."""
		# emp001: 8 + 6 = 14 hours over 2 days = 7 average
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		self.whr.clock_in(1705395600000, "emp001")
		self.whr.clock_out(1705417200000, "emp001")
		result = self.whr.get_average_daily_hours("emp001")
		self.assertEqual(result, "7")

	@timeout(0.4)
	def test_level_2_case_07_get_top_employees_limit(self):
		"""Test top employees with limit less than total employees."""
		# emp001: 14 hours
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		self.whr.clock_in(1705395600000, "emp001")
		self.whr.clock_out(1705417200000, "emp001")
		# emp002: 10 hours
		self.whr.clock_in(1705309200000, "emp002")
		self.whr.clock_out(1705345200000, "emp002")
		# emp003: 5 hours
		self.whr.clock_in(1705309200000, "emp003")
		self.whr.clock_out(1705327200000, "emp003")
		result = self.whr.get_top_employees_by_hours(2)
		self.assertEqual(result, "emp001(14), emp002(10)")

	@timeout(0.4)
	def test_level_2_case_08_get_hours_on_date_no_work(self):
		"""Test getting hours for a date with no work."""
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		result = self.whr.get_hours_on_date("emp001", "2024-01-16")
		self.assertEqual(result, "0")

	@timeout(0.4)
	def test_level_2_case_09_get_hours_in_range_single_date(self):
		"""Test hours in range with single date."""
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		result = self.whr.get_hours_in_range("emp001", "2024-01-15", "2024-01-15")
		self.assertEqual(result, "8")

	@timeout(0.4)
	def test_level_2_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_2."""
		# emp001 works 2024-01-15 09:00-17:00 (8 hours)
		self.assertEqual(self.whr.clock_in(1705309200000, "emp001"), "true")
		self.assertEqual(self.whr.clock_out(1705338000000, "emp001"), "8")
		# emp001 works 2024-01-16 09:00-15:00 (6 hours)
		self.assertEqual(self.whr.clock_in(1705395600000, "emp001"), "true")
		self.assertEqual(self.whr.clock_out(1705417200000, "emp001"), "6")
		# emp002 works 2024-01-15 09:00-19:00 (10 hours)
		self.assertEqual(self.whr.clock_in(1705309200000, "emp002"), "true")
		self.assertEqual(self.whr.clock_out(1705345200000, "emp002"), "10")
		self.assertEqual(self.whr.get_hours_on_date("emp001", "2024-01-15"), "8")
		self.assertEqual(self.whr.get_hours_on_date("emp001", "2024-01-16"), "6")
		self.assertEqual(self.whr.get_hours_in_range("emp001", "2024-01-15", "2024-01-16"), "14")
		self.assertEqual(self.whr.get_employees_by_date("2024-01-15"), "emp001, emp002")
		self.assertEqual(self.whr.get_top_employees_by_hours(2), "emp001(14), emp002(10)")
		self.assertEqual(self.whr.get_average_daily_hours("emp001"), "7")


if __name__ == "__main__":
	unittest.main()
