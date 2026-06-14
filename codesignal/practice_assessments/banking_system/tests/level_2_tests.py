import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from banking_system_impl import BankingSystemImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for Banking System - Outgoing Totals & Ranking

	Tests cover: TOP_SPENDERS, and reopened PAY / TRANSFER (outgoing totals).
	"""

	failureException = Exception

	def setUp(self):
		self.bank = BankingSystemImpl()
		for acc in ("a", "b", "c"):
			self.bank.create_account(1, acc)
			self.bank.deposit(1, acc, 1000)

	@timeout(0.4)
	def test_level_2_case_01_ranking(self):
		self.bank.pay(2, "a", 300)
		self.bank.transfer(3, "b", "c", 500)
		self.bank.pay(4, "c", 100)
		self.assertEqual(self.bank.top_spenders(5, 3), "b(500), a(300), c(100)")

	@timeout(0.4)
	def test_level_2_case_02_limit_n(self):
		self.bank.pay(2, "a", 300)
		self.bank.transfer(3, "b", "c", 500)
		self.bank.pay(4, "c", 100)
		self.assertEqual(self.bank.top_spenders(5, 2), "b(500), a(300)")

	@timeout(0.4)
	def test_level_2_case_03_incoming_not_counted(self):
		# c receives 500 but only its own outgoing (100) should count
		self.bank.transfer(2, "b", "c", 500)
		self.bank.pay(3, "c", 100)
		self.assertEqual(self.bank.top_spenders(4, 1), "b(500)")
		self.assertEqual(self.bank.top_spenders(4, 3), "b(500), c(100), a(0)")

	@timeout(0.4)
	def test_level_2_case_04_zero_outgoing_included_last(self):
		self.bank.pay(2, "a", 300)
		self.assertEqual(self.bank.top_spenders(3, 3), "a(300), b(0), c(0)")

	@timeout(0.4)
	def test_level_2_case_05_tie_broken_by_id(self):
		self.bank.pay(2, "c", 200)
		self.bank.pay(3, "a", 200)
		self.assertEqual(self.bank.top_spenders(4, 2), "a(200), c(200)")

	@timeout(0.4)
	def test_level_2_case_06_transfer_accrues_to_source_only(self):
		self.bank.transfer(2, "a", "b", 400)
		self.assertEqual(self.bank.top_spenders(3, 3), "a(400), b(0), c(0)")

	@timeout(0.4)
	def test_level_2_case_07_failed_pay_does_not_count(self):
		# insufficient pay should not add to outgoing
		self.bank.pay(2, "a", 5000)
		self.assertEqual(self.bank.top_spenders(3, 1), "a(0)")

	@timeout(0.4)
	def test_level_2_case_08_empty(self):
		empty = BankingSystemImpl()
		self.assertEqual(empty.top_spenders(1, 3), "")


if __name__ == "__main__":
	unittest.main()
