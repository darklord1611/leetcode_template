import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from banking_system_impl import BankingSystemImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for Banking System - Basic Operations

	Tests cover: CREATE_ACCOUNT, DEPOSIT, PAY, TRANSFER
	"""

	failureException = Exception

	def setUp(self):
		self.bank = BankingSystemImpl()

	@timeout(0.4)
	def test_level_1_case_01_create_account(self):
		self.assertEqual(self.bank.create_account(1, "a"), "true")

	@timeout(0.4)
	def test_level_1_case_02_create_duplicate(self):
		self.bank.create_account(1, "a")
		self.assertEqual(self.bank.create_account(2, "a"), "false")

	@timeout(0.4)
	def test_level_1_case_03_deposit(self):
		self.bank.create_account(1, "a")
		self.assertEqual(self.bank.deposit(2, "a", 1000), "1000")

	@timeout(0.4)
	def test_level_1_case_04_deposit_missing(self):
		self.assertEqual(self.bank.deposit(1, "missing", 100), "")

	@timeout(0.4)
	def test_level_1_case_05_pay(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(2, "a", 1000)
		self.assertEqual(self.bank.pay(3, "a", 300), "700")

	@timeout(0.4)
	def test_level_1_case_06_pay_insufficient(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(2, "a", 700)
		self.assertEqual(self.bank.pay(3, "a", 1000), "")

	@timeout(0.4)
	def test_level_1_case_07_pay_missing(self):
		self.assertEqual(self.bank.pay(1, "missing", 100), "")

	@timeout(0.4)
	def test_level_1_case_08_transfer(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.deposit(2, "a", 1000)
		self.assertEqual(self.bank.transfer(3, "a", "b", 400), "600")
		# b should now hold 400
		self.assertEqual(self.bank.pay(4, "b", 400), "0")

	@timeout(0.4)
	def test_level_1_case_09_transfer_missing_target(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(2, "a", 1000)
		self.assertEqual(self.bank.transfer(3, "a", "missing", 400), "")

	@timeout(0.4)
	def test_level_1_case_10_transfer_same_account(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(2, "a", 1000)
		self.assertEqual(self.bank.transfer(3, "a", "a", 100), "")

	@timeout(0.4)
	def test_level_1_case_11_transfer_insufficient(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.deposit(2, "a", 100)
		self.assertEqual(self.bank.transfer(3, "a", "b", 500), "")


if __name__ == "__main__":
	unittest.main()
