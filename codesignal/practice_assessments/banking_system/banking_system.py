"""
Banking System - Abstract Base Class

This class defines the interface for a simplified banking system
with account management, transactions, scheduled payments, and analytics.
"""


class BankingSystem:
	"""
	Abstract base class for a banking system that manages accounts,
	transactions, scheduled payments, and provides various query operations.
	"""

	def __init__(self):
		"""Initialize the banking system."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: Basic Operations

	def create_account(self, timestamp: int, account_id: str) -> str:
		"""
		Create a new account with zero balance.

		Args:
		    timestamp (int): Transaction timestamp
		    account_id (str): Unique identifier for the account

		Returns:
		    str: "true" if account created successfully, "false" if account already exists
		"""
		raise NotImplementedError("Subclasses must implement create_account()")

	def deposit(self, timestamp: int, account_id: str, amount: int) -> str:
		"""
		Deposit money into an account.

		Args:
		    timestamp (int): Transaction timestamp
		    account_id (str): Account to deposit into
		    amount (int): Amount to deposit

		Returns:
		    str: New balance as string if successful, "" if account doesn't exist
		"""
		raise NotImplementedError("Subclasses must implement deposit()")

	def withdraw(self, timestamp: int, account_id: str, amount: int) -> str:
		"""
		Withdraw money from an account.

		Args:
		    timestamp (int): Transaction timestamp
		    account_id (str): Account to withdraw from
		    amount (int): Amount to withdraw

		Returns:
		    str: New balance as string if successful,
		         "" if account doesn't exist or insufficient funds
		"""
		raise NotImplementedError("Subclasses must implement withdraw()")

	def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> str:
		"""
		Transfer money from one account to another.

		Args:
		    timestamp (int): Transaction timestamp
		    source_account_id (str): Account to transfer from
		    target_account_id (str): Account to transfer to
		    amount (int): Amount to transfer

		Returns:
		    str: Source account's new balance as string if successful,
		         "" if either account doesn't exist or insufficient funds
		"""
		raise NotImplementedError("Subclasses must implement transfer()")

	# Level 2 Methods: Query Operations

	def top_spenders(self, timestamp: int, n: int) -> str:
		"""
		Get the top N accounts by total amount spent (withdrawals + transfers out).

		Args:
		    timestamp (int): Query timestamp
		    n (int): Number of top spenders to return

		Returns:
		    str: Formatted string "account1(amount), account2(amount), ..."
		         sorted by amount descending, then by account_id ascending
		"""
		raise NotImplementedError("Subclasses must implement top_spenders()")

	def get_payment_history(self, timestamp: int, account_id: str, n: int) -> str:
		"""
		Get the last N transactions for an account.

		Args:
		    timestamp (int): Query timestamp
		    account_id (str): Account to query
		    n (int): Number of transactions to return

		Returns:
		    str: Formatted string "OPERATION(amount), OPERATION(amount), ..."
		         where operations are: DEPOSIT, WITHDRAW, TRANSFER_IN, TRANSFER_OUT
		         in reverse chronological order (most recent first)
		"""
		raise NotImplementedError("Subclasses must implement get_payment_history()")

	# Level 3 Methods: Scheduled Payments and Acceptance

	def schedule_payment(self, timestamp: int, account_id: str, amount: int, payment_type: str, delay: int) -> str:
		"""
		Schedule a payment to execute after a delay.

		Args:
		    timestamp (int): Scheduling timestamp
		    account_id (str): Account for the payment
		    amount (int): Amount for the payment
		    payment_type (str): Type of payment ("DEPOSIT" or "WITHDRAW")
		    delay (int): Milliseconds to wait before executing

		Returns:
		    str: "true" if scheduled successfully
		"""
		raise NotImplementedError("Subclasses must implement schedule_payment()")

	def accept_payment(self, timestamp: int, account_id: str, payment_id: str) -> str:
		"""
		Accept a payment that requires 2FA confirmation.

		Large transactions (amount > 1000) require acceptance via payment_id.

		Args:
		    timestamp (int): Acceptance timestamp
		    account_id (str): Account for the payment
		    payment_id (str): Payment identifier (e.g., "payment_1")

		Returns:
		    str: New account balance as string after accepting the payment
		"""
		raise NotImplementedError("Subclasses must implement accept_payment()")

	def top_activity(self, timestamp: int, n: int) -> str:
		"""
		Get the top N accounts by number of transactions.

		Args:
		    timestamp (int): Query timestamp
		    n (int): Number of accounts to return

		Returns:
		    str: Formatted string "account1(count), account2(count), ..."
		         sorted by count descending, then by account_id ascending
		"""
		raise NotImplementedError("Subclasses must implement top_activity()")

	# Level 4 Methods: Merge Accounts and Statistics

	def get_bank_statistics(self, timestamp: int) -> str:
		"""
		Get overall bank statistics.

		Args:
		    timestamp (int): Query timestamp

		Returns:
		    str: "total_accounts:N,total_balance:B,average_balance:A"
		         where average_balance is rounded down to integer
		"""
		raise NotImplementedError("Subclasses must implement get_bank_statistics()")

	def merge_accounts(self, timestamp: int, account_id1: str, account_id2: str) -> str:
		"""
		Merge two accounts, combining their balances and histories.

		The second account is merged into the first, and the second account is removed.

		Args:
		    timestamp (int): Merge timestamp
		    account_id1 (str): First account (will receive merged balance)
		    account_id2 (str): Second account (will be removed)

		Returns:
		    str: New balance of account_id1 as string after merge
		"""
		raise NotImplementedError("Subclasses must implement merge_accounts()")

	def cashback(self, timestamp: int, account_id: str, percentage: int) -> str:
		"""
		Apply cashback rewards to an account.

		Calculates cashback as percentage of total spending (withdrawals + transfers out)
		and adds it to the account balance.

		Args:
		    timestamp (int): Cashback timestamp
		    account_id (str): Account to apply cashback to
		    percentage (int): Cashback percentage (e.g., 10 for 10%)

		Returns:
		    str: Cashback amount as string (not the new balance, just the cashback)
		"""
		raise NotImplementedError("Subclasses must implement cashback()")
