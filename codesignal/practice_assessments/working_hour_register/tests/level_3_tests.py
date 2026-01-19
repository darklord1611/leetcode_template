import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from timeout_decorator import timeout
from working_hour_register_impl import WorkingHourRegisterImpl


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for Working Hour Register - Payroll and Breaks

	Tests cover: SET_HOURLY_RATE, CALCULATE_OVERTIME_HOURS, GET_PAY_FOR_DATE,
	             ADD_BREAK, GET_EMPLOYEES_WITH_OVERTIME, GET_TOTAL_PAY
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh WorkingHourRegister instance for each test."""
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_3_case_01_set_hourly_rate(self):
		"""Test setting hourly rate for an employee."""
		result = self.whr.set_hourly_rate("emp001", 25)
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_3_case_02_calculate_overtime_hours(self):
		"""Test calculating overtime hours (hours > 8)."""
		# 2024-01-15 09:00 to 19:00 = 10 hours, overtime = 2
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705345200000, "emp001")
		result = self.whr.calculate_overtime_hours("emp001", "2024-01-15")
		self.assertEqual(result, "2")

	@timeout(0.4)
	def test_level_3_case_03_calculate_overtime_no_overtime(self):
		"""Test calculating overtime when hours <= 8."""
		# 2024-01-15 09:00 to 17:00 = 8 hours, overtime = 0
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		result = self.whr.calculate_overtime_hours("emp001", "2024-01-15")
		self.assertEqual(result, "0")

	@timeout(0.4)
	def test_level_3_case_04_get_pay_for_date_no_overtime(self):
		"""Test calculating pay with no overtime (8 hours)."""
		# 8 hours * $25 = $200
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705338000000, "emp001")
		self.whr.set_hourly_rate("emp001", 25)
		result = self.whr.get_pay_for_date("emp001", "2024-01-15")
		self.assertEqual(result, "200")

	@timeout(0.4)
	def test_level_3_case_05_get_pay_for_date_with_overtime(self):
		"""Test calculating pay with overtime."""
		# 10 hours: 8 * $25 + 2 * $25 * 1.5 = $200 + $75 = $275
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705345200000, "emp001")
		self.whr.set_hourly_rate("emp001", 25)
		result = self.whr.get_pay_for_date("emp001", "2024-01-15")
		self.assertEqual(result, "275")

	@timeout(0.4)
	def test_level_3_case_06_add_break(self):
		"""Test adding a break that reduces hours worked."""
		# 2024-01-16 09:00 to 17:00 = 8 hours, minus 1 hour break = 7 hours
		self.whr.clock_in(1705395600000, "emp002")
		# Break: 1 hour (1705402800000 to 1705406400000)
		self.whr.add_break(1705402800000, 1705406400000, "emp002")
		result = self.whr.clock_out(1705424400000, "emp002")
		self.assertEqual(result, "7")

	@timeout(0.4)
	def test_level_3_case_07_get_pay_for_date_with_break(self):
		"""Test calculating pay with break deduction."""
		# 7 hours * $20 = $140
		self.whr.clock_in(1705395600000, "emp002")
		self.whr.add_break(1705402800000, 1705406400000, "emp002")
		self.whr.clock_out(1705424400000, "emp002")
		self.whr.set_hourly_rate("emp002", 20)
		result = self.whr.get_pay_for_date("emp002", "2024-01-16")
		self.assertEqual(result, "140")

	@timeout(0.4)
	def test_level_3_case_08_get_employees_with_overtime(self):
		"""Test getting employees who worked overtime on a date."""
		# emp001 works 10 hours (has overtime)
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705345200000, "emp001")
		# emp002 works 7 hours (no overtime)
		self.whr.clock_in(1705395600000, "emp002")
		self.whr.clock_out(1705421200000, "emp002")
		result = self.whr.get_employees_with_overtime("2024-01-15")
		self.assertEqual(result, "emp001")

	@timeout(0.4)
	def test_level_3_case_09_get_total_pay(self):
		"""Test getting total pay across all dates."""
		# emp001 works 10 hours on 2024-01-15: 8*25 + 2*25*1.5 = 275
		self.whr.clock_in(1705309200000, "emp001")
		self.whr.clock_out(1705345200000, "emp001")
		self.whr.set_hourly_rate("emp001", 25)
		result = self.whr.get_total_pay("emp001")
		self.assertEqual(result, "275")

	@timeout(0.4)
	def test_level_3_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_3."""
		# emp001 works 10 hours on 2024-01-15
		self.assertEqual(self.whr.clock_in(1705309200000, "emp001"), "true")
		self.assertEqual(self.whr.clock_out(1705345200000, "emp001"), "10")
		self.assertEqual(self.whr.set_hourly_rate("emp001", 25), "true")
		self.assertEqual(self.whr.calculate_overtime_hours("emp001", "2024-01-15"), "2")
		self.assertEqual(self.whr.get_pay_for_date("emp001", "2024-01-15"), "275")
		# emp002 works 8 hours with 1 hour break on 2024-01-16
		self.assertEqual(self.whr.clock_in(1705395600000, "emp002"), "true")
		self.assertEqual(self.whr.add_break(1705402800000, 1705406400000, "emp002"), "true")
		self.assertEqual(self.whr.clock_out(1705424400000, "emp002"), "7")
		self.assertEqual(self.whr.set_hourly_rate("emp002", 20), "true")
		self.assertEqual(self.whr.get_pay_for_date("emp002", "2024-01-16"), "140")
		self.assertEqual(self.whr.get_employees_with_overtime("2024-01-15"), "emp001")
		self.assertEqual(self.whr.get_total_pay("emp001"), "275")


if __name__ == "__main__":
	unittest.main()
