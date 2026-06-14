from in_memory_database import InMemoryDatabase


class InMemoryDatabaseImpl(InMemoryDatabase):
	"""
	Implementation of the InMemoryDatabase interface.

	The function set is small on purpose. Implement one level at a time and
	expect to reopen earlier functions to satisfy later requirements.
	"""

	def __init__(self):
		"""Initialize the in-memory database."""
		# TODO: implement
		pass

	# Level 1 Methods: Field Operations

	def set_field(self, timestamp: int, key: str, field: str, value: str) -> str:
		"""Set a field's value for a key, creating the record if needed."""
		# TODO: implement
		pass

	def get_field(self, timestamp: int, key: str, field: str) -> str:
		"""Get a field's value for a key."""
		# TODO: implement
		pass

	def delete_field(self, timestamp: int, key: str, field: str) -> str:
		"""Delete a field from a key."""
		# TODO: implement
		pass

	def get_record(self, timestamp: int, key: str) -> str:
		"""Get a key's record as sorted "field=value" pairs."""
		# TODO: implement
		pass

	# Level 2 Methods: Scans & Ranking

	def scan_prefix(self, timestamp: int, key: str, prefix: str) -> str:
		"""Get a key's "field=value" pairs whose field name starts with prefix."""
		# TODO: implement
		pass

	def top_n_keys(self, timestamp: int, n: int) -> str:
		"""Get the top n keys by number of live fields."""
		# TODO: implement
		pass

	# Level 3 Methods: TTL

	def set_field_with_ttl(self, timestamp: int, key: str, field: str, value: str, ttl: int) -> str:
		"""Set a field that is valid for [timestamp, timestamp + ttl)."""
		# TODO: implement
		pass

	# Level 4 Methods: Backup & Restore

	def backup(self, timestamp: int) -> str:
		"""Snapshot the database, recording each ttl-field's remaining ttl."""
		# TODO: implement
		pass

	def restore(self, timestamp: int, backup_timestamp: int) -> str:
		"""Restore the most recent backup whose time is <= backup_timestamp."""
		# TODO: implement
		pass
