import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from timeout_decorator import timeout
from working_hour_register_impl import WorkingHourRegisterImpl


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for Working Hour Register - Range Pay & Payroll

	Tests cover: get_pay_in_range, generate_payroll
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_4_case_01_pay_in_range_basic(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(30, "a")  # [0,30)
		self.whr.set_hourly_rate(31, "a", 10)
		# window [0,20): 20 hours, regular -> 200
		self.assertEqual(self.whr.get_pay_in_range(40, "a", 0, 20), "200")

	@timeout(0.4)
	def test_level_4_case_02_pay_in_range_clips(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(60, "a")  # [0,60)
		self.whr.set_hourly_rate(61, "a", 10)
		# window [10,40): 30 hours -> 300
		self.assertEqual(self.whr.get_pay_in_range(70, "a", 10, 40), "300")

	@timeout(0.4)
	def test_level_4_case_03_pay_in_range_overtime(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(60, "a")  # [0,60)
		self.whr.set_hourly_rate(61, "a", 10)
		# window [0,50): 50 hours -> 40*10 + (10*10*3)//2 = 550
		self.assertEqual(self.whr.get_pay_in_range(70, "a", 0, 50), "550")

	@timeout(0.4)
	def test_level_4_case_04_pay_in_range_no_rate(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(20, "a")
		self.assertEqual(self.whr.get_pay_in_range(30, "a", 0, 20), "0")

	@timeout(0.4)
	def test_level_4_case_05_pay_in_range_no_hours(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")
		self.whr.set_hourly_rate(11, "a", 10)
		self.assertEqual(self.whr.get_pay_in_range(30, "a", 20, 30), "0")

	@timeout(0.4)
	def test_level_4_case_06_pay_in_range_with_break(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(30, "a")  # [0,30)
		self.whr.add_break(31, "a", 5, 10)  # -5 inside window
		self.whr.set_hourly_rate(32, "a", 10)
		# window [0,20): raw 20 minus break 5 = 15 hours -> 150
		self.assertEqual(self.whr.get_pay_in_range(40, "a", 0, 20), "150")

	@timeout(0.4)
	def test_level_4_case_07_payroll_basic(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(20, "a")
		self.whr.set_hourly_rate(21, "a", 10)
		self.whr.clock_in(0, "b")
		self.whr.clock_out(10, "b")
		self.whr.set_hourly_rate(11, "b", 20)
		# a: 20*10=200, b: 10*20=200
		self.assertEqual(self.whr.generate_payroll(30, 0, 30), "a(200), b(200)")

	@timeout(0.4)
	def test_level_4_case_08_payroll_sorted_by_id(self):
		self.whr.clock_in(0, "b")
		self.whr.clock_out(10, "b")
		self.whr.set_hourly_rate(11, "b", 10)
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")
		self.whr.set_hourly_rate(11, "a", 10)
		self.assertEqual(self.whr.generate_payroll(30, 0, 30), "a(100), b(100)")

	@timeout(0.4)
	def test_level_4_case_09_payroll_excludes_no_hours(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")
		self.whr.set_hourly_rate(11, "a", 10)
		self.whr.clock_in(0, "b")
		self.whr.clock_out(10, "b")
		self.whr.set_hourly_rate(11, "b", 10)
		# window [0,5): only a and b each worked 5 -> both included
		# window [50,60): no one worked -> excluded entirely
		self.assertEqual(self.whr.generate_payroll(70, 50, 60), "")

	@timeout(0.4)
	def test_level_4_case_10_payroll_window_clips(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(60, "a")
		self.whr.set_hourly_rate(61, "a", 10)
		# window [0,50): 50 hours -> 550
		self.assertEqual(self.whr.generate_payroll(70, 0, 50), "a(550)")

	@timeout(0.4)
	def test_level_4_case_11_payroll_no_rate_excluded(self):
		# employee with hours but no rate contributes pay 0 and is excluded
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")  # no rate set
		self.whr.clock_in(0, "b")
		self.whr.clock_out(10, "b")
		self.whr.set_hourly_rate(11, "b", 10)
		self.assertEqual(self.whr.generate_payroll(30, 0, 30), "b(100)")


if __name__ == "__main__":
	unittest.main()
