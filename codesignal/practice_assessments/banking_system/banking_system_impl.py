from banking_system import BankingSystem


class BankingSystemImpl(BankingSystem):
	"""
	Implementation of the BankingSystem interface.

	Students should implement all methods defined in the BankingSystem base class.
	Implement one level at a time, keeping in mind that you will need to refactor
	to support additional functionality in later levels.
	"""

	def __init__(self):
		"""Initialize the banking system."""
		# TODO: implement
		pass

	# Level 1 Methods: Basic Operations

	def create_account(self, timestamp: int, account_id: str) -> str:
		"""Create a new account with zero balance."""
		# TODO: implement
		pass

	def deposit(self, timestamp: int, account_id: str, amount: int) -> str:
		"""Deposit money into an account."""
		# TODO: implement
		pass

	def withdraw(self, timestamp: int, account_id: str, amount: int) -> str:
		"""Withdraw money from an account."""
		# TODO: implement
		pass

	def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> str:
		"""Transfer money from one account to another."""
		# TODO: implement
		pass

	# Level 2 Methods: Query Operations

	def top_spenders(self, timestamp: int, n: int) -> str:
		"""Get the top N accounts by total amount spent."""
		# TODO: implement
		pass

	def get_payment_history(self, timestamp: int, account_id: str, n: int) -> str:
		"""Get the last N transactions for an account."""
		# TODO: implement
		pass

	# Level 3 Methods: Scheduled Payments and Acceptance

	def schedule_payment(self, timestamp: int, account_id: str, amount: int, payment_type: str, delay: int) -> str:
		"""Schedule a payment to execute after a delay."""
		# TODO: implement
		pass

	def accept_payment(self, timestamp: int, account_id: str, payment_id: str) -> str:
		"""Accept a payment that requires 2FA confirmation."""
		# TODO: implement
		pass

	def top_activity(self, timestamp: int, n: int) -> str:
		"""Get the top N accounts by number of transactions."""
		# TODO: implement
		pass

	# Level 4 Methods: Merge Accounts and Statistics

	def get_bank_statistics(self, timestamp: int) -> str:
		"""Get overall bank statistics."""
		# TODO: implement
		pass

	def merge_accounts(self, timestamp: int, account_id1: str, account_id2: str) -> str:
		"""Merge two accounts, combining their balances and histories."""
		# TODO: implement
		pass

	def cashback(self, timestamp: int, account_id: str, percentage: int) -> str:
		"""Apply cashback rewards to an account."""
		# TODO: implement
		pass
