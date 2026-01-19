import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from banking_system_impl import BankingSystemImpl


class Level2Tests(unittest.TestCase):
    """
    Level 2 tests for Banking System - Query Operations

    Tests cover: TOP_SPENDERS, GET_PAYMENT_HISTORY
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh BankingSystem instance for each test."""
        self.bank = BankingSystemImpl()

    @timeout(0.4)
    def test_level_2_case_01_top_spenders_basic(self):
        """Test top spenders with withdrawals and transfers."""
        self.bank.create_account(1, "account1")
        self.bank.create_account(2, "account2")
        self.bank.create_account(3, "account3")
        self.bank.deposit(4, "account1", 2000)
        self.bank.deposit(5, "account2", 1500)
        self.bank.deposit(6, "account3", 3000)
        self.bank.withdraw(7, "account1", 500)        # account1 spent: 500
        self.bank.withdraw(8, "account2", 300)        # account2 spent: 300
        self.bank.transfer(9, "account1", "account3", 400)  # account1 spent: 500+400=900
        self.bank.transfer(10, "account2", "account3", 200) # account2 spent: 300+200=500
        self.bank.withdraw(11, "account3", 1000)      # account3 spent: 1000
        result = self.bank.top_spenders(12, 2)
        self.assertEqual(result, "account3(1000), account1(900)")

    @timeout(0.4)
    def test_level_2_case_02_payment_history_basic(self):
        """Test payment history returns recent transactions."""
        self.bank.create_account(1, "account1")
        self.bank.deposit(2, "account1", 2000)
        self.bank.withdraw(3, "account1", 500)
        self.bank.transfer(4, "account1", "account2", 400)
        result = self.bank.get_payment_history(5, "account1", 3)
        # Most recent first: TRANSFER_OUT, WITHDRAW, DEPOSIT
        self.assertEqual(result, "TRANSFER_OUT(400), WITHDRAW(500), DEPOSIT(2000)")

    @timeout(0.4)
    def test_level_2_case_03_payment_history_with_transfer_in(self):
        """Test payment history includes incoming transfers."""
        self.bank.create_account(1, "account1")
        self.bank.create_account(2, "account2")
        self.bank.create_account(3, "account3")
        self.bank.deposit(4, "account1", 2000)
        self.bank.deposit(5, "account3", 3000)
        self.bank.transfer(6, "account1", "account3", 400)
        self.bank.transfer(7, "account2", "account3", 200)
        self.bank.withdraw(8, "account3", 1000)
        result = self.bank.get_payment_history(9, "account3", 5)
        # Most recent first
        self.assertEqual(result, "WITHDRAW(1000), TRANSFER_IN(200), TRANSFER_IN(400), DEPOSIT(3000)")

    @timeout(0.4)
    def test_level_2_case_04_top_spenders_empty(self):
        """Test top spenders with no spending."""
        self.bank.create_account(1, "account1")
        self.bank.deposit(2, "account1", 1000)
        result = self.bank.top_spenders(3, 5)
        # account1 has no spending (only deposit)
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_2_case_05_top_spenders_ordering(self):
        """Test top spenders are ordered by amount descending, then by ID ascending."""
        self.bank.create_account(1, "account1")
        self.bank.create_account(2, "account2")
        self.bank.create_account(3, "account3")
        self.bank.deposit(4, "account1", 1000)
        self.bank.deposit(5, "account2", 1000)
        self.bank.deposit(6, "account3", 1000)
        self.bank.withdraw(7, "account1", 300)  # account1: 300
        self.bank.withdraw(8, "account2", 500)  # account2: 500
        self.bank.withdraw(9, "account3", 300)  # account3: 300
        result = self.bank.top_spenders(10, 3)
        # account2(500) first, then account1 and account3 (both 300) sorted by ID
        self.assertEqual(result, "account2(500), account1(300), account3(300)")

    @timeout(0.4)
    def test_level_2_case_06_payment_history_limit(self):
        """Test payment history respects the limit parameter."""
        self.bank.create_account(1, "account1")
        self.bank.deposit(2, "account1", 100)
        self.bank.deposit(3, "account1", 200)
        self.bank.deposit(4, "account1", 300)
        self.bank.deposit(5, "account1", 400)
        result = self.bank.get_payment_history(6, "account1", 2)
        # Only 2 most recent
        self.assertEqual(result, "DEPOSIT(400), DEPOSIT(300)")

    @timeout(0.4)
    def test_level_2_case_07_top_spenders_with_limit(self):
        """Test top spenders respects the limit parameter."""
        for i in range(5):
            self.bank.create_account(i, f"account{i}")
            self.bank.deposit(i+10, f"account{i}", 1000)
            self.bank.withdraw(i+20, f"account{i}", (i+1)*100)
        result = self.bank.top_spenders(100, 3)
        # Top 3: account4(500), account3(400), account2(300)
        self.assertEqual(result, "account4(500), account3(400), account2(300)")

    @timeout(0.4)
    def test_level_2_case_08_payment_history_empty_account(self):
        """Test payment history for account with no transactions."""
        self.bank.create_account(1, "account1")
        result = self.bank.get_payment_history(2, "account1", 5)
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_2_case_09_multiple_operations(self):
        """Test combination of deposits, withdrawals, and transfers."""
        self.bank.create_account(1, "acc1")
        self.bank.create_account(2, "acc2")
        self.bank.deposit(3, "acc1", 1000)
        self.bank.deposit(4, "acc2", 500)
        self.bank.withdraw(5, "acc1", 100)
        self.bank.transfer(6, "acc1", "acc2", 200)
        self.bank.withdraw(7, "acc2", 50)
        # acc1 spent: 100 + 200 = 300
        # acc2 spent: 50
        result = self.bank.top_spenders(8, 2)
        self.assertEqual(result, "acc1(300), acc2(50)")

    @timeout(0.4)
    def test_level_2_case_10_complete_scenario(self):
        """Test complete scenario from test_data_2."""
        self.bank.create_account(1, "account1")
        self.bank.create_account(2, "account2")
        self.bank.create_account(3, "account3")
        self.bank.deposit(4, "account1", 2000)
        self.bank.deposit(5, "account2", 1500)
        self.bank.deposit(6, "account3", 3000)
        self.bank.withdraw(7, "account1", 500)
        self.bank.withdraw(8, "account2", 300)
        self.bank.transfer(9, "account1", "account3", 400)
        self.bank.transfer(10, "account2", "account3", 200)
        self.bank.withdraw(11, "account3", 1000)

        result1 = self.bank.top_spenders(12, 2)
        self.assertEqual(result1, "account3(1000), account1(900)")

        result2 = self.bank.get_payment_history(13, "account1", 3)
        self.assertEqual(result2, "TRANSFER_OUT(400), WITHDRAW(500), DEPOSIT(2000)")

        result3 = self.bank.get_payment_history(14, "account3", 5)
        self.assertEqual(result3, "WITHDRAW(1000), TRANSFER_IN(200), TRANSFER_IN(400), DEPOSIT(3000)")


if __name__ == '__main__':
    unittest.main()
