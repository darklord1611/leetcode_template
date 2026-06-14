import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from banking_system_impl import BankingSystemImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for Banking System - Merging Accounts & Historical Balance

	Tests cover: MERGE_ACCOUNTS, GET_BALANCE, and merge-awareness of the
	previously implemented operations.
	"""

	failureException = Exception

	def setUp(self):
		self.bank = BankingSystemImpl()

	@timeout(0.4)
	def test_level_4_case_01_merge_combines_balance(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.deposit(1, "a", 1000)
		self.bank.deposit(1, "b", 500)
		self.assertEqual(self.bank.merge_accounts(5, "a", "b"), "true")
		self.assertEqual(self.bank.get_balance(5, "a", 5), "1500")

	@timeout(0.4)
	def test_level_4_case_02_merge_invalid(self):
		self.bank.create_account(1, "a")
		self.assertEqual(self.bank.merge_accounts(2, "a", "a"), "false")
		self.assertEqual(self.bank.merge_accounts(2, "a", "missing"), "false")
		self.assertEqual(self.bank.merge_accounts(2, "missing", "a"), "false")

	@timeout(0.4)
	def test_level_4_case_03_merged_account_gone(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.merge_accounts(2, "a", "b")
		self.assertEqual(self.bank.deposit(3, "b", 100), "")

	@timeout(0.4)
	def test_level_4_case_04_merge_combines_outgoing(self):
		for acc in ("a", "b", "c"):
			self.bank.create_account(1, acc)
			self.bank.deposit(1, acc, 1000)
		self.bank.pay(2, "a", 300)
		self.bank.pay(2, "b", 200)
		self.bank.merge_accounts(3, "a", "b")
		self.assertEqual(self.bank.top_spenders(4, 2), "a(500), c(0)")

	@timeout(0.4)
	def test_level_4_case_05_merge_reassigns_scheduled_payments(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.deposit(1, "b", 1000)
		self.bank.schedule_payment(1, "b", 300, 10)  # executes at 11
		self.bank.merge_accounts(2, "a", "b")          # payment now belongs to a
		self.assertEqual(self.bank.deposit(11, "a", 0), "700")
		self.assertEqual(self.bank.top_spenders(11, 1), "a(300)")

	@timeout(0.4)
	def test_level_4_case_06_historical_balance(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(2, "a", 1000)
		self.bank.pay(5, "a", 400)
		self.assertEqual(self.bank.get_balance(10, "a", 1), "0")
		self.assertEqual(self.bank.get_balance(10, "a", 2), "1000")
		self.assertEqual(self.bank.get_balance(10, "a", 5), "600")

	@timeout(0.4)
	def test_level_4_case_07_historical_before_creation(self):
		self.bank.create_account(3, "a")
		self.bank.deposit(3, "a", 1000)
		self.assertEqual(self.bank.get_balance(10, "a", 2), "")

	@timeout(0.4)
	def test_level_4_case_08_historical_around_merge(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.deposit(1, "a", 1000)
		self.bank.deposit(1, "b", 500)
		self.bank.merge_accounts(5, "a", "b")
		self.assertEqual(self.bank.get_balance(10, "b", 3), "500")
		self.assertEqual(self.bank.get_balance(10, "b", 5), "")
		self.assertEqual(self.bank.get_balance(10, "a", 3), "1000")
		self.assertEqual(self.bank.get_balance(10, "a", 6), "1500")

	@timeout(0.4)
	def test_level_4_case_09_historical_with_scheduled_execution(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(2, "a", 300, 5)  # executes at 7
		self.assertEqual(self.bank.get_balance(10, "a", 6), "1000")
		self.assertEqual(self.bank.get_balance(10, "a", 7), "700")

	@timeout(0.4)
	def test_level_4_case_10_get_balance_missing(self):
		self.assertEqual(self.bank.get_balance(5, "missing", 3), "")


if __name__ == "__main__":
	unittest.main()
