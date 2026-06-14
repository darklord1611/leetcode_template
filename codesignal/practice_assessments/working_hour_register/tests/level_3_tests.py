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
	Level 3 tests for Working Hour Register - Breaks & Overtime Pay

	Tests cover: set_hourly_rate, add_break, get_pay, and breaks woven into
	get_total_hours / get_hours_in_range.
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_3_case_01_set_rate(self):
		self.whr.clock_in(1, "a")
		self.assertEqual(self.whr.set_hourly_rate(2, "a", 10), "true")

	@timeout(0.4)
	def test_level_3_case_02_set_rate_unknown(self):
		self.assertEqual(self.whr.set_hourly_rate(1, "missing", 10), "false")

	@timeout(0.4)
	def test_level_3_case_03_add_break_subtracts_total(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")  # 10
		self.assertEqual(self.whr.add_break(11, "a", 3, 5), "true")  # -2
		self.assertEqual(self.whr.get_total_hours(20, "a"), "8")

	@timeout(0.4)
	def test_level_3_case_04_break_outside_session(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")  # [0,10)
		self.assertEqual(self.whr.add_break(11, "a", 8, 12), "false")
		self.assertEqual(self.whr.get_total_hours(20, "a"), "10")

	@timeout(0.4)
	def test_level_3_case_05_break_spanning_two_sessions(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(5, "a")    # [0,5)
		self.whr.clock_in(10, "a")
		self.whr.clock_out(20, "a")   # [10,20)
		# [4,12) is not within a single session
		self.assertEqual(self.whr.add_break(21, "a", 4, 12), "false")
		self.assertEqual(self.whr.get_total_hours(30, "a"), "15")

	@timeout(0.4)
	def test_level_3_case_06_break_empty_window(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")
		self.assertEqual(self.whr.add_break(11, "a", 5, 5), "false")

	@timeout(0.4)
	def test_level_3_case_07_break_affects_range(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(20, "a")  # [0,20)
		self.whr.add_break(21, "a", 5, 9)  # -4 break inside window
		# window [0,10): raw 10, minus break overlap 4 = 6
		self.assertEqual(self.whr.get_hours_in_range(30, "a", 0, 10), "6")

	@timeout(0.4)
	def test_level_3_case_08_pay_regular_only(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(30, "a")  # 30 hours
		self.whr.set_hourly_rate(31, "a", 10)
		self.assertEqual(self.whr.get_pay(40, "a"), "300")

	@timeout(0.4)
	def test_level_3_case_09_pay_with_overtime(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(50, "a")  # 50 hours: 40 reg + 10 ot
		self.whr.set_hourly_rate(51, "a", 10)
		# 40*10 + (10*10*3)//2 = 400 + 150 = 550
		self.assertEqual(self.whr.get_pay(60, "a"), "550")

	@timeout(0.4)
	def test_level_3_case_10_pay_no_rate(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")
		self.assertEqual(self.whr.get_pay(20, "a"), "0")

	@timeout(0.4)
	def test_level_3_case_11_pay_no_hours(self):
		self.whr.clock_in(0, "a")
		self.whr.set_hourly_rate(1, "a", 10)
		self.assertEqual(self.whr.get_pay(20, "a"), "0")

	@timeout(0.4)
	def test_level_3_case_12_pay_after_break(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(44, "a")   # 44 hours
		self.whr.add_break(45, "a", 0, 4)  # -4 -> 40 hours
		self.whr.set_hourly_rate(46, "a", 10)
		self.assertEqual(self.whr.get_pay(50, "a"), "400")


if __name__ == "__main__":
	unittest.main()
