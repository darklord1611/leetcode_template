from banking_system import BankingSystem


class BankingSystemImpl(BankingSystem):
	"""
	Implementation of the BankingSystem interface.

	The function set is small on purpose. Implement one level at a time and
	expect to reopen earlier functions to satisfy later requirements.
	"""

	def __init__(self):
		"""Initialize the banking system."""
		# TODO: implement
		pass

	# Level 1 Methods: Basic Operations

	def create_account(self, timestamp: int, account_id: str) -> str:
		"""Create a new account with balance 0."""
		# TODO: implement
		pass

	def deposit(self, timestamp: int, account_id: str, amount: int) -> str:
		"""Add amount to the account's balance."""
		# TODO: implement
		pass

	def pay(self, timestamp: int, account_id: str, amount: int) -> str:
		"""Withdraw amount from the account (an outgoing payment)."""
		# TODO: implement
		pass

	def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> str:
		"""Move amount from source to target."""
		# TODO: implement
		pass

	# Level 2 Methods: Outgoing Totals & Ranking

	def top_spenders(self, timestamp: int, n: int) -> str:
		"""Return the top n accounts by outgoing total."""
		# TODO: implement
		pass

	# Level 3 Methods: Scheduled Payments

	def schedule_payment(self, timestamp: int, account_id: str, amount: int, delay: int) -> str:
		"""Schedule a payment from account_id to execute at timestamp + delay."""
		# TODO: implement
		pass

	def cancel_payment(self, timestamp: int, account_id: str, payment_id: str) -> str:
		"""Cancel a not-yet-executed scheduled payment belonging to account_id."""
		# TODO: implement
		pass

	# Level 4 Methods: Merging Accounts & Historical Balance

	def merge_accounts(self, timestamp: int, account_id_1: str, account_id_2: str) -> str:
		"""Merge account_id_2 into account_id_1."""
		# TODO: implement
		pass

	def get_balance(self, timestamp: int, account_id: str, time_at: int) -> str:
		"""Return the account's balance as it was at the historical time time_at."""
		# TODO: implement
		pass
