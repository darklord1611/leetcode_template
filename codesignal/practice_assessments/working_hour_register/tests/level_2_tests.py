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
	Level 2 tests for Working Hour Register - Range Queries

	Tests cover: get_hours_in_range, get_top_employees_by_hours
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_2_case_01_range_full_session(self):
		self.whr.clock_in(2, "a")
		self.whr.clock_out(10, "a")  # session [2,10) = 8
		self.assertEqual(self.whr.get_hours_in_range(20, "a", 0, 20), "8")

	@timeout(0.4)
	def test_level_2_case_02_range_clips_left(self):
		self.whr.clock_in(2, "a")
		self.whr.clock_out(10, "a")  # [2,10)
		self.assertEqual(self.whr.get_hours_in_range(20, "a", 5, 20), "5")

	@timeout(0.4)
	def test_level_2_case_03_range_clips_right(self):
		self.whr.clock_in(2, "a")
		self.whr.clock_out(10, "a")  # [2,10)
		self.assertEqual(self.whr.get_hours_in_range(20, "a", 0, 6), "4")

	@timeout(0.4)
	def test_level_2_case_04_range_clips_both(self):
		self.whr.clock_in(2, "a")
		self.whr.clock_out(20, "a")  # [2,20)
		self.assertEqual(self.whr.get_hours_in_range(30, "a", 5, 11), "6")

	@timeout(0.4)
	def test_level_2_case_05_range_no_overlap(self):
		self.whr.clock_in(2, "a")
		self.whr.clock_out(10, "a")  # [2,10)
		self.assertEqual(self.whr.get_hours_in_range(20, "a", 12, 20), "0")

	@timeout(0.4)
	def test_level_2_case_06_range_multiple_sessions(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(5, "a")    # [0,5)
		self.whr.clock_in(10, "a")
		self.whr.clock_out(20, "a")   # [10,20)
		# window [3,15): 2 from first + 5 from second = 7
		self.assertEqual(self.whr.get_hours_in_range(30, "a", 3, 15), "7")

	@timeout(0.4)
	def test_level_2_case_07_range_unknown_employee(self):
		self.assertEqual(self.whr.get_hours_in_range(20, "missing", 0, 20), "0")

	@timeout(0.4)
	def test_level_2_case_08_top_basic_order(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")  # 10
		self.whr.clock_in(0, "b")
		self.whr.clock_out(3, "b")   # 3
		self.assertEqual(self.whr.get_top_employees_by_hours(20, 2), "a(10), b(3)")

	@timeout(0.4)
	def test_level_2_case_09_top_tie_by_id(self):
		self.whr.clock_in(0, "b")
		self.whr.clock_out(5, "b")   # 5
		self.whr.clock_in(0, "a")
		self.whr.clock_out(5, "a")   # 5
		self.assertEqual(self.whr.get_top_employees_by_hours(20, 2), "a(5), b(5)")

	@timeout(0.4)
	def test_level_2_case_10_top_limit_n(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(10, "a")
		self.whr.clock_in(0, "b")
		self.whr.clock_out(7, "b")
		self.whr.clock_in(0, "c")
		self.whr.clock_out(3, "c")
		self.assertEqual(self.whr.get_top_employees_by_hours(20, 2), "a(10), b(7)")

	@timeout(0.4)
	def test_level_2_case_11_top_none(self):
		self.assertEqual(self.whr.get_top_employees_by_hours(20, 3), "")

	@timeout(0.4)
	def test_level_2_case_12_top_excludes_open_session(self):
		self.whr.clock_in(0, "a")
		self.whr.clock_out(4, "a")   # 4 completed
		self.whr.clock_in(10, "a")   # open, ignored
		self.assertEqual(self.whr.get_top_employees_by_hours(20, 1), "a(4)")


if __name__ == "__main__":
	unittest.main()
