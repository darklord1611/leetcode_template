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

	Tests cover: CREATE_ACCOUNT, DEPOSIT, WITHDRAW, TRANSFER
	All tests have a 0.4 second timeout.
	"""

	failureException = Exception

	def setUp(self):
		"""Create a fresh BankingSystem instance for each test."""
		self.bank = BankingSystemImpl()

	@timeout(0.4)
	def test_level_1_case_01_create_account(self):
		"""Test creating a new account."""
		result = self.bank.create_account(1, "account1")
		self.assertEqual(result, "true")

	@timeout(0.4)
	def test_level_1_case_02_create_duplicate_account(self):
		"""Test that duplicate account creation returns false."""
		self.bank.create_account(1, "account1")
		result = self.bank.create_account(2, "account1")
		self.assertEqual(result, "false")

	@timeout(0.4)
	def test_level_1_case_03_deposit_to_existing_account(self):
		"""Test depositing money to an existing account."""
		self.bank.create_account(1, "account1")
		result = self.bank.deposit(2, "account1", 1000)
		self.assertEqual(result, "1000")

	@timeout(0.4)
	def test_level_1_case_04_deposit_to_nonexistent_account(self):
		"""Test depositing to non-existent account returns empty string."""
		result = self.bank.deposit(1, "nonexistent", 100)
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_1_case_05_withdraw_with_sufficient_funds(self):
		"""Test withdrawal with sufficient balance."""
		self.bank.create_account(1, "account1")
		self.bank.deposit(2, "account1", 1000)
		result = self.bank.withdraw(3, "account1", 200)
		self.assertEqual(result, "800")

	@timeout(0.4)
	def test_level_1_case_06_withdraw_with_insufficient_funds(self):
		"""Test withdrawal with insufficient balance returns empty string."""
		self.bank.create_account(1, "account1")
		self.bank.deposit(2, "account1", 500)
		result = self.bank.withdraw(3, "account1", 600)
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_1_case_07_transfer_with_sufficient_funds(self):
		"""Test transfer between accounts with sufficient balance."""
		self.bank.create_account(1, "account1")
		self.bank.create_account(2, "account2")
		self.bank.deposit(3, "account1", 1000)
		result = self.bank.transfer(4, "account1", "account2", 300)
		self.assertEqual(result, "700")

	@timeout(0.4)
	def test_level_1_case_08_transfer_with_insufficient_funds(self):
		"""Test transfer with insufficient balance returns empty string."""
		self.bank.create_account(1, "account1")
		self.bank.create_account(2, "account2")
		self.bank.deposit(3, "account1", 200)
		result = self.bank.transfer(4, "account1", "account2", 300)
		self.assertEqual(result, "")

	@timeout(0.4)
	def test_level_1_case_09_multiple_deposits(self):
		"""Test multiple deposits accumulate correctly."""
		self.bank.create_account(1, "account1")
		self.assertEqual(self.bank.deposit(2, "account1", 100), "100")
		self.assertEqual(self.bank.deposit(3, "account1", 200), "300")
		self.assertEqual(self.bank.deposit(4, "account1", 150), "450")

	@timeout(0.4)
	def test_level_1_case_10_complete_scenario(self):
		"""Test complete scenario from test_data_1."""
		self.assertEqual(self.bank.create_account(1, "account1"), "true")
		self.assertEqual(self.bank.create_account(2, "account2"), "true")
		self.assertEqual(self.bank.create_account(3, "account1"), "false")
		self.assertEqual(self.bank.deposit(4, "account1", 1000), "1000")
		self.assertEqual(self.bank.deposit(5, "account2", 500), "500")
		self.assertEqual(self.bank.withdraw(6, "account1", 200), "800")
		self.assertEqual(self.bank.withdraw(7, "account2", 600), "")
		self.assertEqual(self.bank.transfer(8, "account1", "account2", 300), "500")
		self.assertEqual(self.bank.deposit(9, "account3", 100), "")


if __name__ == "__main__":
	unittest.main()
