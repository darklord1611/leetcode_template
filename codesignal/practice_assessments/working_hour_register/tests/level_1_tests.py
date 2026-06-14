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
	Level 1 tests for Working Hour Register - Basic Clock In/Out

	Tests cover: clock_in, clock_out, is_clocked_in, get_total_hours
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		self.whr = WorkingHourRegisterImpl()

	@timeout(0.4)
	def test_level_1_case_01_clock_in(self):
		self.assertEqual(self.whr.clock_in(1, "a"), "true")

	@timeout(0.4)
	def test_level_1_case_02_clock_in_already_in(self):
		self.whr.clock_in(1, "a")
		self.assertEqual(self.whr.clock_in(2, "a"), "false")

	@timeout(0.4)
	def test_level_1_case_03_is_clocked_in_true(self):
		self.whr.clock_in(1, "a")
		self.assertEqual(self.whr.is_clocked_in(2, "a"), "true")

	@timeout(0.4)
	def test_level_1_case_04_is_clocked_in_unknown(self):
		self.assertEqual(self.whr.is_clocked_in(1, "missing"), "false")

	@timeout(0.4)
	def test_level_1_case_05_clock_out_returns_duration(self):
		self.whr.clock_in(1, "a")
		self.assertEqual(self.whr.clock_out(9, "a"), "8")

	@timeout(0.4)
	def test_level_1_case_06_clock_out_not_in(self):
		self.whr.clock_in(1, "a")
		self.whr.clock_out(5, "a")
		self.assertEqual(self.whr.clock_out(7, "a"), "")

	@timeout(0.4)
	def test_level_1_case_07_clock_out_unknown(self):
		self.assertEqual(self.whr.clock_out(1, "missing"), "")

	@timeout(0.4)
	def test_level_1_case_08_is_clocked_in_after_out(self):
		self.whr.clock_in(1, "a")
		self.whr.clock_out(5, "a")
		self.assertEqual(self.whr.is_clocked_in(6, "a"), "false")

	@timeout(0.4)
	def test_level_1_case_09_total_hours_sums_sessions(self):
		self.whr.clock_in(1, "a")
		self.whr.clock_out(5, "a")   # 4
		self.whr.clock_in(10, "a")
		self.whr.clock_out(13, "a")  # 3
		self.assertEqual(self.whr.get_total_hours(20, "a"), "7")

	@timeout(0.4)
	def test_level_1_case_10_total_hours_unknown(self):
		self.assertEqual(self.whr.get_total_hours(1, "missing"), "0")

	@timeout(0.4)
	def test_level_1_case_11_total_excludes_open_session(self):
		self.whr.clock_in(1, "a")
		self.whr.clock_out(5, "a")   # 4
		self.whr.clock_in(10, "a")   # still open
		self.assertEqual(self.whr.get_total_hours(20, "a"), "4")

	@timeout(0.4)
	def test_level_1_case_12_reclock_after_out(self):
		self.whr.clock_in(1, "a")
		self.whr.clock_out(5, "a")
		self.assertEqual(self.whr.clock_in(6, "a"), "true")


if __name__ == "__main__":
	unittest.main()
