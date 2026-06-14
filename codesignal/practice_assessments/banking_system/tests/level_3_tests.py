import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from banking_system_impl import BankingSystemImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for Banking System - Scheduled Payments

	Tests cover: SCHEDULE_PAYMENT, CANCEL_PAYMENT, and due-payment processing
	woven into DEPOSIT / PAY / TRANSFER / TOP_SPENDERS.
	"""

	failureException = Exception

	def setUp(self):
		self.bank = BankingSystemImpl()

	@timeout(0.4)
	def test_level_3_case_01_schedule_returns_id(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.assertEqual(self.bank.schedule_payment(1, "a", 100, 10), "payment1")

	@timeout(0.4)
	def test_level_3_case_02_schedule_missing_account(self):
		self.assertEqual(self.bank.schedule_payment(1, "missing", 100, 10), "")

	@timeout(0.4)
	def test_level_3_case_03_executes_at_due_time(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(2, "a", 300, 10)  # executes at 12
		self.assertEqual(self.bank.deposit(11, "a", 0), "1000")  # not yet due
		self.assertEqual(self.bank.deposit(12, "a", 0), "700")   # due now

	@timeout(0.4)
	def test_level_3_case_04_execution_counts_outgoing(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(2, "a", 400, 5)  # executes at 7
		self.assertEqual(self.bank.top_spenders(7, 1), "a(400)")

	@timeout(0.4)
	def test_level_3_case_05_cancel_before_execution(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(2, "a", 300, 10)  # executes at 12
		self.assertEqual(self.bank.cancel_payment(3, "a", "payment1"), "true")
		self.assertEqual(self.bank.deposit(12, "a", 0), "1000")

	@timeout(0.4)
	def test_level_3_case_06_cancel_after_execution(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(2, "a", 300, 5)  # executes at 7
		self.assertEqual(self.bank.deposit(7, "a", 0), "700")
		self.assertEqual(self.bank.cancel_payment(8, "a", "payment1"), "false")

	@timeout(0.4)
	def test_level_3_case_07_cancel_wrong_account_or_id(self):
		self.bank.create_account(1, "a")
		self.bank.create_account(1, "b")
		self.bank.schedule_payment(1, "a", 100, 10)
		self.assertEqual(self.bank.cancel_payment(2, "b", "payment1"), "false")
		self.assertEqual(self.bank.cancel_payment(2, "a", "payment99"), "false")

	@timeout(0.4)
	def test_level_3_case_08_insufficient_at_execution_is_dropped(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 100)
		self.bank.schedule_payment(2, "a", 500, 5)  # executes at 7, but underfunded
		self.assertEqual(self.bank.deposit(7, "a", 0), "100")
		self.assertEqual(self.bank.top_spenders(7, 1), "a(0)")

	@timeout(0.4)
	def test_level_3_case_09_due_order_by_scheduled_time(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(1, "a", 200, 10)  # executes at 11 -> payment1
		self.bank.schedule_payment(1, "a", 300, 5)   # executes at 6  -> payment2
		self.assertEqual(self.bank.deposit(11, "a", 0), "500")

	@timeout(0.4)
	def test_level_3_case_10_due_ties_by_schedule_order(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 1000)
		self.bank.schedule_payment(1, "a", 200, 5)  # executes at 6 -> payment1
		self.bank.schedule_payment(1, "a", 300, 5)  # executes at 6 -> payment2
		self.assertEqual(self.bank.deposit(6, "a", 0), "500")

	@timeout(0.4)
	def test_level_3_case_11_processed_before_triggering_op(self):
		self.bank.create_account(1, "a")
		self.bank.deposit(1, "a", 500)
		self.bank.schedule_payment(1, "a", 400, 5)  # executes at 6
		# at t=6 the scheduled payment runs first (a -> 100), then pay(200) fails
		self.assertEqual(self.bank.pay(6, "a", 200), "")
		self.assertEqual(self.bank.deposit(7, "a", 0), "100")
		self.assertEqual(self.bank.top_spenders(7, 1), "a(400)")


if __name__ == "__main__":
	unittest.main()
