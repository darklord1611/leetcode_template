"""
Banking System - Abstract Base Class

A simplified banking system. The set of operations is intentionally small:
later levels extend the BEHAVIOUR of the same functions rather than adding many
new ones. Implement one level at a time and expect to reopen earlier functions.
"""


class BankingSystem:
	"""Abstract base class for the banking system."""

	def __init__(self):
		"""Initialize the banking system."""
		raise NotImplementedError("Subclasses must implement __init__")

	# Level 1 Methods: Basic Operations

	def create_account(self, timestamp: int, account_id: str) -> str:
		"""
		Create a new account with balance 0.

		Returns:
		    str: "true" if created, "false" if the account already exists.
		"""
		raise NotImplementedError("Subclasses must implement create_account()")

	def deposit(self, timestamp: int, account_id: str, amount: int) -> str:
		"""
		Add amount to the account's balance.

		Returns:
		    str: The new balance, or "" if the account does not exist.
		"""
		raise NotImplementedError("Subclasses must implement deposit()")

	def pay(self, timestamp: int, account_id: str, amount: int) -> str:
		"""
		Withdraw amount from the account (an outgoing payment).

		Returns:
		    str: The new balance, or "" if the account is missing or underfunded.
		"""
		raise NotImplementedError("Subclasses must implement pay()")

	def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> str:
		"""
		Move amount from source to target.

		Returns:
		    str: The source account's new balance, or "" on failure
		         (missing account, same account, or insufficient funds).
		"""
		raise NotImplementedError("Subclasses must implement transfer()")

	# Level 2 Methods: Outgoing Totals & Ranking
	# (PAY and TRANSFER must be reopened to accumulate outgoing totals.)

	def top_spenders(self, timestamp: int, n: int) -> str:
		"""
		Return the top n accounts by outgoing total.

		Returns:
		    str: "id1(total1), id2(total2), ..." (desc by total, ties by id asc).
		"""
		raise NotImplementedError("Subclasses must implement top_spenders()")

	# Level 3 Methods: Scheduled Payments
	# (All transaction operations must process due scheduled payments first.)

	def schedule_payment(self, timestamp: int, account_id: str, amount: int, delay: int) -> str:
		"""
		Schedule a payment from account_id to execute at timestamp + delay.

		Returns:
		    str: A payment id "paymentN", or "" if the account does not exist.
		"""
		raise NotImplementedError("Subclasses must implement schedule_payment()")

	def cancel_payment(self, timestamp: int, account_id: str, payment_id: str) -> str:
		"""
		Cancel a not-yet-executed scheduled payment belonging to account_id.

		Returns:
		    str: "true" if cancelled, otherwise "false".
		"""
		raise NotImplementedError("Subclasses must implement cancel_payment()")

	# Level 4 Methods: Merging Accounts & Historical Balance

	def merge_accounts(self, timestamp: int, account_id_1: str, account_id_2: str) -> str:
		"""
		Merge account_id_2 into account_id_1 (balances, outgoing totals, and
		pending scheduled payments combine); account_id_2 ceases to exist.

		Returns:
		    str: "true" on success, "false" if ids are equal or either is missing.
		"""
		raise NotImplementedError("Subclasses must implement merge_accounts()")

	def get_balance(self, timestamp: int, account_id: str, time_at: int) -> str:
		"""
		Return the account's balance as it was at the historical time time_at.

		Returns:
		    str: The historical balance, or "" if the account did not exist at
		         time_at (or had been merged away by then).
		"""
		raise NotImplementedError("Subclasses must implement get_balance()")
